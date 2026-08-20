import json
import os
import sys
from pathlib import Path

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QGraphicsScene
from PySide6.QtGui import QPixmap, QImage, Qt
import cv2
import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from gen.Ui_MainWindow import Ui_MainWindow


class MainWindow(QMainWindow):


    MAX_BATCH_IMAGES = 20

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.golden_file_path = None
        self.golden_image = None
        self.batch_image = None
        self.batch_images = []
        self.batch_paths = []
        self.current_index = 0
        self.approval_array = ["Unrated"] * self.MAX_BATCH_IMAGES
        assets_dir = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "assets"))
        self.red_x = cv2.imread(os.path.join(assets_dir, "red-x.png"))
        self.green_check = cv2.imread(os.path.join(assets_dir, "green-check.png"))
        self.white_space = cv2.imread(os.path.join(assets_dir, "whiteScreen.png"))
        self.logo = cv2.imread(os.path.join(assets_dir, "G-logo.png"))
        self.approval_image = self.ui.approvalView

        self.ui.uploadGolden.clicked.connect(lambda: self.upload_button_clicked(self.ui.uploadGolden))
        self.ui.uploadBatch.clicked.connect(lambda: self.upload_button_clicked(self.ui.uploadBatch))
        self.ui.previousButton.clicked.connect(self.prev_batch_image)
        self.ui.nextButton.clicked.connect(self.next_batch_image)
        self.ui.similarButton.clicked.connect(lambda: self.rate_image(True))
        self.ui.dissimilarButton.clicked.connect(lambda: self.rate_image(False))
        #self.ui.algorithmButton.clicked.connect(self.create_json)
        self.ui.algorithmButton.clicked.connect(self.algorithm_button_clicked)
        self.ui.actionSave.triggered.connect(self.save_button)
        self.ui.actionExit.triggered.connect(self.close)
        self.ui.actionAuto.triggered.connect(self.auto_calculate)
        self.ui.actionLoad.triggered.connect(self.load_save)

        self.setWindowTitle("Gregs Image Comparison")
        self.setWindowIcon(QPixmap(os.path.join(assets_dir, "G-logo.png")))
        self.ui.approvalView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.approvalView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.truth_val_changed("Unrated")

    #start of pipeline for image upload, processing, display.
    def upload_button_clicked(self, button):
        try:
            if button == self.ui.uploadGolden:
                self.golden_file_path = QFileDialog.getOpenFileName(self, "Select Image", "", "Image Files (*.png *.jpg *.bmp)")
                if self.golden_file_path[0] != '':
                    processed_image = self.image_process(self.golden_file_path[0])
                    if processed_image is not None:
                        self.golden_image = processed_image
                        self.display_image(processed_image, self.ui.goldenView)
                else:
                    #print("No file selected.")
                    QMessageBox.warning(self, "Error", "Please select a file to upload.")
                return
            elif button == self.ui.uploadBatch:
                QMessageBox.information(self, "Batch Upload", f"Please select up to {self.MAX_BATCH_IMAGES} images")
                filepaths = QFileDialog.getOpenFileNames(self, "Select Image(s)", "", "Image Files (*.png *.jpg *.bmp)")
                selected_paths = filepaths[0]

                if not selected_paths:
                    #print("No files selected.")
                    QMessageBox.warning(self, "Error", "Please select at least one file to upload.")
                    return

                if len(selected_paths) > self.MAX_BATCH_IMAGES:
                    QMessageBox.warning(
                        self,
                        "Batch Limit Reached",
                        f"You selected {len(selected_paths)} images. Only the first {self.MAX_BATCH_IMAGES} will be used."
                    )
                    selected_paths = selected_paths[:self.MAX_BATCH_IMAGES]

                processed_images = []
                valid_paths = []

                for path in selected_paths:
                    image = self.image_process(path)
                    if image is not None:
                        processed_images.append(image)
                        valid_paths.append(path)

                if not processed_images:
                    return

                if len(processed_images) < len(selected_paths):
                    QMessageBox.warning(
                        self,
                        "Invalid Images",
                        f"Some selected images were not valid color images and have been skipped. {len(processed_images)} valid images loaded."
                    )

                self.truth_val_changed("Unrated")
                self.batch_images = processed_images
                self.batch_paths = valid_paths
                self.current_index = 0
                self.approval_array = ["Unrated"] * self.MAX_BATCH_IMAGES
                self.batch_image = processed_images[0]
                self.display_image(processed_images[0], self.ui.batchView)

                if len(processed_images) > 1:
                    QMessageBox.information(
                        self,
                        "Batch Loaded",
                        f"Loaded {len(processed_images)} batch images."
                    )
                self.ui.indexTrackerText.setText(f"{self.current_index + 1}/{len(self.batch_images)}")
                return
            else:
                QMessageBox.warning(self, "Error", "Unsupported upload button.")
                return
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")

    #turns image path into image object, uses check color function to determine if image is used
    def image_process(self, image_path):
        try:
            image = cv2.imread(image_path)
            if image is None:
                QMessageBox.critical(self, "Error", "Failed to load the image. Please check the file path.")
                return None
            if not self.check_color(image):
                return None
            return image

        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred while processing the image: {str(e)}")
            return None

    #converts image to b g r, if all channels are equal image has no color
    def check_color(self, image):
        try:
            b, g, r = cv2.split(image)
            if (np.array_equal(b, g) and np.array_equal(g, r)):
                QMessageBox.critical(self, "Error", "This program only supports color images.")
                return False
            return True
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred while checking the image color: {str(e)}")
            return False

    #turns image into displayable pixel map
    def image_to_pixmap(self, image):
        try:
            rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb.shape
            qimg = QImage(rgb.data, w, h, ch * w, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(qimg)
            return pixmap
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred while converting the image to pixmap: {str(e)}")
            return None

    #displays image to specified graphics view
    def display_image(self, pixel_map, graphics_view):
        try:
            if isinstance(pixel_map, QPixmap):
                pixmap = pixel_map
            else:
                pixmap = self.image_to_pixmap(pixel_map)
            if pixmap is not None:
                scene = QGraphicsScene()
                scene.addPixmap(pixmap)
                graphics_view.setScene(scene)
                graphics_view.fitInView(scene.sceneRect(), Qt.KeepAspectRatio)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred while displaying the image: {str(e)}")

    #moves batch image index forward, updates display and index tracker text
    def next_batch_image(self):
        if self.batch_images and len(self.batch_images) > 1:
            if (self.current_index + 1) >= len(self.batch_images):
                return
            self.current_index += 1
            self.truth_val_changed(self.approval_array[self.current_index])
            self.batch_image = self.batch_images[self.current_index]
            self.display_image(self.batch_image, self.ui.batchView)
            self.ui.indexTrackerText.setText(f"{self.current_index + 1}/{len(self.batch_images)}")

    #moves batch image index backward, updates display and index tracker text
    def prev_batch_image(self):
        if self.batch_images and len(self.batch_images) > 1:
            if (self.current_index - 1) < 0:
                return
            self.current_index -= 1
            self.truth_val_changed(self.approval_array[self.current_index])
            self.batch_image = self.batch_images[self.current_index]
            self.display_image(self.batch_image, self.ui.batchView)
            self.ui.indexTrackerText.setText(f"{self.current_index + 1}/{len(self.batch_images)}")

    #creates parsable json file for current batch and rating
    def create_json(self, save_path):
        if self.batch_images is not None:
            image_data = {"images": []}
            image_ID = 0
            for path in self.batch_paths:
                image_data["images"].append({"id": image_ID, "path": path, "similarity": self.approval_array[image_ID]})
                image_ID += 1
            image_data["golden_image"] = {"path": self.golden_file_path[0] if self.golden_file_path else None}
            with open(save_path, "w") as file:
                json.dump(image_data, file, indent=4)

    #rates the current batch image as similar or dissimilar to the golden image
    def rate_image(self, approval):
        if self.batch_images and self.golden_image is not None:
            self.approval_array[self.current_index] = approval
            self.truth_val_changed(approval)
        else:
            QMessageBox.warning(self, "Error", "upload golden and batch images before rating.")
            return

    #first algorithm, compares to see if they are the exact same image
    def exact_algorithm(self):
        if self.batch_images and self.golden_image is not None:
            curr_image = self.batch_images[self.current_index]
            r1, g1, b1 = cv2.split(curr_image)
            r2, g2, b2 = cv2.split(self.golden_image)
            if (np.array_equal(r1, r2) and np.array_equal(g1, g2) and np.array_equal(b1, b2)):
                return True
            else:
                return False
        else:
            QMessageBox.warning(self, "Error", "upload golden and batch images")
            return

    #algorithm that makes controus from batch and golden image, compares largest one and sends results
    def contour_algorithm(self):
        if self.batch_images and self.golden_image is not None:
            curr_image = self.batch_images[self.current_index]
            gray_batch = cv2.cvtColor(curr_image, cv2.COLOR_BGR2GRAY)
            gray_golden = cv2.cvtColor(self.golden_image, cv2.COLOR_BGR2GRAY)
            _, thresh_batch = cv2.threshold(gray_batch, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            _, thresh_golden = cv2.threshold(gray_golden, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            contours, _ = cv2.findContours(thresh_batch, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            golden_contours, _ = cv2.findContours(thresh_golden, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            if not contours or not golden_contours:
                return False

            batch_contour = max(contours, key=cv2.contourArea)
            golden_contour = max(golden_contours, key=cv2.contourArea)

            if (cv2.matchShapes(batch_contour, golden_contour, cv2.CONTOURS_MATCH_I1, 0.0) < 0.1):
                return True
            else:
                return False

    #uses both algorithms to determine if imagese are similar or not
    def algorithm_button_clicked(self):
        if self.batch_images and self.golden_image is not None:
            result = self.exact_algorithm()
            if result:
                self.approval_array[self.current_index] = True
            else:
                self.approval_array[self.current_index] = self.contour_algorithm()
            self.truth_val_changed(self.approval_array[self.current_index])

    #updates approval image based on truth value chosen
    def truth_val_changed(self, truth_val):
        if (truth_val == True):
            self.display_image(self.green_check, self.approval_image)
            return
        if (truth_val == False):
            self.display_image(self.red_x, self.approval_image)
            return
        else:
            self.display_image(self.white_space, self.approval_image)
            return

    #overrides resize event to ensure images are resized when window is resized
    def resizeEvent(self, event):
        super().resizeEvent(event)
        if self.golden_image is not None:
            self.display_image(self.golden_image, self.ui.goldenView)
        if self.batch_images:
            self.display_image(self.batch_images[self.current_index], self.ui.batchView)
            self.truth_val_changed(self.approval_array[self.current_index])
        else:
            self.truth_val_changed("Unrated")

    def save_button(self):
        save_path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "JSON Files (*.json)")
        if save_path:
            if save_path[-5:] != ".json":
                save_path += ".json"
            self.create_json(save_path)

    def auto_calculate(self):
        if self.batch_images and self.golden_image is not None:
            reply = QMessageBox.question(
                self,
                "Auto algorithm",
                "Auto algorithm will override all manual ratings. Proceed?",
                QMessageBox.Yes | QMessageBox.No
            )
            if reply == QMessageBox.No:
                return
            for i in range(len(self.batch_images)):
                self.current_index = i
                self.algorithm_button_clicked()
            for i in range(len(self.batch_images)):
                self.prev_batch_image()
            self.batch_image = self.batch_images[self.current_index]
            self.display_image(self.batch_image, self.ui.batchView)
            self.ui.indexTrackerText.setText(f"{self.current_index + 1}/{len(self.batch_images)}")
        else:
            QMessageBox.warning(self, "Error", "upload golden and batch images before auto calculating.")
            return

    def load_save(self):
        QMessageBox.information(self, "Load Save", "image file paths must not have changed since last save")
        save_path, _ = QFileDialog.getOpenFileName(self, "Select JSON File", "", "JSON Files (*.json)")
        if save_path:
            try:
                with open(save_path, "r") as file:
                    image_data = json.load(file)
                golden_image_path = image_data.get("golden_image", {}).get("path")
                if golden_image_path and os.path.exists(golden_image_path):
                    self.golden_file_path = (golden_image_path,)
                    self.golden_image = self.image_process(golden_image_path)
                    if self.golden_image is not None:
                        self.display_image(self.golden_image, self.ui.goldenView)
                else:
                    QMessageBox.warning(self, "Error", "Golden image path is invalid or does not exist.")

                batch_images_data = image_data.get("images", [])
                valid_paths = []
                processed_images = []
                for img in batch_images_data:
                    path = img.get("path")
                    if path and os.path.exists(path):
                        image = self.image_process(path)
                        if image is not None:
                            processed_images.append(image)
                            valid_paths.append(path)

                if not processed_images:
                    QMessageBox.warning(self, "Error", "No valid batch images found in the JSON file.")
                    return

                if len(processed_images) < len(batch_images_data):
                    QMessageBox.warning(self, "Invalid Images", f"Some images in JSON file invalid."
                    )

                self.batch_images = processed_images
                self.batch_paths = valid_paths
                self.current_index = 0
                self.approval_array = [img.get("similarity", "Unrated") for img in batch_images_data]
                self.batch_image = processed_images[0]
                self.truth_val_changed(self.approval_array[self.current_index])
                self.display_image(processed_images[0], self.ui.batchView)
                self.ui.indexTrackerText.setText(f"{self.current_index + 1}/{len(self.batch_images)}")

            except Exception as e:
                QMessageBox.critical(self, "Error", f"An error occurred while loading the JSON file: {str(e)}")
            
app = QApplication([])
window = MainWindow()
window.show()
app.exec()
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QGraphicsScene
from PySide6.QtGui import QPixmap, QImage, Qt
from Ui_MainWindow import Ui_MainWindow
import cv2
import numpy as np
import json
import os

class MainWindow(QMainWindow):
    MAX_BATCH_IMAGES = 20

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.filepath = None
        self.goldenImage = None
        self.batchImage = None
        self.batchImages = []
        self.batchPaths = []
        self.current_index = 0
        self.approval_array = ["Unrated"] * self.MAX_BATCH_IMAGES
        assets_dir = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "assets"))
        self.redX = cv2.imread(os.path.join(assets_dir, "red-x.png"))
        self.greenCheck = cv2.imread(os.path.join(assets_dir, "green-check.png"))
        self.whiteSpace = cv2.imread(os.path.join(assets_dir, "whiteScreen.png"))
        self.logo = cv2.imread(os.path.join(assets_dir, "G-logo.png"))
        self.approvalImage = self.ui.approvalView

        self.ui.uploadGolden.clicked.connect(lambda: self.upload_button_clicked(self.ui.uploadGolden))
        self.ui.uploadBatch.clicked.connect(lambda: self.upload_button_clicked(self.ui.uploadBatch))
        self.ui.previousButton.clicked.connect(self.prevBatchImage)
        self.ui.nextButton.clicked.connect(self.nextBatchImage)
        self.ui.similarButton.clicked.connect(lambda: self.rateImage(True))
        self.ui.dissimilarButton.clicked.connect(lambda: self.rateImage(False))
        #self.ui.algorithmButton.clicked.connect(self.create_JSON)
        self.ui.algorithmButton.clicked.connect(self.algorithm_button_clicked)

        self.setWindowTitle("Gregs Image Comparison")
        self.setWindowIcon(QPixmap(os.path.join(assets_dir, "G-logo.png")))
        self.ui.approvalView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.approvalView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.truth_val_changed("Unrated")

    #start of pipeline for image upload, processing, display.
    def upload_button_clicked(self, button):
        try:
            if button == self.ui.uploadGolden:
                filepath = QFileDialog.getOpenFileName(self, "Select Image", "", "Image Files (*.png *.jpg *.bmp)")
                if filepath[0] != '':
                    processed_image = self.image_process(filepath[0])
                    if processed_image is not None:
                        self.goldenImage = processed_image
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
                self.batchImages = processed_images
                self.batchPaths = valid_paths
                self.current_index = 0
                self.approval_array = ["Unrated"] * self.MAX_BATCH_IMAGES
                self.batchImage = processed_images[0]
                self.display_image(processed_images[0], self.ui.batchView)

                if len(processed_images) > 1:
                    QMessageBox.information(
                        self,
                        "Batch Loaded",
                        f"Loaded {len(processed_images)} batch images."
                    )
                self.ui.indexTrackerText.setText(f"{self.current_index + 1}/{len(self.batchImages)}")
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
    def display_image(self, image, graphics_view):
        try:
            if isinstance(image, QPixmap):
                pixmap = image
            else:
                pixmap = self.image_to_pixmap(image)
            if pixmap is not None:
                scene = QGraphicsScene()
                scene.addPixmap(pixmap)
                graphics_view.setScene(scene)
                graphics_view.fitInView(scene.sceneRect(), Qt.KeepAspectRatio)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred while displaying the image: {str(e)}")

    #moves batch image index forward, updates display and index tracker text
    def nextBatchImage(self):
        if self.batchImages and len(self.batchImages) > 1:
            if (self.current_index + 1) >= len(self.batchImages):
                return
            self.current_index += 1
            self.truth_val_changed(self.approval_array[self.current_index])
            self.batchImage = self.batchImages[self.current_index]
            self.display_image(self.batchImage, self.ui.batchView)
            self.ui.indexTrackerText.setText(f"{self.current_index + 1}/{len(self.batchImages)}")

    #moves batch image index backward, updates display and index tracker text
    def prevBatchImage(self):
        if self.batchImages and len(self.batchImages) > 1:
            if (self.current_index - 1) < 0:
                return
            self.current_index -= 1
            self.truth_val_changed(self.approval_array[self.current_index])
            self.batchImage = self.batchImages[self.current_index]
            self.display_image(self.batchImage, self.ui.batchView)
            self.ui.indexTrackerText.setText(f"{self.current_index + 1}/{len(self.batchImages)}")

    #creates parsable json file for current batch and rating
    def create_JSON(self):
        if self.batchImages is not None:
            image_data = {"images": []}
            imageId = 0
            for path in self.batchPaths:
                image_data["images"].append({"id": imageId, "path": path, "similarity": self.approval_array[imageId]})
                imageId += 1
            with open("data.json", "w") as file:
                json.dump(image_data, file, indent=4)

            data = json.load(open("data.json"))

    #rates the current batch image as similar or dissimilar to the golden image
    def rateImage(self, approval):
        if self.batchImages and self.goldenImage is not None:
            self.approval_array[self.current_index] = approval
            self.truth_val_changed(approval)
        else:
            QMessageBox.warning(self, "Error", "upload golden and batch images before rating.")
            return

    #first algorithm, compares to see if they are the exact same image
    def exact_algorithm(self):
        if self.batchImages and self.goldenImage is not None:
            currImage = self.batchImages[self.current_index]
            r1, g1, b1 = cv2.split(currImage)
            r2, g2, b2 = cv2.split(self.goldenImage)
            if (np.array_equal(r1, r2) and np.array_equal(g1, g2) and np.array_equal(b1, b2)):
                return True
            else:
                return False
        else:
            QMessageBox.warning(self, "Error", "upload golden and batch images")
            return

    #algorithm that makes controus from batch and golden image, compares largest one and sends results
    def contour_algorithm(self):
        if self.batchImages and self.goldenImage is not None:
            currImage = self.batchImages[self.current_index]
            grayBatch = cv2.cvtColor(currImage, cv2.COLOR_BGR2GRAY)
            grayGolden = cv2.cvtColor(self.goldenImage, cv2.COLOR_BGR2GRAY)
            _, threshBatch = cv2.threshold(grayBatch, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            _, threshGolden = cv2.threshold(grayGolden, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            contours, _ = cv2.findContours(threshBatch, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            goldenContours, _ = cv2.findContours(threshGolden, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            if not contours or not goldenContours:
                return False

            batchContour = max(contours, key=cv2.contourArea)
            goldenContour = max(goldenContours, key=cv2.contourArea)

            if (cv2.matchShapes(batchContour, goldenContour, cv2.CONTOURS_MATCH_I1, 0.0) < 0.1):
                return True
            else:
                return False

    #uses both algorithms to determine if imagese are similar or not
    def algorithm_button_clicked(self):
        if self.batchImages and self.goldenImage is not None:
            result = self.exact_algorithm()
            if result:
                self.approval_array[self.current_index] = True
            else:
                self.approval_array[self.current_index] = self.contour_algorithm()
            self.truth_val_changed(self.approval_array[self.current_index])

    #updates approval image based on truth value chosen
    def truth_val_changed(self, truthVal):
        if (truthVal == True):
            self.display_image(self.greenCheck, self.approvalImage)
            return
        if (truthVal == False):
            self.display_image(self.redX, self.approvalImage)
            return
        else:
            self.display_image(self.whiteSpace, self.approvalImage)
            return

    #overrides resize event to ensure images are resized when window is resized
    def resizeEvent(self, event):
        super().resizeEvent(event)
        if self.goldenImage is not None:
            self.display_image(self.goldenImage, self.ui.goldenView)
        if self.batchImage is not None:
            self.display_image(self.batchImage, self.ui.batchView)
        if self.batchImages:
            self.truth_val_changed(self.approval_array[self.current_index])
        else:
            self.truth_val_changed("Unrated")
            
app = QApplication([])
window = MainWindow()
window.show()
app.exec()
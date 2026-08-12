from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QGraphicsScene
from PySide6.QtGui import QPixmap, QImage, Qt
from Ui_MainWindow import Ui_MainWindow
import cv2
import numpy as np

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.filepath = None
        self.goldenImage = None

        self.ui.uploadGolden.clicked.connect(self.button_clicked)

    def button_clicked(self):
        try:
            filepath = QFileDialog.getOpenFileName(self, "Select Golden Image", "", "Image Files (*.png *.jpg *.bmp)")
            if filepath[0] != '':
                self.goldenImage = self.image_process(filepath[0])
                if self.goldenImage is not None:
                    self.display_image(self.goldenImage, self.ui.goldenView)
            else:
                print("No file selected.")
                QMessageBox.warning(self, "Error", "Please select a file to upload.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")

    def image_process(self, image_path):
        try:
            # Load the image
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

    def display_image(self, image, graphics_view):
        try:
            pixmap = self.image_to_pixmap(image)
            if pixmap is not None:
                scene = QGraphicsScene()
                scene.addPixmap(pixmap)
                graphics_view.setScene(scene)
                graphics_view.fitInView(scene.sceneRect(), Qt.KeepAspectRatio)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred while displaying the image: {str(e)}")
        
app = QApplication([])
window = MainWindow()
window.show()
app.exec()
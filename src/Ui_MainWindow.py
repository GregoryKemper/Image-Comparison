# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainGUI.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGraphicsView, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(841, 562)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.uploadGolden = QPushButton(self.centralwidget)
        self.uploadGolden.setObjectName(u"uploadGolden")
        self.uploadGolden.setGeometry(QRect(140, 20, 131, 61))
        self.goldenView = QGraphicsView(self.centralwidget)
        self.goldenView.setObjectName(u"goldenView")
        self.goldenView.setGeometry(QRect(10, 80, 371, 271))
        self.batchView = QGraphicsView(self.centralwidget)
        self.batchView.setObjectName(u"batchView")
        self.batchView.setGeometry(QRect(410, 80, 371, 271))
        self.uploadBatch = QPushButton(self.centralwidget)
        self.uploadBatch.setObjectName(u"uploadBatch")
        self.uploadBatch.setGeometry(QRect(530, 20, 131, 61))
        self.previousButton = QPushButton(self.centralwidget)
        self.previousButton.setObjectName(u"previousButton")
        self.previousButton.setGeometry(QRect(490, 360, 81, 26))
        self.nextButton = QPushButton(self.centralwidget)
        self.nextButton.setObjectName(u"nextButton")
        self.nextButton.setGeometry(QRect(620, 360, 81, 26))
        self.similarButton = QPushButton(self.centralwidget)
        self.similarButton.setObjectName(u"similarButton")
        self.similarButton.setGeometry(QRect(450, 410, 81, 81))
        self.dissimilarButton = QPushButton(self.centralwidget)
        self.dissimilarButton.setObjectName(u"dissimilarButton")
        self.dissimilarButton.setGeometry(QRect(360, 410, 81, 81))
        self.algorithmButton = QPushButton(self.centralwidget)
        self.algorithmButton.setObjectName(u"algorithmButton")
        self.algorithmButton.setGeometry(QRect(270, 410, 81, 81))
        self.indexTrackerText = QLineEdit(self.centralwidget)
        self.indexTrackerText.setObjectName(u"indexTrackerText")
        self.indexTrackerText.setGeometry(QRect(570, 360, 51, 26))
        self.indexTrackerText.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.indexTrackerText.setReadOnly(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 841, 33))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.uploadGolden.setText(QCoreApplication.translate("MainWindow", u"Upload Golden", None))
        self.uploadBatch.setText(QCoreApplication.translate("MainWindow", u"Upload Batch", None))
        self.previousButton.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.nextButton.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.similarButton.setText(QCoreApplication.translate("MainWindow", u"Similar", None))
        self.dissimilarButton.setText(QCoreApplication.translate("MainWindow", u"Dissimilar", None))
        self.algorithmButton.setText(QCoreApplication.translate("MainWindow", u"Algorithm", None))
        self.indexTrackerText.setText(QCoreApplication.translate("MainWindow", u"0/0", None))
    # retranslateUi


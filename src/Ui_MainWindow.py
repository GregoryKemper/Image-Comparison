# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'testgui.ui'
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
from PySide6.QtWidgets import (QApplication, QGraphicsView, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(841, 600)
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
        self.uploadGolden.setGeometry(QRect(130, 350, 131, 61))
        self.goldenView = QGraphicsView(self.centralwidget)
        self.goldenView.setObjectName(u"goldenView")
        self.goldenView.setGeometry(QRect(80, 120, 256, 192))
        self.batchView = QGraphicsView(self.centralwidget)
        self.batchView.setObjectName(u"batchView")
        self.batchView.setGeometry(QRect(390, 120, 256, 192))
        self.uploadBatch = QPushButton(self.centralwidget)
        self.uploadBatch.setObjectName(u"uploadBatch")
        self.uploadBatch.setGeometry(QRect(450, 350, 131, 61))
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
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainGUILayout.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGraphicsView, QHBoxLayout, QLayout,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(841, 562)
        MainWindow.setMinimumSize(QSize(400, 400))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush)
        MainWindow.setPalette(palette)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setSpacing(16)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.uploadGolden = QPushButton(self.centralwidget)
        self.uploadGolden.setObjectName(u"uploadGolden")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.uploadGolden.sizePolicy().hasHeightForWidth())
        self.uploadGolden.setSizePolicy(sizePolicy1)
        self.uploadGolden.setMinimumSize(QSize(0, 50))

        self.horizontalLayout.addWidget(self.uploadGolden)

        self.uploadBatch = QPushButton(self.centralwidget)
        self.uploadBatch.setObjectName(u"uploadBatch")
        sizePolicy1.setHeightForWidth(self.uploadBatch.sizePolicy().hasHeightForWidth())
        self.uploadBatch.setSizePolicy(sizePolicy1)
        self.uploadBatch.setMinimumSize(QSize(0, 50))

        self.horizontalLayout.addWidget(self.uploadBatch)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.goldenView = QGraphicsView(self.centralwidget)
        self.goldenView.setObjectName(u"goldenView")
        self.goldenView.setAcceptDrops(False)

        self.horizontalLayout_2.addWidget(self.goldenView)

        self.batchView = QGraphicsView(self.centralwidget)
        self.batchView.setObjectName(u"batchView")
        self.batchView.setAcceptDrops(False)

        self.horizontalLayout_2.addWidget(self.batchView)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.horizontalSpacer = QSpacerItem(80, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.previousButton = QPushButton(self.centralwidget)
        self.previousButton.setObjectName(u"previousButton")
        sizePolicy1.setHeightForWidth(self.previousButton.sizePolicy().hasHeightForWidth())
        self.previousButton.setSizePolicy(sizePolicy1)
        self.previousButton.setMinimumSize(QSize(0, 35))
        self.previousButton.setMaximumSize(QSize(16777215, 50))

        self.horizontalLayout_3.addWidget(self.previousButton)

        self.indexTrackerText = QLineEdit(self.centralwidget)
        self.indexTrackerText.setObjectName(u"indexTrackerText")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.indexTrackerText.sizePolicy().hasHeightForWidth())
        self.indexTrackerText.setSizePolicy(sizePolicy2)
        self.indexTrackerText.setMinimumSize(QSize(50, 35))
        self.indexTrackerText.setMaximumSize(QSize(50, 50))
        self.indexTrackerText.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.indexTrackerText.setMaxLength(20)
        self.indexTrackerText.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.indexTrackerText)

        self.approvalView = QGraphicsView(self.centralwidget)
        self.approvalView.setObjectName(u"approvalView")
        self.approvalView.setMinimumSize(QSize(50, 35))
        self.approvalView.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_3.addWidget(self.approvalView)

        self.nextButton = QPushButton(self.centralwidget)
        self.nextButton.setObjectName(u"nextButton")
        sizePolicy1.setHeightForWidth(self.nextButton.sizePolicy().hasHeightForWidth())
        self.nextButton.setSizePolicy(sizePolicy1)
        self.nextButton.setMinimumSize(QSize(0, 35))
        self.nextButton.setMaximumSize(QSize(16777215, 50))

        self.horizontalLayout_3.addWidget(self.nextButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.algorithmButton = QPushButton(self.centralwidget)
        self.algorithmButton.setObjectName(u"algorithmButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.algorithmButton.sizePolicy().hasHeightForWidth())
        self.algorithmButton.setSizePolicy(sizePolicy3)
        self.algorithmButton.setMinimumSize(QSize(50, 50))
        self.algorithmButton.setMaximumSize(QSize(175, 100))

        self.horizontalLayout_4.addWidget(self.algorithmButton)

        self.dissimilarButton = QPushButton(self.centralwidget)
        self.dissimilarButton.setObjectName(u"dissimilarButton")
        self.dissimilarButton.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.dissimilarButton.sizePolicy().hasHeightForWidth())
        self.dissimilarButton.setSizePolicy(sizePolicy3)
        self.dissimilarButton.setMinimumSize(QSize(50, 50))
        self.dissimilarButton.setMaximumSize(QSize(175, 100))

        self.horizontalLayout_4.addWidget(self.dissimilarButton)

        self.similarButton = QPushButton(self.centralwidget)
        self.similarButton.setObjectName(u"similarButton")
        sizePolicy3.setHeightForWidth(self.similarButton.sizePolicy().hasHeightForWidth())
        self.similarButton.setSizePolicy(sizePolicy3)
        self.similarButton.setMinimumSize(QSize(50, 50))
        self.similarButton.setMaximumSize(QSize(175, 100))

        self.horizontalLayout_4.addWidget(self.similarButton)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.verticalLayout_2.setStretch(1, 1)

        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 841, 33))
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy4)
        self.menubar.setMinimumSize(QSize(0, 0))
        palette1 = QPalette()
        brush1 = QBrush(QColor(255, 255, 255, 228))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush2)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush1)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush2)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush2)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush2)
        self.menubar.setPalette(palette1)
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuFile.setMinimumSize(QSize(0, 0))
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.uploadGolden.setText(QCoreApplication.translate("MainWindow", u"Upload Golden", None))
        self.uploadBatch.setText(QCoreApplication.translate("MainWindow", u"Upload Batch", None))
        self.previousButton.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.indexTrackerText.setText(QCoreApplication.translate("MainWindow", u"0/0", None))
        self.nextButton.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.algorithmButton.setText(QCoreApplication.translate("MainWindow", u"Algorithm", None))
        self.dissimilarButton.setText(QCoreApplication.translate("MainWindow", u"Dissimilar", None))
        self.similarButton.setText(QCoreApplication.translate("MainWindow", u"Similar", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi


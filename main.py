# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1100, 816)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Moon")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("bin/rocket.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setStyleSheet("")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(600, 600))
        self.centralwidget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(185, 43, 39, 255), stop:1 rgba(21, 101, 192, 255));\n"
"border-radius : 25px ;")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_7 = QtWidgets.QFrame(self.centralwidget)
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_7.setStyleSheet("background-color: rgb(255, 255, 255,0.2);")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_9 = QtWidgets.QFrame(self.frame_7)
        self.frame_9.setStyleSheet("border-radius : 25px  ;")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.label_4 = QtWidgets.QLabel(self.frame_9)
        self.label_4.setGeometry(QtCore.QRect(20, 15, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Moon")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color:transparent ;")
        self.label_4.setObjectName("label_4")
        self.label_8 = QtWidgets.QLabel(self.frame_9)
        self.label_8.setGeometry(QtCore.QRect(100, 30, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Moon")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color:transparent ;\n"
"font: 75 10pt \"Moon\";")
        self.label_8.setObjectName("label_8")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_9)
        self.pushButton_3.setGeometry(QtCore.QRect(258, 17, 35, 35))
        self.pushButton_3.setStyleSheet("background-color:transparent ;")
        self.pushButton_3.setText("")
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.frame_9)
        self.frame_6 = QtWidgets.QFrame(self.frame_7)
        self.frame_6.setMaximumSize(QtCore.QSize(150, 70))
        self.frame_6.setStyleSheet("background-color: transparent ;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_6.setSizeIncrement(QtCore.QSize(0, 0))
        self.pushButton_6.setBaseSize(QtCore.QSize(0, 0))
        self.pushButton_6.setTabletTracking(False)
        self.pushButton_6.setStyleSheet("        QPushButton\n"
"        {\n"
"            color: #b1b1b1;\n"
"            border-radius: 15px;\n"
"            padding: 3px;\n"
"            padding-left: 5px;\n"
"            padding-right: 5px;\n"
"    font: 75 14pt \"Moon\";\n"
"        }\n"
"        \n"
"        QPushButton:pressed\n"
"        {\n"
"            background-color: rgb(255, 255, 255);\n"
"        }\n"
"        \n"
"        QPushButton:hover\n"
"        {\n"
"            border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"        }\n"
"")
        self.pushButton_6.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("bin/minimize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon1)
        self.pushButton_6.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_6.setAutoRepeat(False)
        self.pushButton_6.setAutoExclusive(False)
        self.pushButton_6.setFlat(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout.addWidget(self.pushButton_6)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_5.setSizeIncrement(QtCore.QSize(0, 0))
        self.pushButton_5.setBaseSize(QtCore.QSize(0, 0))
        self.pushButton_5.setTabletTracking(False)
        self.pushButton_5.setStyleSheet("        QPushButton\n"
"        {\n"
"            color: #b1b1b1;\n"
"            border-radius: 15;\n"
"            padding: 3px;\n"
"            padding-left: 5px;\n"
"            padding-right: 5px;\n"
"    font: 75 14pt \"Moon\";\n"
"        }\n"
"        \n"
"        QPushButton:pressed\n"
"        {\n"
"            background-color: rgb(255, 255, 255);\n"
"        }\n"
"        \n"
"        QPushButton:hover\n"
"        {\n"
"            border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"        }\n"
"")
        self.pushButton_5.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("bin/maximize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon2)
        self.pushButton_5.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_5.setAutoRepeat(False)
        self.pushButton_5.setAutoExclusive(False)
        self.pushButton_5.setFlat(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_4.setSizeIncrement(QtCore.QSize(0, 0))
        self.pushButton_4.setBaseSize(QtCore.QSize(0, 0))
        self.pushButton_4.setTabletTracking(False)
        self.pushButton_4.setStyleSheet("        QPushButton\n"
"        {\n"
"            color: #b1b1b1;\n"
"            border-radius: 15;\n"
"            padding: 3px;\n"
"            padding-left: 5px;\n"
"            padding-right: 5px;\n"
"    font: 75 14pt \"Moon\";\n"
"        }\n"
"        \n"
"        QPushButton:pressed\n"
"        {\n"
"            background-color: rgb(255, 255, 255);\n"
"        }\n"
"        \n"
"        QPushButton:hover\n"
"        {\n"
"            border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"        }\n"
"")
        self.pushButton_4.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("bin/close-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_4.setAutoRepeat(False)
        self.pushButton_4.setAutoExclusive(False)
        self.pushButton_4.setFlat(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.horizontalLayout_2.addWidget(self.frame_6)
        self.verticalLayout.addWidget(self.frame_7)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame_10 = QtWidgets.QFrame(self.frame_4)
        self.frame_10.setGeometry(QtCore.QRect(20, 80, 471, 160))
        self.frame_10.setStyleSheet("QFrame { \n"
"background-color: rgb(255, 255, 255,0.2);\n"
"border-radius : 20px ;\n"
"}\n"
"\n"
"QFrame:hover {\n"
"\n"
"border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"\n"
"}\n"
"\n"
"QLineEdit {\n"
"background-color: rgb(0, 0, 0,0.3);\n"
"color : rgb(255, 255, 255) ;\n"
"border-radius : 10px ; }\n"
"        \n"
"QLineEdit:hover {border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a); }")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.label = QtWidgets.QLabel(self.frame_10)
        self.label.setGeometry(QtCore.QRect(200, 10, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Moon")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"font: 75 14pt \"Moon\";\n"
"background-color: rgb(255, 255, 255,0);\n"
"}\n"
"\n"
"QLabel:hover {border : 2px solid rgb(255, 0, 0,0)}")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_10)
        self.lineEdit.setGeometry(QtCore.QRect(32, 60, 421, 30))
        self.lineEdit.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lineEdit.setStyleSheet("font: 75 12pt \"Moon\";\n"
"padding-left : 4px ;\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.frame_10)
        self.label_2.setGeometry(QtCore.QRect(10, 65, 21, 20))
        font = QtGui.QFont()
        font.setFamily("Moon")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label_2.setObjectName("label_2")
        self.label.raise_()
        self.label_2.raise_()
        self.lineEdit.raise_()
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setGeometry(QtCore.QRect(20, 300, 431, 151))
        self.frame_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_5.setStyleSheet("QFrame { \n"
"background-color: rgb(255, 255, 255,0.2);\n"
"border-radius : 20px ;\n"
"}\n"
"\n"
"QFrame:hover {\n"
"border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QComboBox {\n"
"    background-color: rgb(0, 0, 0,0.3) ;\n"
"    border-radius:10px ;\n"
"    }\n"
"    QComboBox:hover {\n"
"     border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"    }\n"
"    \n"
"    \n"
"    QComboBox::drop-down\n"
"    {\n"
"         subcontrol-origin: padding;\n"
"         subcontrol-position: top right;\n"
"         width: 15px;\n"
"         border-left-width: 0px;\n"
"         border-left-color: darkgray;\n"
"         border-left-style: solid; /* just a single line */\n"
"         border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"         border-bottom-right-radius: 3px; \n"
"     }\n"
"    \n"
"    QComboBox QAbstractItemView\n"
"    {\n"
"        background-color: rgb(255, 255, 255);\n"
"         border: 2px solid darkgray; \n"
"        selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"    \n"
"    \n"
"    \n"
"    }\n"
"    \n"
"\n"
"")
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setLineWidth(1)
        self.frame_5.setObjectName("frame_5")
        self.label_5 = QtWidgets.QLabel(self.frame_5)
        self.label_5.setGeometry(QtCore.QRect(160, 10, 141, 31))
        self.label_5.setStyleSheet("QLabel {\n"
"font: 75 14pt \"Moon\";\n"
"background-color: rgb(255, 255, 255,0);\n"
"}\n"
"\n"
"QLabel:hover {border : 2px solid rgb(255, 0, 0,0)}")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame_5)
        self.label_6.setGeometry(QtCore.QRect(10, 65, 21, 20))
        font = QtGui.QFont()
        font.setFamily("Moon")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label_6.setObjectName("label_6")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_5)
        self.comboBox_2.setGeometry(QtCore.QRect(30, 60, 391, 30))
        font = QtGui.QFont()
        font.setFamily("Moon")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.comboBox_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_2.setStyleSheet("font: 75 14pt \"Moon\";")
        self.comboBox_2.setEditable(False)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 0, 50, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setStyleSheet("        QPushButton\n"
"        {\n"
"            background-color:transparent;\n"
"            color: rgb(0, 0, 0);\n"
"            border-width: 1px;\n"
"            border-radius: 15;\n"
"            font: 75 14pt \"Moon\";\n"
"        }\n"
"        \n"
"        QPushButton:pressed\n"
"        {\n"
"    background-color: rgb(180, 180, 180,0.3);\n"
"        }\n"
"        \n"
"        QPushButton:hover\n"
"        {\n"
"            border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"            padding-right: 3px;\n"
"            padding-top : 3px ;\n"
"        }\n"
"")
        self.pushButton_7.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("bin/fb.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon4)
        self.pushButton_7.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_8.setGeometry(QtCore.QRect(80, 0, 50, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setStyleSheet("        QPushButton\n"
"        {\n"
"            background-color:transparent;\n"
"            color: rgb(0, 0, 0);\n"
"            border-width: 1px;\n"
"            border-radius: 15;\n"
"            font: 75 14pt \"Moon\";\n"
"        }\n"
"        \n"
"        QPushButton:pressed\n"
"        {\n"
"    background-color: rgb(180, 180, 180,0.3);\n"
"        }\n"
"        \n"
"        QPushButton:hover\n"
"        {\n"
"            border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"            padding-right: 3px;\n"
"            padding-bottom : 3px ;\n"
"        }\n"
"")
        self.pushButton_8.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("bin/Octocat.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon5)
        self.pushButton_8.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_3.addWidget(self.frame_4)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setStyleSheet("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_8 = QtWidgets.QFrame(self.frame_3)
        self.frame_8.setGeometry(QtCore.QRect(50, 80, 381, 160))
        self.frame_8.setStyleSheet("QFrame { \n"
"background-color: rgb(255, 255, 255,0.2);\n"
"border-radius : 20px ;\n"
"}\n"
"\n"
"QFrame:hover {\n"
"border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QLineEdit {\n"
"background-color: rgb(0, 0, 0,0.3);\n"
"color : rgb(255, 255, 255) ;\n"
"border-radius : 10px ; }\n"
"        \n"
"QLineEdit:hover {border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);}\n"
"")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.label_7 = QtWidgets.QLabel(self.frame_8)
        self.label_7.setGeometry(QtCore.QRect(190, 10, 81, 31))
        self.label_7.setStyleSheet("QLabel {\n"
"font: 75 14pt \"Moon\";\n"
"background-color: rgb(255, 255, 255,0);\n"
"}\n"
"\n"
"QLabel:hover {border : 2px solid rgb(255, 0, 0,0)}")
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.frame_8)
        self.label_9.setGeometry(QtCore.QRect(10, 66, 21, 20))
        font = QtGui.QFont()
        font.setFamily("Moon")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label_9.setObjectName("label_9")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_8)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 60, 341, 30))
        self.lineEdit_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lineEdit_2.setStyleSheet("font: 75 12pt \"Moon\";\n"
"padding-left : 4px ;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_2.setGeometry(QtCore.QRect(154, 110, 100, 30))
        self.pushButton_2.setStyleSheet("        QPushButton\n"
"        {\n"
"            color: #b1b1b1;\n"
"            background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"            border-width: 1px;\n"
"            border-color: #1e1e1e;\n"
"            border-style: solid;\n"
"            border-radius: 10;\n"
"            padding: 3px;\n"
"            padding-left: 5px;\n"
"            padding-right: 5px;\n"
"        }\n"
"        \n"
"        QPushButton:pressed\n"
"        {\n"
"            background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"        }\n"
"        \n"
"        QPushButton:hover\n"
"        {\n"
"            border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"        }\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(140, 330, 161, 31))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255,0);\n"
"font: 75 14pt \"Moon\";")
        self.label_3.setObjectName("label_3")
        self.checkBox = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox.setGeometry(QtCore.QRect(90, 270, 261, 41))
        self.checkBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox.setStyleSheet("QCheckBox {\n"
"color: rgb(0, 0, 0) ;\n"
"font: 75 14pt \"Moon\";\n"
"background-color: rgb(255, 255, 255,0.2);\n"
"border-radius : 20px ;\n"
"padding-right : 3px ;\n"
"}\n"
"        \n"
"QCheckBox:hover {\n"
"            border-style:solid;\n"
"            padding-left: 2px;\n"
"            padding-right: 5px;\n"
"            padding-bottom: 2px;\n"
"            padding-top: 2px;\n"
"            border-width:2px;\n"
"         /*   border-color: transparent; */\n"
"border-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"        }\n"
"QCheckBox::indicator:checked {\n"
"            image: url(/usr/share/icons/Adwaita/16x16/actions/object-select-symbolic.symbolic.png);\n"
"            height: 15px;\n"
"            width: 15px;\n"
"            border-style:solid;\n"
"            border-width: 1px;\n"
"            border-color: #48a5fd;\n"
"            color: #ffffff;\n"
"            border-radius: 3px;\n"
"            background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #48a5fd, stop:0.5 #329cfb, stop:1 #48a5fd);\n"
"        }\n"
"QCheckBox::indicator:unchecked {\n"
"            height: 15px;\n"
"            width: 15px;\n"
"            border-style:solid;\n"
"            border-width: 1px;\n"
"            border-color: #48a5fd;\n"
"            border-radius: 3px;\n"
"            background-color: #fbfdfa;\n"
"        }")
        self.checkBox.setObjectName("checkBox")
        self.label_10 = QtWidgets.QLabel(self.frame_3)
        self.label_10.setGeometry(QtCore.QRect(90, 400, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Moon")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("font: 75 14pt \"Moon\";")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame_3)
        self.label_11.setGeometry(QtCore.QRect(90, 460, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Moon")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("font: 75 14pt \"Moon\";")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame_3)
        self.label_12.setGeometry(QtCore.QRect(220, 400, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Moon")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("font: 75 14pt \"Moon\";")
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frame_3)
        self.label_13.setGeometry(QtCore.QRect(220, 460, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Moon")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("font: 75 14pt \"Moon\";")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_3.addWidget(self.frame_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.frame)
        self.frame_11 = QtWidgets.QFrame(self.centralwidget)
        self.frame_11.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_11.setStyleSheet("background-color: rgb(255, 255, 255,0);\n"
"padding-left : 20px ;\n"
"padding-right: 20px ;")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.progressBar = QtWidgets.QProgressBar(self.frame_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Moon")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet("QProgressBar{\n"
"background-color: rgb(59, 59, 152);\n"
"color: rgb(255, 0, 0);\n"
"text-align : center ;\n"
"border-color: rgb(255, 0, 255);\n"
"padding-left : 0px ;\n"
"padding-right : 0px ;\n"
"border-style: solid;\n"
"border-radius: 15px ;}\n"
"\n"
"QProgressBar::chunk {\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.438, x2:1, y2:0.523, stop:0 rgba(190, 50, 94, 255), stop:1 rgba(255, 85, 255, 255));\n"
"border-style: solid;\n"
"border-radius: 15px ;\n"
"\n"
"}\n"
"\n"
"")
        self.progressBar.setMaximum(100)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_2.addWidget(self.progressBar)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.frame_11)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255,0.2);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.pushButton.setBaseSize(QtCore.QSize(0, 0))
        self.pushButton.setTabletTracking(False)
        self.pushButton.setStyleSheet("        QPushButton\n"
"        {\n"
"            color: #b1b1b1;\n"
"            background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"            border-width: 1px;\n"
"            border-color: #1e1e1e;\n"
"            border-style: solid;\n"
"            border-radius: 10;\n"
"            padding: 3px;\n"
"            padding-left: 5px;\n"
"            padding-right: 5px;\n"
"    font: 75 14pt \"Moon\";\n"
"        }\n"
"        \n"
"        QPushButton:pressed\n"
"        {\n"
"            background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"        }\n"
"        \n"
"        QPushButton:hover\n"
"        {\n"
"            border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"        }\n"
"")
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setAutoExclusive(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.comboBox_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "Rocket Downloader"))
        self.label_8.setText(_translate("MainWindow", "YT & FB "))
        self.label.setText(_translate("MainWindow", "Enter Link"))
        self.label_2.setText(_translate("MainWindow", ">>"))
        self.label_5.setText(_translate("MainWindow", "Video Quality"))
        self.label_6.setText(_translate("MainWindow", ">>"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "360p"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "720p"))
        self.label_7.setText(_translate("MainWindow", "Save As"))
        self.label_9.setText(_translate("MainWindow", ">>"))
        self.pushButton_2.setText(_translate("MainWindow", "Browse"))
        self.label_3.setText(_translate("MainWindow", ".mp3 extension"))
        self.checkBox.setText(_translate("MainWindow", "Download As Audio "))
        self.label_10.setText(_translate("MainWindow", "Video Title : "))
        self.label_11.setText(_translate("MainWindow", "Video Size :"))
        self.pushButton.setText(_translate("MainWindow", "Download"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

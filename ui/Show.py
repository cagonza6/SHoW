# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/Show.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(950, 925)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(800, 600))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.ClockLCD = QtGui.QLCDNumber(self.centralwidget)
        self.ClockLCD.setMinimumSize(QtCore.QSize(0, 75))
        self.ClockLCD.setStyleSheet(_fromUtf8(""))
        self.ClockLCD.setSmallDecimalPoint(False)
        self.ClockLCD.setSegmentStyle(QtGui.QLCDNumber.Filled)
        self.ClockLCD.setObjectName(_fromUtf8("ClockLCD"))
        self.verticalLayout.addWidget(self.ClockLCD)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.p1_name = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p1_name.sizePolicy().hasHeightForWidth())
        self.p1_name.setSizePolicy(sizePolicy)
        self.p1_name.setMaximumSize(QtCore.QSize(500, 500))
        self.p1_name.setStyleSheet(_fromUtf8(""))
        self.p1_name.setText(_fromUtf8(""))
        self.p1_name.setPixmap(QtGui.QPixmap(_fromUtf8(":/people/user_1.jpg")))
        self.p1_name.setAlignment(QtCore.Qt.AlignCenter)
        self.p1_name.setObjectName(_fromUtf8("p1_name"))
        self.horizontalLayout_3.addWidget(self.p1_name)
        self.p2_name = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p2_name.sizePolicy().hasHeightForWidth())
        self.p2_name.setSizePolicy(sizePolicy)
        self.p2_name.setMaximumSize(QtCore.QSize(500, 500))
        self.p2_name.setText(_fromUtf8(""))
        self.p2_name.setPixmap(QtGui.QPixmap(_fromUtf8(":/people/user_2.jpg")))
        self.p2_name.setAlignment(QtCore.Qt.AlignCenter)
        self.p2_name.setObjectName(_fromUtf8("p2_name"))
        self.horizontalLayout_3.addWidget(self.p2_name)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.ClockP1 = QtGui.QLCDNumber(self.centralwidget)
        self.ClockP1.setMinimumSize(QtCore.QSize(0, 75))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ClockP1.setFont(font)
        self.ClockP1.setObjectName(_fromUtf8("ClockP1"))
        self.horizontalLayout.addWidget(self.ClockP1)
        self.ClockP2 = QtGui.QLCDNumber(self.centralwidget)
        self.ClockP2.setMinimumSize(QtCore.QSize(0, 100))
        self.ClockP2.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ClockP2.setFont(font)
        self.ClockP2.setObjectName(_fromUtf8("ClockP2"))
        self.horizontalLayout.addWidget(self.ClockP2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.btnStop = QtGui.QPushButton(self.centralwidget)
        self.btnStop.setObjectName(_fromUtf8("btnStop"))
        self.horizontalLayout_5.addWidget(self.btnStop)
        self.btnReset = QtGui.QPushButton(self.centralwidget)
        self.btnReset.setObjectName(_fromUtf8("btnReset"))
        self.horizontalLayout_5.addWidget(self.btnReset)
        self.btnStart = QtGui.QPushButton(self.centralwidget)
        self.btnStart.setObjectName(_fromUtf8("btnStart"))
        self.horizontalLayout_5.addWidget(self.btnStart)
        self.btnOpening = QtGui.QPushButton(self.centralwidget)
        self.btnOpening.setObjectName(_fromUtf8("btnOpening"))
        self.horizontalLayout_5.addWidget(self.btnOpening)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.GroupboxTests = QtGui.QGroupBox(self.centralwidget)
        self.GroupboxTests.setObjectName(_fromUtf8("GroupboxTests"))
        self.gridLayout = QtGui.QGridLayout(self.GroupboxTests)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.btnStopP1 = QtGui.QPushButton(self.GroupboxTests)
        self.btnStopP1.setObjectName(_fromUtf8("btnStopP1"))
        self.gridLayout.addWidget(self.btnStopP1, 0, 0, 1, 1)
        self.btnStopP2 = QtGui.QPushButton(self.GroupboxTests)
        self.btnStopP2.setObjectName(_fromUtf8("btnStopP2"))
        self.gridLayout.addWidget(self.btnStopP2, 0, 2, 1, 1)
        self.btnPointP1 = QtGui.QPushButton(self.GroupboxTests)
        self.btnPointP1.setObjectName(_fromUtf8("btnPointP1"))
        self.gridLayout.addWidget(self.btnPointP1, 1, 0, 1, 1)
        self.btnPointP2 = QtGui.QPushButton(self.GroupboxTests)
        self.btnPointP2.setObjectName(_fromUtf8("btnPointP2"))
        self.gridLayout.addWidget(self.btnPointP2, 1, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.GroupboxTests)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 950, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Simple Hotwire", None))
        self.label_2.setText(_translate("MainWindow", "Elapsed Time", None))
        self.label.setText(_translate("MainWindow", "Individual time", None))
        self.btnStop.setText(_translate("MainWindow", "Stop", None))
        self.btnReset.setText(_translate("MainWindow", "Reset", None))
        self.btnStart.setText(_translate("MainWindow", "Start", None))
        self.btnOpening.setText(_translate("MainWindow", "Opening", None))
        self.GroupboxTests.setTitle(_translate("MainWindow", "Tests", None))
        self.btnStopP1.setText(_translate("MainWindow", "Stop P1", None))
        self.btnStopP2.setText(_translate("MainWindow", "Stop P2", None))
        self.btnPointP1.setText(_translate("MainWindow", "Point P1", None))
        self.btnPointP2.setText(_translate("MainWindow", "Point P2", None))

import imgs_rc
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.output.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 480)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.searchField = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchField.sizePolicy().hasHeightForWidth())
        self.searchField.setSizePolicy(sizePolicy)
        self.searchField.setText("")
        self.searchField.setObjectName("searchField")
        self.gridLayout.addWidget(self.searchField, 0, 8, 1, 1)
        self.homeButton = QtWidgets.QPushButton(Form)
        self.homeButton.setObjectName("homeButton")
        self.gridLayout.addWidget(self.homeButton, 0, 9, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.webView = QtWebKitWidgets.QWebView(Form)
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")
        self.gridLayout.addWidget(self.webView, 4, 0, 1, 10)
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 3, 0, 1, 10)
        self.Back = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Back.sizePolicy().hasHeightForWidth())
        self.Back.setSizePolicy(sizePolicy)
        self.Back.setMinimumSize(QtCore.QSize(0, 0))
        self.Back.setObjectName("Back")
        self.gridLayout.addWidget(self.Back, 0, 3, 1, 1)
        self.loadingButton = QtWidgets.QPushButton(Form)
        self.loadingButton.setObjectName("loadingButton")
        self.gridLayout.addWidget(self.loadingButton, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 2, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Python Web"))
        self.searchField.setPlaceholderText(_translate("Form", "Search"))
        self.homeButton.setText(_translate("Form", "Home"))
        self.Back.setText(_translate("Form", "Back"))
        self.loadingButton.setText(_translate("Form", "PushButton"))
        self.pushButton.setText(_translate("Form", "Go"))

from PyQt5 import QtWebKitWidgets

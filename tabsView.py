# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tabsView.ui'
#
# Created: Tue Dec 27 12:06:04 2016
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PythonWebBrowser(object):
    def setupUi(self, PythonWebBrowser):
        PythonWebBrowser.setObjectName("PythonWebBrowser")
        PythonWebBrowser.resize(640, 480)
        self.tabWidget = QtWidgets.QTabWidget(PythonWebBrowser)
        self.tabWidget.setGeometry(QtCore.QRect(0, 70, 641, 411))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWeb1 = QtWebKitWidgets.QWebView(self.tab)
        self.tabWeb1.setGeometry(QtCore.QRect(0, 0, 631, 371))
        self.tabWeb1.setProperty("url", QtCore.QUrl("about:blank"))
        self.tabWeb1.setObjectName("tabWeb1")
        self.tabWidget.addTab(self.tab, "")
        self.urlInput = QtWidgets.QLineEdit(PythonWebBrowser)
        self.urlInput.setGeometry(QtCore.QRect(0, 10, 231, 33))
        self.urlInput.setObjectName("urlInput")
        self.goBtn = QtWidgets.QPushButton(PythonWebBrowser)
        self.goBtn.setGeometry(QtCore.QRect(230, 10, 41, 31))
        self.goBtn.setObjectName("goBtn")
        self.reloadBtn = QtWidgets.QPushButton(PythonWebBrowser)
        self.reloadBtn.setGeometry(QtCore.QRect(270, 10, 101, 31))
        self.reloadBtn.setObjectName("reloadBtn")
        self.backBtn = QtWidgets.QPushButton(PythonWebBrowser)
        self.backBtn.setGeometry(QtCore.QRect(370, 10, 101, 31))
        self.backBtn.setObjectName("backBtn")
        self.searchInput = QtWidgets.QLineEdit(PythonWebBrowser)
        self.searchInput.setGeometry(QtCore.QRect(470, 10, 111, 33))
        self.searchInput.setObjectName("searchInput")
        self.homeBtn = QtWidgets.QPushButton(PythonWebBrowser)
        self.homeBtn.setGeometry(QtCore.QRect(580, 10, 61, 31))
        self.homeBtn.setObjectName("homeBtn")
        self.newTabBtn = QtWidgets.QPushButton(PythonWebBrowser)
        self.newTabBtn.setGeometry(QtCore.QRect(0, 40, 101, 31))
        self.newTabBtn.setObjectName("newTabBtn")
        self.deleteTabBtn = QtWidgets.QPushButton(PythonWebBrowser)
        self.deleteTabBtn.setGeometry(QtCore.QRect(100, 40, 101, 31))
        self.deleteTabBtn.setObjectName("deleteTabBtn")
        self.loadingBar = QtWidgets.QProgressBar(PythonWebBrowser)
        self.loadingBar.setGeometry(QtCore.QRect(200, 40, 441, 31))
        self.loadingBar.setProperty("value", 24)
        self.loadingBar.setObjectName("loadingBar")

        self.retranslateUi(PythonWebBrowser)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(PythonWebBrowser)

    def retranslateUi(self, PythonWebBrowser):
        _translate = QtCore.QCoreApplication.translate
        PythonWebBrowser.setWindowTitle(_translate("PythonWebBrowser", "PythonWebBrowser"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("PythonWebBrowser", "Tab 1"))
        self.goBtn.setText(_translate("PythonWebBrowser", "Go"))
        self.reloadBtn.setText(_translate("PythonWebBrowser", "Reload"))
        self.backBtn.setText(_translate("PythonWebBrowser", "Back"))
        self.searchInput.setPlaceholderText(_translate("PythonWebBrowser", "Search"))
        self.homeBtn.setText(_translate("PythonWebBrowser", "Home"))
        self.newTabBtn.setText(_translate("PythonWebBrowser", "New Tab"))
        self.deleteTabBtn.setText(_translate("PythonWebBrowser", "Delete Tab"))

from PyQt5 import QtWebKitWidgets

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebKitWidgets import QWebView, QWebPage
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest
from PyQt5.QtWebKit import QWebSettings
from tabsView import Ui_PythonWebBrowser
import sqlite3
import sys,os,socket,time,getpass

class tabs(object):
  def tab(self):
    self.webView(
  
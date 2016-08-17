from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
#from PyQt5.QtWebEngineCore import *
from PyQt5.QtWebEngineWidgets import *
import sys

app = QApplication(sys.argv)

view = QWebEngineView();
view.setUrl(QUrl("http://useragentstring.com"))
view.setUrl(QUrl("http://html5test.com"))
view.resize(1280,720)
view.show()

app.exec_()
sys.exit(0)



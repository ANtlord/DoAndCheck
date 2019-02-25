#!/usr/bin/env python
import sys
#  from PyQt5 import QtQuick
#  from PyQt5.QtGui import QGuiApplication
#  from PyQt5.QtQml import QQmlApplicationEngine

from PySide2.QtWidgets import QApplication
from PySide2.QtQuick import QQuickView
from PySide2 import QtQuick
from PySide2.QtCore import QUrl
from PySide2.QtQml import QQmlApplicationEngine

def main():
    #  QtQuick.QQuickWindow.setSceneGraphBackend(QtQuick.QSGRendererInterface.Software)
    #  app = QGuiApplication(sys.argv)
    #  engine = QQmlApplicationEngine()
    #  engine.load('qml/main.qml')
    #  engine.quit.connect(app.quit)
    #  sys.exit(app.exec_())

    app = QApplication(sys.argv)
    #  view = QQuickView()
    engine = QQmlApplicationEngine()
    engine.load('qml/main.qml')
    engine.quit.connect(app.quit)

    #  view.setSource(url)
    #  view.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

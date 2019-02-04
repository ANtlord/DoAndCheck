#!/usr/bin/env python
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from typing import Callable


def build_list_item() -> QtWidgets.QListWidgetItem:
    """Create an item for a check list."""
    item = QtWidgets.QListWidgetItem()
    font = QtGui.QFont()
    font.setStrikeOut(False)
    item.setFont(font)
    brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
    brush.setStyle(QtCore.Qt.NoBrush)
    item.setForeground(brush)
    item.setFlags(
        QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled |
        QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled
    )
    return item


def _build_btn(
    name: str, callback: Callable, layout: QtWidgets.QHBoxLayout, form,
) -> QtWidgets.QPushButton:
    button = QtWidgets.QPushButton(form)
    button.clicked.connect(callback)
    button.setObjectName(name)
    layout.addWidget(button)
    return button


class Widget(QtWidgets.QWidget):
    def closeEvent(self, event):
        super().closeEvent(event)
        self.hide()


class SystemTrayIcon(QtWidgets.QSystemTrayIcon):
    def __init__(self, icon, parent: Widget):
        super().__init__(icon, parent)
        self.activated.connect(self.toggle_hidden)
        self.flag = False
        self.setToolTip("Do And Check")

    def toggle_hidden(self):
        widget = self.parent()
        if widget.isVisible():
            self.parent().hide()
        else:
            self.parent().show()
            self.parent().activateWindow()


class Ui_Form(object):
    def setupUi(self, Form: Widget):
        Form.setObjectName("Form")
        Form.resize(540, 313)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon_32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)

        self.verticalLayout.addWidget(self.listWidget)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.buttons_layout = QtWidgets.QHBoxLayout()
        self.buttons_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.buttons_layout.setObjectName("buttons_layout")
        self.init_buttons(self.buttons_layout, Form)
        self.verticalLayout_2.addLayout(self.buttons_layout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.listWidget.clicked.connect(self.check_item)
        self.init_shortcuts()

    def init_shortcuts(self):
        """Initialization of shortcuts.

        Available shortcuts:
            * Del - delete current check list item.
            * Shift + Enter (Shift + Retrurn) - add an item.
            * F2 - rename selected item.
            * Shift + Up / Shift + Down - move selected item.
            * Space - check selected item.
        """
        shortcuts = {
            'Del': self.remove,
            'Shift+Return': self.add,
            'Space': self.check_item,
            'F2': self.change,
            'Shift+Up': self.move_item_up,
            'Shift+Down': self.move_item_down,
            'Ctrl+Q': QtWidgets.qApp.quit,
        }
        for key, callback in shortcuts.items():
            list_widget_shortcut = QtWidgets.QShortcut(QtGui.QKeySequence(key), self.listWidget)
            list_widget_shortcut.activated.connect(callback)

    def _move_current_item(self, stop_row, new_row_func: Callable[[int], int]):
        row = self.listWidget.currentRow()
        if row == stop_row:
            return
        item = self.listWidget.takeItem(row)
        self.listWidget.insertItem(new_row_func(row), item)
        self.listWidget.setCurrentRow(new_row_func(row))

    def move_item_up(self):
        """Move current item to up by one position."""
        self._move_current_item(0, lambda x: x - 1)

    def move_item_down(self):
        """Move current item to down by one position."""
        last_index = self.listWidget.count() - 1
        self._move_current_item(last_index, lambda x: x + 1)

    def init_buttons(self, layout: QtWidgets.QHBoxLayout, form):
        """Initialization of buttons.

        Buttons:
            * self.add_btn - button to add an item.
            * self.change_btn - button to change a text of current item.
            * self.delete_btn - button to delete current item.
            * self.clear - button to remove all items.
        """
        self.add_btn = _build_btn('add_btn', self.add, layout, form)
        self.change_btn = _build_btn("change_btn", self.change, layout, form)
        self.delete_btn = _build_btn("delete_btn", self.remove, layout, form)
        self.clear_btn = _build_btn("clear_btn", self.clear, layout, form)

    def _start_current_item_edition(self):
        """Adds a flag provides an editing to current item and start editing of the item."""
        item = self.listWidget.currentItem()
        flags = item.flags()
        item.setFlags(flags | QtCore.Qt.ItemIsEditable)
        self.listWidget.editItem(item)
        item.setFlags(flags)

    def change(self):
        """Change current item."""
        self._start_current_item_edition()

    def add(self):
        """Add an item."""
        item = build_list_item()
        self.listWidget.addItem(item)
        self.listWidget.setCurrentItem(item)
        self._start_current_item_edition()

    def remove(self):
        """Remove current item."""
        self.listWidget.takeItem(self.listWidget.currentRow())

    def check_item(self):
        """Check current item."""
        item = self.listWidget.currentItem()
        font = QtGui.QFont()
        font.setStrikeOut(not item.font().strikeOut())
        item.setFont(font)

    def clear(self):
        """Remove all items."""
        self.listWidget.clear()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Do And Check"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.add_btn.setText(_translate("Form", "Add"))
        self.change_btn.setText(_translate("Form", "Change"))
        self.delete_btn.setText(_translate("Form", "Delete"))
        self.clear_btn.setText(_translate("Form", "Clear"))


def main():
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.load('qml/qml.qml')
    engine.quit.connect(app.quit)
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

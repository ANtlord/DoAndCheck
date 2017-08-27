#!/usr/bin/env python
import sys
from PyQt5 import QtCore, QtGui, QtWidgets


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


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(540, 313)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon_16.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setObjectName("listWidget")

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
        self.clear_btn.clicked.connect(self.clear)
        self.change_btn.clicked.connect(self.change)
        self.init_shortcuts()

    def init_shortcuts(self):
        """Initialization of shortcuts.

        Available shortcuts:
            * Del - delete current check list item.
            * Shift + Enter (Shift + Retrurn) - add an item.
        """
        list_widget_shortcut = QtWidgets.QShortcut(QtGui.QKeySequence('Del'), self.listWidget)
        list_widget_shortcut.activated.connect(self.remove)
        list_widget_shortcut = QtWidgets.QShortcut(
            QtGui.QKeySequence('Shift+Return'), self.listWidget
        )
        list_widget_shortcut.activated.connect(self.add)
        list_widget_shortcut = QtWidgets.QShortcut(QtGui.QKeySequence('Space'), self.listWidget)
        list_widget_shortcut.activated.connect(self.check_item)

    def init_buttons(self, layout: QtWidgets.QHBoxLayout, Form):
        """Initialization of buttons.

        Buttons:
            * self.add_btn - button to add an item.
            * self.change_btn - button to change a text of current item.
            * self.delete_btn - button to delete current item.
            * self.clear - button to remove all items.
        """
        self.add_btn = QtWidgets.QPushButton(Form)
        self.add_btn.clicked.connect(self.add)
        self.add_btn.setObjectName("add_btn")
        layout.addWidget(self.add_btn)
        self.change_btn = QtWidgets.QPushButton(Form)
        self.change_btn.setObjectName("change_btn")
        layout.addWidget(self.change_btn)
        self.delete_btn = QtWidgets.QPushButton(Form)
        self.delete_btn.setObjectName("delete_btn")
        self.delete_btn.clicked.connect(self.remove)
        layout.addWidget(self.delete_btn)
        self.clear_btn = QtWidgets.QPushButton(Form)
        self.clear_btn.setStyleSheet("")
        self.clear_btn.setObjectName("clear_btn")
        layout.addWidget(self.clear_btn)

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
        Form.setWindowTitle(_translate("Form", "Form"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.add_btn.setText(_translate("Form", "Add"))
        self.change_btn.setText(_translate("Form", "Change"))
        self.delete_btn.setText(_translate("Form", "Delete"))
        self.clear_btn.setText(_translate("Form", "Clear"))


def main():
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

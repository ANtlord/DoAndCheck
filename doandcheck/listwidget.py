import logging

from typing import NamedTuple
from PyQt5 import QtCore, QtWidgets, QtGui


logger = logging.getLogger()


class Task(NamedTuple):
    is_checked: bool
    caption: str


class TaskModel(QtCore.QAbstractListModel):
    def __init__(self, data, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._data = data

    def insertRows(self, row: int, count: int, index: QtCore.QModelIndex = None):
        if index is None:
            index = QtCore.QModelIndex()
        self.beginInsertRows(index, row, row + count - 1)
        new_data = [Task(False, '')] * count
        self._data = self._data[:row] + new_data + self._data[row:]
        self.endInsertRows()
        logger.debug('data after inserting `%s`', self._data)
        return True

    def removeRows(self, row: int, count: int, parent: QtCore.QModelIndex = None):
        if parent is None:
            parent = QtCore.QModelIndex()
        if not parent.isValid():
            logger.debug('removeRows: parent is not valid')
            return False

        self.beginRemoveRows(parent, row, row + count - 1)
        del self._data[row:row + count]
        self.endRemoveRows()
        logger.debug('data after removing `%s`', self._data)
        return True

    def rowCount(self, index: QtCore.QModelIndex = None):
        return len(self._data)

    def data(self, index: QtCore.QModelIndex, role: int = QtCore.Qt.DisplayRole):
        if role in (QtCore.Qt.DisplayRole, QtCore.Qt.EditRole):
            return self._data[index.row()].caption
        elif role == QtCore.Qt.FontRole:
            font = QtGui.QFont()
            val = self._data[index.row()].is_checked
            font.setStrikeOut(val)
            return font
        return None

    def get_task(self, row) -> Task:
        return self._data[row]

    def setData(self, index: QtCore.QModelIndex, value, role = QtCore.Qt.EditRole):
        if not index.isValid():
            logger.debug('setData: it is not valid')
            return False
        value_type = type(value)
        if value_type == str:
            task: Task = self._data[index.row()]
            self._data[index.row()] = Task(caption=value, is_checked=task.is_checked)
        elif value_type == Task:
            self._data[index.row()] = value
        self.dataChanged.emit(index, index, [0, 2])
        logger.debug('data after setting `%s`', self._data)
        return True
    
    def flags(self, index: QtCore.QModelIndex):
        flags = super().flags(index)
        if index.isValid():
            return QtCore.Qt.ItemIsEditable | flags
        return flags


class ListWidgetItem(QtWidgets.QListWidgetItem):
    def event(self, event: QtCore.QEvent):
        logger.debug(self.__class__, event.type())
        return super().event(event)

    def keyPressEvent(self, event: QtGui.QKeyEvent):
        logger.debug(self.__class__, 'keyPressEvent')
        return super().keyPressEvent(event)


class ListWidget(QtWidgets.QListView):
    def add(self):
        model: TaskModel = self.model()
        #  logger.debug('row count before add', model.rowCount())
        #  index = model.index(model.rowCount() - 1)
        model.insertRows(model.rowCount(), 1, None)
        #  logger.debug('row count after add', model.rowCount())

    def count(self):
        return self.model().rowCount()

    def takeItem(self, row: int) -> Task:
        model: TaskModel = self.model()
        index = model.index(row, 0)
        data = model._data[row]
        logger.debug('Remove row %s', index.row())
        res = model.removeRow(index.row(), index)

        if row > self.count() - 1:
            self.setCurrentIndex(model.index(self.count() - 1))
        return data

    def insertItem(self, row: int, value: str):
        model: TaskModel = self.model()
        model.insertRows(row, 1, model.index(min(row, self.count() - 1), 0))
        index = model.index(row, 0)
        model.setData(index, value)
        logger.debug('after set data `%s`', model.data(index))

    def setCurrentRow(self, row: int):
        model: TaskModel = self.model()
        index = model.index(row, 0)
        self.setCurrentIndex(index)

    def currentRow(self):
        return self.currentIndex().row()

    def clear(self):
        model = self.model()
        index = self.currentIndex()
        model.removeRows(0, self.count(), index)


class LineEdit(QtWidgets.QLineEdit):
    def keyPressEvent(self, event: QtGui.QKeyEvent):
        if event.key() not in (QtCore.Qt.Key_Up, QtCore.Qt.Key_Down, QtCore.Qt.Key_Tab, QtCore.Qt.Key_Tab):
            super().keyPressEvent(event)


class TaskDelegate(QtWidgets.QStyledItemDelegate):
    def __init__(self, mainWindow, *args, **kwargs):
        self._mainWindow = mainWindow 
        super().__init__(*args, **kwargs)

    def setEditorData(self, editor: QtWidgets.QWidget, index: QtCore.QModelIndex):
        text = index.model().data(index, QtCore.Qt.DisplayRole)
        editor.setText(text)

    def createEditor(self, parent, option, index):
        lineEdit = LineEdit(parent)
        shortcut = QtWidgets.QShortcut(QtGui.QKeySequence('Shift+Tab'), lineEdit)
        shortcut.activated.connect(lambda: None)
        self._mainWindow.itemLineEdit = lineEdit
        return lineEdit

from typing import NamedTuple
from PyQt5 import QtCore, QtWidgets, QtGui


#  class ListWidget(QtWidgets.QListWidget):
    #  pass


class Task(NamedTuple):
    is_checked: bool
    caption: str


class TaskModel(QtCore.QAbstractListModel):
    def __init__(self, data, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._data = data

    def insertRows(self, row: int, count: int, index: QtCore.QModelIndex):
        if not index.isValid():
            print('it is not valid')
            return False

        self.beginInsertRows(index, row, row + count - 1)
        new_data = [None] * count
        for _ in range(row + 1):
            self._data = self._data[:row] + new_data + self._data[row:]
        self.endInsertRows()
        return True

    def rowCount(self, index: QtCore.QModelIndex = None):
        return len(self._data)

    def data(self, index: QtCore.QModelIndex, role: int):
        if role == QtCore.Qt.DisplayRole:
            return self._data[index.row()]
        return None

    def setData(self, index: QtCore.QModelIndex, value):
        if not index.isValid():
            print('it is not valid')
            return False
        self._data[index.row()] = value
        self.dataChanged.emit(index, index, [0, 2])
        return True
    
    def flags(self, index: QtCore.QModelIndex):
        flags = super().flags(index)
        if index.isValid():
            return QtCore.Qt.ItemIsEditable | flags
        return flags


class ListWidgetItem(QtWidgets.QListWidgetItem):
    def event(self, event: QtCore.QEvent):
        print(self.__class__, event.type())
        return super().event(event)

    def keyPressEvent(self, event: QtGui.QKeyEvent):
        print(self.__class__, 'keyPressEvent')
        return super().keyPressEvent(event)


class ListWidget(QtWidgets.QListWidget):
    def event(self, event: QtCore.QEvent):
        if event.type() == QtCore.QEvent.KeyRelease and not self.parentWidget().is_idle():
            ch = self.children()
            for c in ch:
                print('---->', type(c))
            print(self.__class__, event.type())
            event.accept()
            return False
        return super().event(event)

    #  def dataChanged(self, top: QtCore.QModelIndex, bottom: QtCore.QModelIndex, *args, **kwargs):
        #  print('dataChanged', top.row(), bottom.row(), args, kwargs)
        #  return super().dataChanged(top, bottom, *args, **kwargs)

    #  def setData(self, *args, **kwargs):
        #  print('setData')
        #  return False
        #  print('focusOutEvent', args)
        #  return super().focusOutEvent(*args, **kwargs)
    #  def __init__(self, *args, **kwargs):
        #  super().__init__(*args, **kwargs)


class TaskDelegate(QtWidgets.QStyledItemDelegate):
    def paint(self, painter: QtGui.QPainter, option: QtWidgets.QStyleOptionViewItem, index: QtCore.QModelIndex):
        pass
    #  def createEditor(self, parent, *args, **kwargs):
        #  return QtWidgets.QLineEdit(parent)
        #  return None
        #  ret = super().createEditor(*args, **kwargs)
        #  print(args, kwargs, ret)
        #  return ret

    #  def editorEvent(self, *args, **kwargs):
        #  print('editorEvent')
        #  return False

    #  def destroyEditor(self, *args, **kwargs):
        #  print('destroyEditor')
        #  return None
        #  ret = super().destroyEditor(*args, **kwargs)
        #  print(args, kwargs, ret)
        #  return ret

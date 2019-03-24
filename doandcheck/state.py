from PyQt5 import QtCore

class Base:
    __slots__ = '_state', '_widget',

    def __init__(self, widget):
        widget._state = self
        self._widget = widget

    def edit(self):
        pass

    def idle(self):
        pass

    def resume(self):
        pass

    def add(self):
        pass


class Idle(Base):
    __slots__ = tuple()

    def edit(self):
        Editing(self._widget)

    def add(self):
        #  item = build_list_item()
        self._widget.listWidget.add()
        model = self._widget.listWidget.model()
        index = model.index(self._widget.listWidget.count() - 1, 0)
        if index.row() != self._widget.listWidget.count() - 1:
            exit(1)
        self._widget.listWidget.setCurrentIndex(index)
        currentIndex = self._widget.listWidget.currentIndex()
        self.edit()


class Editing(Base):
    __slots__ = tuple()

    def __init__(self, widget):
        super().__init__(widget)
        listWidget = self._widget.listWidget
        if listWidget.count():
            index = listWidget.currentIndex()
            listWidget.openPersistentEditor(index)
            self.resume()

    def idle(self):
        listWidget = self._widget.listWidget
        index = listWidget.currentIndex()
        listWidget.closePersistentEditor(index)
        Idle(self._widget)

    def resume(self):
        self._widget.itemLineEdit.setFocus()

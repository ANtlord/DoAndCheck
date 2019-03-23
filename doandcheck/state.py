from PyQt5 import QtCore

class Base:
    __slots__ = '_state', '_widget',

    def __init__(self, widget):
        print('State is ', self.__class__)
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
        print('add')
        #  item = build_list_item()
        self._widget.listWidget.add()
        model = self._widget.listWidget.model()
        print('self._widget.listWidget.count', self._widget.listWidget.count())
        index = model.index(self._widget.listWidget.count() - 1, 0)
        if index.row() != self._widget.listWidget.count() - 1:
            print('index.isValid()', index.isValid(), 'row', index.row())
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
            #  listWidget.editItem(listWidget.currentItem())
            #  model: TaskModel = listWidget.model()
            index = listWidget.currentIndex()
            print('edit row', index.row())
            listWidget.openPersistentEditor(index)
            self.resume()

    def idle(self):
        listWidget = self._widget.listWidget
        model: TaskModel = listWidget.model()
        index = model.index(model.rowCount() - 1)
        listWidget.closePersistentEditor(index)
        Idle(self._widget)

    def resume(self):
        self._widget.itemLineEdit.setFocus()

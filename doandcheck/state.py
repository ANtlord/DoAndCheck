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


class Idle(Base):
    __slots__ = tuple()

    def edit(self):
        Editing(self._widget)


class Editing(Base):
    __slots__ = tuple()

    def __init__(self, widget):
        super().__init__(widget)
        self.resume()

    def idle(self):
        listWidget = self._widget.listWidget
        listWidget.closePersistentEditor(listWidget.currentItem())
        Idle(self._widget)

    def resume(self):
        listWidget = self._widget.listWidget
        if listWidget.count():
            #  listWidget.editItem(listWidget.currentItem())
            listWidget.openPersistentEditor(listWidget.currentItem())

# Desktop GUI crossplatoform development.

So I deciede to make a proof of possibility of crossplatform development without ElectronJS.
I tried to make it on Qt but then I picked QML due to its possibility to make more flexible
interface. As far as I got there is no possibility to make a button with red triangles using native
widgets. So let's work with QML. As I am not C++ master I choose my favorite script language Python.
There is a good bindings and I chose PyQt.

The first problem I encountered is flickering on resizing the applicaion's window. There are no
relevant information on Google. My Qt version is 5.11 but responses on the internet are about 5.9.
Let's try to mix the responses.

To be honest I'm not so good at QML and I need an IDE. Due to there is no IDE for QML project on
Python, I downloaded QtCreator and created a QML sample.

So I've found an advice to set software renderer interface to scene graph backend. As far as I know
hardware renderer is better than Software but it solves the flickering. I hope there is no lags in
the future. So the solution is 

```python
from PyQt5 import QtQuick
QtQuick.QQuickWindow.setSceneGraphBackend(QtQuick.QSGRendererInterface.Software)
```

I encountered issues related to features of layouts. I picked Row and Column objects to split the
windows onto base areas. I set ListView object and buttons in the layouts and I got a couple of
errors. All of them were about wrong usage of `anchors.*` properties. The error is
```
QML ListView: Detected anchors on an item that is managed by a layout. This is undefined behavior;
use Layout.alignment instead.
```
So I fixed it by moving my layouts in Item objects. That's it!


Now the list is ready and buttons are shown. So I need to make some work on keyboard shortcuts.
Where should I go? I need to get this done with QML or Python. I hope Python.

OMG There is a segfault on quit. QPixmap: Must construct a QGuiApplication before a QPixmap. So ok.
It's not the first segfault in my life. Even with Python. Let's go Google.

As usual Google doesn't help. I tried to use PySide2 instead of PyQt5. So it avoids the segfault but
flickering returns. I can't fix it using PySide because the Qt binding doesn't have QSGRendererInterface.
Checkout the [link](https://wiki.qt.io/Qt_for_Python_Missing_Bindings). Reading that I assume that
PyQt covers Qt API better that PySide2 regardless the fact that PySide2 is official.

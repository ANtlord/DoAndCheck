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

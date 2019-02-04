import QtQuick 2.11
import QtQuick.Window 2.11
import QtQuick.Controls 2.3

Window {
    id: window
    visible: true
    width: 640
    height: 480
    title: qsTr("Hello World")

    Column {
        id: column
        x: 0
        y: 0
        width: 640
        height: 480
    }

    Row {
        id: row
        y: 385
        height: 95
        anchors.right: parent.right
        anchors.rightMargin: 0
        anchors.left: parent.left
        anchors.leftMargin: 0
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 0
    }

    Button {
        id: button
        y: 413
        text: qsTr("Button")
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 27
        anchors.left: parent.left
        anchors.leftMargin: 16
    }

    Button {
        id: button1
        x: 518
        y: 413
        text: qsTr("Button")
        anchors.right: parent.right
        anchors.rightMargin: 22
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 27
    }
}

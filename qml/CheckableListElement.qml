import QtQuick 2.11

Item {
    x: 5
    width: 80
    height: 40
    Row {
        id: row2
        Rectangle {
            width: 40
            height: 40
            color: colorCode
        }

        Text {
            text: name
            font.bold: true
            anchors.verticalCenter: parent.verticalCenter
        }
        spacing: 10
    }
}

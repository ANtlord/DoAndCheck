import QtQuick 2.11

Rectangle {
    id: me
    x: 5
    anchors.left: parent.left
    anchors.right: parent.right
    height: 40
    color: activeFocus ? "#ccc" : "white"

    state: (inputState ? "checked" : "unchecked")
    states: [
        State {
            name: "checked"
            PropertyChanges {
                target: square
                color: "black"
            }
            PropertyChanges {
                target: caption
                color: "gray"
                font.strikeout: true
                font.bold: false
            }
        },
        State {
            name: "unchecked"
            PropertyChanges {
                target: square
                color: "blue"
            }
        },
        State {
            name: "focused"
            PropertyChanges {
                target: me
                color: "gray"
            }
        }
    ]

    MouseArea {
        anchors.fill: parent
        onClicked: parent.state = (parent.state == "checked" ? "unchecked" : "checked")
    }

    Row {
        id: row2
        Rectangle {
            id: square
            width: 40
            height: 40
            color: colorCode
        }

        Text {
            id: caption
            text: name
            font.bold: true
            anchors.verticalCenter: parent.verticalCenter
        }
        spacing: 10
    }
}

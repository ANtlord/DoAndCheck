import QtQuick 2.11
import QtQuick.Window 2.11
import QtQuick.Controls 2.3
import QtQuick.Layouts 1.3

Window {
    id: window
    visible: true
    width: 640
    height: 480
    title: qsTr("Hello World")
    minimumWidth: 640
    minimumHeight: 480

    ColumnLayout {
        id: column
        anchors.fill: parent

//        RowLayout {
//            id: topRow

//            Item {
//                Layout.fillHeight: true
//                Layout.fillWidth: true

//                ListView {
//                    anchors.fill: parent
//                    id: checkListView
//                    interactive: true
//                    focus: true
//                    model: ListModel {
//                        ListElement {
//                            name: "Grey"
//                            colorCode: "grey"
//                            inputState: true
//                        }

//                        ListElement {
//                            name: "Red"
//                            colorCode: "red"
//                            inputState: false
//                        }

//                        ListElement {
//                            name: "Blue"
//                            colorCode: "blue"
//                            inputState: false
//                        }

//                        ListElement {
//                            name: "Green"
//                            colorCode: "green"
//                            inputState: false
//                        }
//                    }
//                    delegate: CheckableListElement{}
//                }
//            }

//        }

        Item {
            Layout.fillWidth: true
            Layout.preferredHeight: 50
            focus: false
            RowLayout {
                anchors.fill: parent
                anchors.leftMargin: spacing
                anchors.rightMargin: spacing
                id: bottomRow

                spacing: 5

                Button {
                    id: addButton
                    text: qsTr("Add")
                    Layout.fillWidth: true
                }

                Button {
                    id: changeButton
                    text: qsTr("Change")
                }

                Button {
                    id: deleteButton
                    text: qsTr("Delete")
                }

                Button {
                    id: clearButton
                    text: qsTr("Clear")
                }

            }
        }

    }
}

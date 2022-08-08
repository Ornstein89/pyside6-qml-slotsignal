import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Layouts

/*
https://stackoverflow.com/q/73218005/12691808
*/

Page{
    id: page2

    // !!! singal №3 in nested QML Object
    signal page2_signal(string input_string)

    // !!! important - this name is used
    // to access page2 from C++ or Python backend
    objectName: "page2_objname"

    Button{
        text: "Go to page 1"
        anchors.centerIn: parent
        onClicked: {
            stacklayout.currentIndex = 0
        }
    }
}

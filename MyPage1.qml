import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Layouts

/*
https://stackoverflow.com/q/73218005/12691808
*/

Page{
    id: page1

    // !!! singal №2 in nested QML Object
    signal page1_signal(string input_string)

    // !!! important - this name is used
    // to access page1 from C++ or Python backend
    objectName: "page1_objname"

    Button{
        text: "Go to page 2"
        anchors.centerIn: parent
        onClicked: {
            stacklayout.currentIndex = 1
            // call root object signal from nested object
            mainapp_signal("mainapp_signal() from page1");
            // call nested object signal from same object
            page1_signal("page1_signal() from page1");
            // call another nested object signal
            page2.page2_signal("page2_signal() from page1");
        }
    }
}

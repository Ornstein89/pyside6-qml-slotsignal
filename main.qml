import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Layouts

/*
https://stackoverflow.com/q/73218005/12691808
*/

ApplicationWindow {
    width: 480
    height: 640
    visible: true
    title: qsTr("Example for Stackoverflow")

    // !!! singal №1 in root QML Object - most easy to connect in main.py
    signal mainapp_signal(string input_string)

    StackLayout {
        id : stacklayout
        anchors.fill: parent
        MyPage1 {
            id: page1
        }
        MyPage2 {
            id: page2
        }
    }
}

# This Python file uses the following encoding: utf-8
import sys
from pathlib import Path

from PySide6.QtCore import QObject, QUrl, Slot, Signal, Qt
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

#
# for https://stackoverflow.com/a/73277234/12691808
#

class TestClass(QObject):
    '''
    Object - slot-owner and signal-acceptor
    '''
    @Slot(str)
    def test_slot1(self, input_string : str):
        print(input_string)
    @Slot(str)
    def test_slot2(self, input_string : str):
        print(input_string)
    @Slot(str)
    def test_slot3(self, input_string : str):
        print(input_string)

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    test_object = TestClass()
    qml_file = Path(__file__).resolve().parent / "main.qml"
    engine.load(qml_file)
    if not engine.rootObjects():
        sys.exit(-1)

    # !!! connect ApplicationWindow.mainapp_signal() to test_object.test_slot1
    engine.rootObjects()[0]\
        .mainapp_signal.connect(
            test_object.test_slot1,
            type=Qt.ConnectionType.QueuedConnection)

    # !!! access nested page1 from python backend
    qmlpage1 = engine.rootObjects()[0].findChild(QObject, "page1_objname")

    # !!! and connect MyPage1.page1_signal() to test_object.test_slot2
    qmlpage1.page1_signal.connect(
            test_object.test_slot2,
            type=Qt.ConnectionType.QueuedConnection)

    # !!! access nested page2 from python backend
    qmlpage2 = engine.rootObjects()[0].findChild(QObject, "page2_objname")

    # !!! and connect MyPage2.page2_signal() to test_object.test_slot3
    qmlpage2.page2_signal.connect(
            test_object.test_slot3,
            type=Qt.ConnectionType.QueuedConnection)

    sys.exit(app.exec())

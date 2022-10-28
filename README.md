[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# pyside6-qml-slotsignal
Demo project for Python (PySide6) - QML slot-signal interaction, included
* emit `mainapp_signal` signal, declared in root `ApplicationWindow`, from nested `Page`, and python slot callback,
* emit `page1_signal` signal, declared in nested `page1`, from same page, and python slot callback,
* emit `page2_signal` signal, declared in another nested `page2` , from `page1`, and python slot callback.

The result of successfull 3 signal-slot calls is console output:

<img src="https://user-images.githubusercontent.com/26321368/183409596-12a3cf24-37f8-4bc6-b078-356561ef36b7.png" width="500"/>

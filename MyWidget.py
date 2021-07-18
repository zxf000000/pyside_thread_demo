import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton('click me')
        self.text = QtWidgets.QLabel('hello world', alignment=QtCore.Qt.AlignCenter)
        self.text.setStyleSheet("""
            background-color: #234234;
            color: #ffffff;
            font-size: 20px;
        """)
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.button.clicked.connect(self.magic)
        self.setLayout(self.layout)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))

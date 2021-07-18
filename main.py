import sys
from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget, QLabel, QTextEdit
from MyWidget import MyWidget
from PySide6.QtCore import QUrl
from PySide6.QtCore import QObject, Signal, QThread
from time import sleep

worker = None


class AThread(QThread):
    finished = Signal(str)

    def __init__(self):
        super(AThread, self).__init__()
        self.worker = Worker()
        self.worker.error.connect(self.error_func)

    def error_func(self, obj):
        self.finished.emit(obj['msg'])

    def run(self):
        print('run')
        self.worker.start_work()


class Worker(QObject):
    error = Signal(object)

    def start_work(self):
        print('start')
        for i in range(10):
            sleep(1)
            print('11')
            self.error.emit(({'code': 1, 'msg': '123123'}))


class MyWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.work_thread = AThread()
        self.work_thread.finished.connect(self.receive_error)

        self.label = QTextEdit('')

        self.button = QPushButton('tap me')
        self.button.clicked.connect(self.execute_work)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)
        self.resize(500, 400)
        self.setLayout(self.layout)
        self.show()

    def receive_error(self, str):
        self.label.insertPlainText(str + '\n')

    def execute_work(self):
        print('exec')
        self.work_thread.start()


if __name__ == '__main__':
    app = QApplication([])
    view = MyWindow()
    sys.exit(app.exec())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

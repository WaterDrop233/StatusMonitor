import sys
from function import status
from mwindow import Ui_Form
from PySide2.QtCore import QTimer
from PySide2.QtWidgets import QApplication, QMainWindow


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_label_text)
        self.timer.start(100)  # 定时器每隔1秒触发一次

    def update_label_text(self):
        text = status()
        self.ui.label.setText(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MyMainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

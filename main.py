import sys
import psutil
import GPUtil
from mwindow import Ui_Form
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow


def status(self):
    def GetRAM():
        RAMFree = str(round(psutil.virtual_memory().free / 1024 ** 3, 1))
        RAMUsed = str(round(psutil.virtual_memory().used / 1024 ** 3, 1))
        RAMStatus = "内存:已用:" + RAMUsed + "GB" + "\n" + "     未用:" + RAMFree + "GB"
        return RAMStatus

    def GetCPU():
        CPUStatus = "CPU:已用:" + str(psutil.cpu_percent(interval=0.2))
        return CPUStatus

    def GetGPU():
        if len(GPUtil.getGPUs()) != 0:
            GPUStatus = "显卡:负载率:" + str(round(GPUtil.getGPUs()[0].load, 1)) + "\n" + "     显存使用率:" + str(
                round(GPUtil.getGPUs()[0].memoryUtil, 1))
        else:
            GPUStatus = "未检测到显卡"
        return GPUStatus

    return str(GetCPU() + "\n" + GetRAM() + "\n" + GetGPU())


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_label_text)
        self.timer.start(1000)  # 定时器每隔1秒触发一次
        icon = QIcon("LOGO/LOGO.ico")
        self.setWindowIcon(icon)

    def update_label_text(self):
        text = status()
        self.ui.label.setText(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MyMainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

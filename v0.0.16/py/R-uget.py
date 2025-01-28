from sys import exit, argv
from PySide2.QtWidgets import QSystemTrayIcon, QApplication, QMenu, QAction
from PySide2.QtGui import QIcon
from os import startfile


class RUGetTray(QSystemTrayIcon):
    def __init__(self):
        super().__init__()
        self.icon = None
        self.u_path = "F:\\"
        self.stop_ = True
        self.menu = QMenu()
        self.setup()
        self.show()

    def setup(self):
        self.icon = QIcon("icon.png")
        self.setIcon(self.icon)
        self.setToolTip("R-uget v0.0.16")
        self.add_menu()

    def add_menu(self):
        action = QAction("开始识别", self, triggered=self.start)
        action2 = QAction("结束识别", self, triggered=self.stop)
        action3 = QAction("退出程序", self, triggered=self.quit)
        self.menu.addAction(action)
        self.menu.addAction(action2)
        self.menu.addAction(action3)
        self.setContextMenu(self.menu)

    def stop(self):
        self.stop_ = True
        with open("b", "w") as w:
            w.write("1")

    def start(self):
        self.stop_ = False
        with open("b", "w") as w:
            w.write("2")
        startfile("find_u.exe")

    def quit(self):
        self.hide()
        exit()


if __name__ == "__main__":
    app = QApplication(argv)
    RUGet = RUGetTray()
    exit(app.exec_())

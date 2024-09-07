import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QStackedWidget, QWidget
from PyQt5 import uic


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("MainWindow.ui", self)

        self.stack_widget = self.findChild(QStackedWidget, "stackedWidget")

        self.login_page = self.findChild(QWidget, "Login_Page")
        self.exchange_page = self.findChild(QWidget, "Exchange_Page")

        self.login_button = self.findChild(QPushButton, "Login_Button")
        self.login_button.clicked.connect(self.on_login_enter)

        self.exit_button = self.findChild(QPushButton, "Exit_Button")
        self.exit_button.clicked.connect(self.on_exit_enter)

        self.stack_widget.setCurrentWidget(self.login_page)
        self.show()

    def on_login_enter(self):
        self.stack_widget.setCurrentWidget(self.exchange_page)
        print("Switched to Exchange Page")

    def on_exit_enter(self):
        self.stack_widget.setCurrentWidget(self.login_page)
        print("Switched to Login Page")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    uiWindow = UI()
    sys.exit(app.exec_())

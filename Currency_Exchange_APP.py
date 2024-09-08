import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QStackedWidget, QWidget, QLineEdit
from PyQt5 import uic


class CurrencyExchangeAPP(QMainWindow):
    def __init__(self):
        super(CurrencyExchangeAPP, self).__init__()
        uic.loadUi("MainWindow.ui", self)

        self.stack_widget = self.findChild(QStackedWidget, "stackedWidget")

        self.login_page = self.findChild(QWidget, "Login_Page")
        self.login_button = self.findChild(QPushButton, "Login_Button")
        self.user = self.findChild(QLineEdit, "User_Line")
        self.password = self.findChild(QLineEdit, "User_Line")

        self.exchange_page = self.findChild(QWidget, "Exchange_Page")
        self.exit_button = self.findChild(QPushButton, "Exit_Button")

        self.__load()

    def run(self):
        self.show()

    def __on_login_enter(self):
        print(self.user.text(), self.password.text())
        self.stack_widget.setCurrentWidget(self.exchange_page)
        print("Switched to Exchange Page")

    def __on_exit_enter(self):
        self.stack_widget.setCurrentWidget(self.login_page)
        print("Switched to Login Page")

    def __on_convert_enter(self):
        print("clicked on convert")

    def __load(self):
        self.stack_widget.setCurrentWidget(self.login_page)

        self.login_button.clicked.connect(self.__on_login_enter)
        self.exit_button.clicked.connect(self.__on_exit_enter)

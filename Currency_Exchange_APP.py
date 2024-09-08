from PyQt5.QtWidgets import QPushButton, QMainWindow, QStackedWidget, QWidget, QLineEdit, QComboBox
from PyQt5 import uic

from User_Data import UserData
from Validation import UserValidation


class CurrencyExchangeAPP(QMainWindow):
    def __init__(self):
        super(CurrencyExchangeAPP, self).__init__()
        uic.loadUi("MainWindow.ui", self)

        self.__stack_widget = self.findChild(QStackedWidget, "stackedWidget")

        self.__login_page = self.findChild(QWidget, "Login_Page")
        self.__login_button = self.findChild(QPushButton, "Login_Button")
        self.__user = self.findChild(QLineEdit, "User_Line")
        self.__password = self.findChild(QLineEdit, "Password_Line")

        self.__exchange_page = self.findChild(QWidget, "Exchange_Page")
        self.__convert_button = self.findChild(QPushButton, "Convert_Button")
        self.__exit_button = self.findChild(QPushButton, "Exit_Button")
        self.__currency_1 = self.findChild(QComboBox, "Currency_1")
        self.__currency_2 = self.findChild(QComboBox, "Currency_2")
        self.__converted_amount = self.findChild(QLineEdit, "Converted_Amount_Line")
        self.__input_amount = self.findChild(QLineEdit, "Amount_Line")

        self.__connect_button_events()

    def run(self):
        self.__stack_widget.setCurrentWidget(self.__login_page)
        self.show()

    def __on_login_enter(self):
        user_data = UserData()
        user_validation = UserValidation(user_data)
        username = self.__user.text()
        password = self.__password.text()
        if user_validation.validate(username, password):
            self.__stack_widget.setCurrentWidget(self.__exchange_page)

    def __on_exit_enter(self):
        self.__stack_widget.setCurrentWidget(self.__login_page)

    def __on_convert_enter(self):
        print(self.__currency_1.currentText())
        print(self.__currency_2.currentText())
        print(self.__input_amount.text())
        print("clicked on convert")

    def __connect_button_events(self):
        self.__login_button.clicked.connect(self.__on_login_enter)
        self.__exit_button.clicked.connect(self.__on_exit_enter)
        self.__convert_button.clicked.connect(self.__on_convert_enter)

from PyQt5.QtWidgets import QPushButton, QMainWindow, QStackedWidget, QWidget, QLineEdit, QComboBox
from PyQt5 import uic

from Error_Handler import ErrorHandler


class CurrencyExchangeAPP(QMainWindow):
    def __init__(self, *, validation_controller, currency_converter, currency_data):
        super(CurrencyExchangeAPP, self).__init__()
        uic.loadUi("MainWindow.ui", self)

        self.__validation_controller = validation_controller
        self.__currency_converter = currency_converter
        self.__currency_data = currency_data

        self.__stack_widget = self.findChild(QStackedWidget, "stackedWidget")

        self.__login_page = self.findChild(QWidget, "Login_Page")
        self.__login_button = self.findChild(QPushButton, "Login_Button")
        self.__user = self.findChild(QLineEdit, "User_Line")
        self.__password = self.findChild(QLineEdit, "Password_Line")

        self.__exchange_page = self.findChild(QWidget, "Exchange_Page")
        self.__convert_button = self.findChild(QPushButton, "Convert_Button")
        self.__exit_button = self.findChild(QPushButton, "Exit_Button")
        self.__currency_from = self.findChild(QComboBox, "Currency_1")
        self.__currency_to = self.findChild(QComboBox, "Currency_2")
        self.__converted_amount = self.findChild(QLineEdit, "Converted_Amount_Line")
        self.__input_amount = self.findChild(QLineEdit, "Amount_Line")

        self.__connect_button_events()
        self.__fill_currency()

    def run(self):
        self.__reset_login_page()
        self.__reset_exchange_page()
        self.__stack_widget.setCurrentWidget(self.__login_page)
        self.show()

    def __on_login_enter(self):
        username = self.__user.text()
        password = self.__password.text()
        if self.__validation_controller.validate(username, password):
            self.__stack_widget.setCurrentWidget(self.__exchange_page)
            self.__reset_login_page()
        else:
            ErrorHandler("Login Failed", "Username or password is incorrect.")

    def __on_exit_enter(self):
        self.__stack_widget.setCurrentWidget(self.__login_page)
        self.__reset_exchange_page()

    def __on_convert_enter(self):
        currency_from = self.__currency_from.currentText()
        currency_to = self.__currency_to.currentText()
        input_amount = self.__input_amount.text()
        try:
            amount = float(input_amount)
            result = self.__currency_converter.convert(currency_from, currency_to, amount)
            if result is None:
                self.__converted_amount.setText("Invalid conversion")
            else:
                self.__converted_amount.setText(f"{result:.2f}")
        except ValueError:
            self.__converted_amount.setText("Invalid input")
        except Exception:
            self.__converted_amount.setText("Error")

    def __fill_currency(self):
        currency_data_list = list(self.__currency_data)
        self.__currency_from.addItems(currency_data_list)
        self.__currency_to.addItems(currency_data_list)
        default_currency_from = 'GEL'
        default_currency_to = 'USD'
        if default_currency_from in currency_data_list and default_currency_to in currency_data_list:
            self.__currency_from.setCurrentText(default_currency_from)
            self.__currency_to.setCurrentText(default_currency_to)

    def __connect_button_events(self):
        self.__login_button.clicked.connect(self.__on_login_enter)
        self.__exit_button.clicked.connect(self.__on_exit_enter)
        self.__convert_button.clicked.connect(self.__on_convert_enter)

    def __reset_login_page(self):
        self.__user.setText("")
        self.__password.setText("")

    def __reset_exchange_page(self):
        self.__currency_from.setCurrentText('GEL')
        self.__currency_to.setCurrentText('USD')
        self.__converted_amount.setText(f"")
        self.__input_amount.setText("")

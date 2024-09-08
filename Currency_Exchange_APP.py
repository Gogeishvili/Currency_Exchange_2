from PyQt5.QtWidgets import QPushButton, QMainWindow, QStackedWidget, QWidget, QLineEdit, QComboBox, QMessageBox
from PyQt5 import uic


class CurrencyExchangeAPP(QMainWindow):
    def __init__(self, *, validation_controller, convert_controller, currency_data):
        super(CurrencyExchangeAPP, self).__init__()
        uic.loadUi("MainWindow.ui", self)

        self.__validation_controller = validation_controller
        self.__converter_controller = convert_controller
        self.__currencies_data = currency_data

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
        self.__fill_currency()

    def run(self):
        self.__reset_login_page()
        self.__reset_exchange_page()
        self.__stack_widget.setCurrentWidget(self.__login_page)
        self.show()

    def __show_error_message(self, title, message):
        error_msg = QMessageBox()
        error_msg.setIcon(QMessageBox.Warning)
        error_msg.setWindowTitle(title)
        error_msg.setText(message)
        error_msg.exec_()

    def __on_login_enter(self):
        username = self.__user.text()
        password = self.__password.text()
        if self.__validation_controller.validate(username, password):
            self.__stack_widget.setCurrentWidget(self.__exchange_page)
            self.__reset_login_page()
        else:
            self.__show_error_message("Login Failed", "Username or password is incorrect.")

    def __on_exit_enter(self):
        self.__stack_widget.setCurrentWidget(self.__login_page)
        self.__reset_exchange_page()

    def __on_convert_enter(self):
        currency_1 = self.__currency_1.currentText()
        currency_2 = self.__currency_2.currentText()
        amount_text = self.__input_amount.text()

        try:
            amount = float(amount_text)
            result = self.__converter_controller.convert(currency_1, currency_2, amount)
            if result is None:
                self.__converted_amount.setText("Invalid conversion")
            else:
                self.__converted_amount.setText(f"{result:.2f}")
        except ValueError:
            self.__converted_amount.setText("Invalid input")
        except Exception as e:
            self.__converted_amount.setText("Error")

    def __fill_currency(self):
        currencies = list(self.__currencies_data)
        self.__currency_1.addItems(currencies)
        self.__currency_2.addItems(currencies)
        default_currency_1 = 'GEL'
        default_currency_2 = 'USD'
        if default_currency_1 in currencies and default_currency_2 in currencies:
            self.__currency_1.setCurrentText(default_currency_1)
            self.__currency_2.setCurrentText(default_currency_2)

    def __connect_button_events(self):
        self.__login_button.clicked.connect(self.__on_login_enter)
        self.__exit_button.clicked.connect(self.__on_exit_enter)
        self.__convert_button.clicked.connect(self.__on_convert_enter)

    def __reset_login_page(self):
        self.__user.setText("")
        self.__password.setText("")

    def __reset_exchange_page(self):
        self.__currency_1.setCurrentText('GEL')
        self.__currency_2.setCurrentText('USD')
        self.__converted_amount.setText(f"")
        self.__input_amount.setText("")

import sys
from PyQt5.QtWidgets import QApplication
from Currency_Data_Controller import CurrencyDataController
from Currency_Exchange_APP import CurrencyExchangeAPP
from User_Data_Controller import UserDataController
from User_Validation_Controller import UserValidationController
from Currency_Converter import CurrencyConverter


def main():
    app = QApplication(sys.argv)

    user_data_controller = UserDataController()
    user_data = user_data_controller.users

    currency_data_controller = CurrencyDataController()
    currency_data = currency_data_controller.currency_data

    validation_controller = UserValidationController(user_data)

    currency_converter = CurrencyConverter(currency_data)

    currency_exchange_app = CurrencyExchangeAPP(validation_controller=validation_controller,
                                                currency_converter=currency_converter, currency_data=currency_data)
    currency_exchange_app.run()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

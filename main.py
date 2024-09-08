import sys

from PyQt5.QtWidgets import QApplication

from Currency_Data import CurrencyDataController
from Currency_Exchange_APP import CurrencyExchangeAPP
from User_Data import UserDataController
from Validation import UserValidationController
from Currency_Converter import CurrencyConverter


def main():
    app = QApplication(sys.argv)

    user_data_contoller = UserDataController()
    user_data = user_data_contoller.users

    currency_data_controller = CurrencyDataController()
    currency_data = currency_data_controller.currencies

    validation_controller = UserValidationController(user_data)

    currencyConverter = CurrencyConverter(currency_data)

    currency_exchange_app = CurrencyExchangeAPP(validation_controller=validation_controller,
                                                convert_controller=currencyConverter,
                                                currency_data=currency_data)
    currency_exchange_app.run()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

import sys
from PyQt5.QtWidgets import QApplication

from Currency_Data import CurrencyDataController
from Currency_Exchange_APP import CurrencyExchangeAPP
from User_Data import UserDataController
from Validation import UserValidationController


def main():
    app = QApplication(sys.argv)

    user_data = UserDataController().users
    currency_data = CurrencyDataController().currencies
    user_validation_controller=UserValidationController(user_data)

    currency_exchange_app = CurrencyExchangeAPP(user_validation_controller=user_validation_controller,
                                                currency_data=currency_data)
    currency_exchange_app.run()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

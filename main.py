import sys
from PyQt5.QtWidgets import QApplication
from Currency_Exchange_APP import CurrencyExchangeAPP


def main():
    app = QApplication(sys.argv)



    currency_exchange_app = CurrencyExchangeAPP()
    currency_exchange_app.run()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

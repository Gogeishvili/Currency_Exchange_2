class CurrencyConverter:
    def __init__(self, currency_data):
        self.__currency_data = currency_data

    def convert(self, from_currency, to_currency, amount):
        normalized_rates = self.__normalize_rates(self.__currency_data)

        if from_currency not in normalized_rates or to_currency not in normalized_rates:
            return None
        try:
            amount = float(amount)
        except ValueError:
            return None

        rate = normalized_rates[to_currency] / normalized_rates[from_currency]
        return amount * rate

    def __normalize_rates(self, rates):
        base_rate = rates.get('GEL', 1.00)
        normalized_rates = {code: base_rate / rate for code, rate in rates.items()}
        return normalized_rates

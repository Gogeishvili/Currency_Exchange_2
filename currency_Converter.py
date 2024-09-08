class CurrencyConverter:
    def __init__(self, currency_data):
        self.__currency_data = currency_data

    def convert(self, currency_from, currency_to, amount):
        normalized_rates = self.__normalize_rates(self.__currency_data)

        if currency_from not in normalized_rates or currency_to not in normalized_rates:
            return None
        try:
            amount = float(amount)
        except ValueError:
            return None

        rate = normalized_rates[currency_to] / normalized_rates[currency_from]
        return amount * rate

    def __normalize_rates(self, rates):
        base_rate = rates.get('GEL', 1.00)
        normalized_rates = {code: base_rate / rate for code, rate in rates.items()}
        return normalized_rates

import requests

class CurrencyDataController:
    def __init__(self):
        self.__api_url = 'https://nbg.gov.ge/gw/api/ct/monetarypolicy/currencies/ka/json/?date=2024-09-03'
        self.__currencies = self.__load_currency_data()

    @property
    def currencies(self):
        return self.__currencies

    def __load_currency_data(self):
        response = requests.get(self.__api_url)

        if response.status_code == 200:
            data = response.json()

            if isinstance(data, list):
                data = data[0]
                if 'currencies' in data:
                    currencies = data['currencies']

                    currency_dict = {}
                    for currency in currencies:
                        code = currency['code']
                        rate = currency['rate']
                        currency_dict[code] = rate

                    if 'GEL' not in currency_dict:
                        currency_dict['GEL'] = 1.00

            return currency_dict
        else:
            raise Exception("Failed to fetch data from API")


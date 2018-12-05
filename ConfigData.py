DRIVERPATH = '/home/zebra/BrowserDrivers/chromedriver'
URL = 'https://finance.i.ua/'

CURRENCY_AMOUNT = 'currency_amount'
ACTUAL_EXCHANGE = "//p[@id='UAH']//input[@id='currency_exchange']"
EXPECTED_EXCHANGE = "//tfoot[@class='service_bank_rates_usd']//tr[@role='row']//td[@class='buy_rate']"

AVERAGE = "//*[@id='latest_currency_container']/tfoot[1]/tr[1]/td[1]/span/span"
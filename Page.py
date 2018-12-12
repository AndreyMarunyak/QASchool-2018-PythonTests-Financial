from Locators import MainPageLocators

class MainPage():

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.locator = MainPageLocators()

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def __calculate_average_value(self):
        span_list = []
        for el in range(1, 30):
            span_list.append(float(self.find_element(*self.locator.list_of_values(el)).text))

        return sum(span_list)

    def get_exchange_value(self):
        EXCHANGE_VALUE = self.find_element(*self.locator.ACTUAL_EXCHANGE_FIELD)
        EXCHANGE_VALUE = self.driver.execute_script("return arguments[0].value", EXCHANGE_VALUE)
        EXCHANGE_VALUE = float(EXCHANGE_VALUE.replace(' ', ''))
        return EXCHANGE_VALUE

    def set_value_to_exchange(self, value):
        return self.driver.find_element(*self.locator.CURRENCY_AMOUNT_FIELD).send_keys(value)

    def get_expected_value(self):
        EXPECTED_VALUE = self.find_element(*self.locator.AVERAGE_VALUE_FIELD).text
        EXPECTED_VALUE = round((float(EXPECTED_VALUE) * 120), 2)
        return EXPECTED_VALUE

    def get_expected_average_value(self):
        return float(self.find_element(*self.locator.AVERAGE_VALUE_FIELD).text)

    def get_actual_average_value(self):
        return round((self.__calculate_average_value() / 29), 4)
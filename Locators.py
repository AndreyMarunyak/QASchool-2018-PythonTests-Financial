from selenium.webdriver.common.by import By
from ConfigData import *

class MainPageLocators():

    CURRENCY_AMOUNT_FIELD = (By.XPATH, CURRENCY_AMOUNT)
    ACTUAL_EXCHANGE_FIELD = (By.XPATH, ACTUAL_EXCHANGE)
    AVERAGE_VALUE_FIELD = (By.XPATH, ACTUAL_EXCHANGE)

    def list_of_values(self, value):
        LIST_OF_VALUES = (By.XPATH, "//*[@id='latest_currency_container']/tbody[1]/tr["
                          + str(value)
                          + "]/td[1]/span/span")
        return LIST_OF_VALUES
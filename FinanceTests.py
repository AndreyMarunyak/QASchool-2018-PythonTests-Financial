import time
import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Browser import *
from ConfigData import *

Chrome = Browser.chrome()

class FinanceTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        Chrome.get(URL)

    def test_1_amountToSell(self):
        Chrome.find_element(By.ID, CURRENCY_AMOUNT).send_keys('120')
        Current_exchange = Chrome.find_element(By.XPATH, ACTUAL_EXCHANGE)
        Actual_exchange = Chrome.execute_script("return arguments[0].value", Current_exchange)
        Actual_exchange = Actual_exchange.replace(' ', '')

        Expected_exchange = Chrome.find_element(By.XPATH, EXPECTED_EXCHANGE).text
        Expected_exchange = round((float(Expected_exchange) * 120), 2)


        self.assertTrue(Expected_exchange == float(Actual_exchange))

    @classmethod
    def tearDownClass(cls):
        Chrome.close()
        Chrome.quit()
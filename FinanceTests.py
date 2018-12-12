import time
import unittest

from selenium.webdriver.common.by import By

from Browser import *
from ConfigData import *
from Page import MainPage

Chrome = Browser.chrome()

MainPage = MainPage(Chrome, URL)

class FinanceTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        Chrome.get(URL)

    def test_1_amountToSell(self):

        MainPage.set_value_to_exchange('120')

        Actual_exchange = MainPage.get_exchange_value()

        Expected_exchange = MainPage.get_expected_value()

        self.assertTrue(Expected_exchange == Actual_exchange, 'Wrong calculating')

    def test_2_averageCurrency(self):

        average_expected = float(Chrome.find_element(By.XPATH, AVERAGE).text)
        average_actual = round((sumRates(Chrome) / 29), 4)
        print(average_actual)
        print(average_expected)
        self.assertTrue(average_actual == average_expected, 'Actual result {0}, expected result {1}'.format(
            str(average_actual), str(average_expected)))


    @classmethod
    def tearDownClass(cls):

        Chrome.close()
        Chrome.quit()
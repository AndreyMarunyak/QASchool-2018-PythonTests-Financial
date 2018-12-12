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

        expected_exchange = MainPage.get_expected_value()

        self.assertTrue(expected_exchange == Actual_exchange, 'Wrong calculating')

    def test_2_averageCurrency(self):

        average_expected = MainPage.get_expected_average_value()
        average_actual = MainPage.get_actual_average_value()

        self.assertTrue(average_actual == average_expected, 'Actual result {0}, expected result {1}'.format(
            str(average_actual), str(average_expected)))


    @classmethod
    def tearDownClass(cls):

        Chrome.close()
        Chrome.quit()
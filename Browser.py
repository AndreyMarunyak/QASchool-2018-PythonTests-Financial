from selenium import webdriver
from selenium.webdriver.common.by import By

from ConfigData import *


class Browser():

    @staticmethod
    def chrome():
        return webdriver.Chrome(executable_path=DRIVERPATH)

def sumRates(browser):
    span_list = []
    for el in range(1, 30):
        span_list.append(float(browser.find_element(By.XPATH, "//*[@id='latest_currency_container']/tbody[1]/tr["
                                             + str(el) + "]/td[1]/span/span").text))

    return sum(span_list)
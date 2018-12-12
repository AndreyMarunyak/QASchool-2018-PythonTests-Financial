from selenium import webdriver

from ConfigData import *


class Browser():

    @staticmethod
    def chrome():
        return webdriver.Chrome(executable_path=DRIVERPATH)


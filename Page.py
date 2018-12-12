from Locators import MainPageLocators

class MainPage():

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.locator = MainPageLocators()

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def calculate_average_value(self, values):
        span_list = []
        for el in range(1, 30):
            span_list.append(self.locator.list_of_values(el).text)


        return sum(span_list)
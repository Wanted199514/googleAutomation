from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.BasePage import BasePage


class searchPageLocators:
    locator_search_field = (By.XPATH, "//input[@title]")


class SearchPage(BasePage):

    def set_search_field(self, text):
        search_field = self.find_element(searchPageLocators.locator_search_field)
        search_field.click()
        search_field.send_keys(text)
        search_field.send_keys(Keys.ENTER)
        return search_field

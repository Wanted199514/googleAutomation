from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class searchResultLocators:
    locator_search_results = (By.XPATH, "//div[@id='search']/div/div/div/div/div")
    second_link = (By.XPATH, "//div[2]/div/div/div/a/h3")


class SearchResultPage(BasePage):

    def get_search_results(self):
        all_list = self.find_elements(searchResultLocators.locator_search_results, time=2)
        return all_list

    def click_on_second_link(self):
        return self.find_element(searchResultLocators.second_link, time=2).click()


#     search_results = webDriver.find_elements_by_xpath("//div[@id='search']/div/div/div/div/div")
#     link = search_results[1].find_element_by_xpath(".//h3/span")
#     link.click()
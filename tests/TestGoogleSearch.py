from selenium.webdriver.support.wait import WebDriverWait

from pages.SearchPage import SearchPage
from pages.SearchResultPage import SearchResultPage


def test_google_search(browser):
    search_page = SearchPage(browser)
    search_page.go_to_site()
    search_page.set_search_field("markets")
    search_result_page = SearchResultPage(browser)
    assert 9 >= len(search_result_page.get_search_results())
    search_result_page.click_on_second_link()
    assert browser.title == "Markets: Indexes, Bonds, Forex, Key Commodities, ETFs"

# def testGoogleSearch():
#     webDriver = WebDriver(executable_path="C://Windows//System32//chromedriver.exe")
#     webDriver.get("https://www.google.com.ua/")
#
#     search_field = webDriver.find_element_by_xpath("//input[@title]")
#     search_field.send_keys("markets")
#     search_field.send_keys(Keys.ENTER)
#
#     def checkResultsCount(webDriver):
#         search_results = webDriver.find_elements_by_xpath("//div[@id='search']/div/div/div/div/div")
#         return len(search_results) >= 9
#
#     WebDriverWait(webDriver, 5, 0.5).until(checkResultsCount, "Количество результатов поиска больше 9")
#
#     search_results = webDriver.find_elements_by_xpath("//div[@id='search']/div/div/div/div/div")
#     link = search_results[1].find_element_by_xpath(".//h3/span")
#     link.click()
#
#     assert webDriver.title == "Markets: Indexes, Bonds, Forex, Key Commodities, ETFs"
#     webDriver.close()
#     webDriver.quit()

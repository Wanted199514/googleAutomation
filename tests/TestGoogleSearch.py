from pages.SearchPage import SearchPage
from pages.SearchResultPage import SearchResultPage


def test_google_search(browser):
    search_page = SearchPage(browser)
    search_page.go_to_site()
    search_page.set_search_field("markets")
    search_result_page = SearchResultPage(browser)
    assert 10 == len(search_result_page.get_search_results())
    search_result_page.click_on_second_link()
    assert browser.title == "Markets: Indexes, Bonds, Forex, Key Commodities, ETFs"

import json
import re
from selenium import webdriver

URL = "https://www.kinopoisk.ru/top/navigator/m_act[years]/1890%3A2020/m_act[num_vote]/10/m_act[rating]" \
      "/1%3A/m_act[tomat_rating]/1%3A/m_act[review_procent]/1%3A/m_act[is_film]/on/order/rating/perpage/200/#results"


class Parser:

    def __init__(self, headless=False):
        self._dr = self.sign_in(headless)
        self._prev_page = ''
        self._current_page = URL
        self._next_page = ''
        self.first_200 = []

    def sign_in(self, headless):
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("-headless")
        return webdriver.Firefox(options=options)

    def final(self):
        self._dr.quit()
        with open("../../../static/first_200.json", 'w') as f:
            json.dump(self.first_200, f)

    def prepare_url(self):
        self._dr.get(self._current_page)

    def start(self):
        self.prepare_url()
        item_list = self._dr.find_element_by_css_selector("#itemList")
        for count, div in enumerate(item_list.find_elements_by_xpath("./div")):
            info = div.find_element_by_xpath(".//div[@class='info']")
            name = info.find_element_by_xpath(".//div[@class='name']/a")
            url = name.get_attribute("href")
            title = name.text
            en_name = info.find_element_by_xpath(".//div[@class='name']/span").text
            rate_kinopoisk = div.find_element_by_xpath("./div[4]").get_attribute("value")
            image = div.find_element_by_xpath(".//div[@class='poster']/a/img").get_attribute("src")
            record = {
                'title': title,
                'en_title': en_name,
                'mark': rate_kinopoisk,
                'poster': image,
                '_link': url,
            }
            print(count, record)
            self.first_200.append(record)


if __name__ == '__main__':
    parser = Parser(headless=True)
    try:
        parser.start()
    finally:
        parser.final()
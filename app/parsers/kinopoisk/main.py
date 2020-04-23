import json
import re
from selenium import webdriver

BASE_URL = "https://www.kinopoisk.ru/top/navigator"
URL = "/m_act[years]/1890%3A2020/m_act[num_vote]/10/m_act[rating]" \
      "/1%3A/m_act[tomat_rating]/1%3A/m_act[review_procent]/1%3A/m_act[is_film]/on/order/rating/perpage/200/page/1/#results"


class Parser:

    def __init__(self, headless=False):
        self._dr = self.sign_in(headless)
        self._prev_page = None
        self._current_page = None
        self._next_page = None
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

    def write_to_file(self):
        with open("../../../static/first_200.json", 'a') as f:
            json.dump(self.first_200, f)

    def change_page(self):
        if self._current_page is None:
            self._current_page = URL
            self._set_page()
        else:
            self._prev_page = self._current_page
            url = re.split('/', self._prev_page)
            for i, ii in enumerate(url):
                if ii == "page":
                    url[i+1] = int(url[i+1])+1
            self._current_page = '/'.join([str(u) for u in url])
            self._set_page()

    def _set_page(self):
        self._dr.get(BASE_URL+self._current_page)

    def _append_to(self, di):
        self.first_200.append(di)
        self.write_to_file()

    def start(self):
        for i in range(1,55):

            self.change_page()
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
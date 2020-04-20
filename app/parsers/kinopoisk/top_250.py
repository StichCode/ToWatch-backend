import json
import re


from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

URL = "https://www.kinopoisk.ru/top"
"""
{
    title: '',
    origin_title: '',
    year: '',
    mark: '',
    count_votes: ''
    _link: ''

}

"""

MAIN_JSON = []

op = webdriver.FirefoxOptions()
op.add_argument("-headless")

dr = webdriver.Firefox(options=op)
dr.get(URL)
table = dr.find_element_by_xpath('//*[@id="block_left"]/div/table/tbody/tr/td/table[3]/tbody/tr/td/table/tbody')
for el in table.find_elements_by_xpath("./tr"):
    if not el.get_attribute("id"):
        pass
    else:
        try:
            span = el.find_element_by_xpath("./td[2]/span")
        except NoSuchElementException:
            span = None
        MAIN_JSON.append({
            "title": re.split(" ", el.find_element_by_xpath("./td[2]/a").text)[0],
            "origin_title": "" if span is None else span.text,
            "year": re.findall("[0-9]+", el.find_element_by_xpath("./td[2]/a").text)[0],
            "mark": el.find_element_by_xpath("./td[3]/div/a").text,
            "count_votes": el.find_element_by_xpath("./td[3]/div/span").text,
            "_link": el.find_element_by_xpath("./td[2]/a").get_attribute('href')
        })

print(MAIN_JSON)
with open("top250.json", "w") as f:
    json.dump(MAIN_JSON, f)


dr.quit()
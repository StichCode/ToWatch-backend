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
            origin_title = el.find_element_by_xpath("./td[2]/span")
            mark = el.find_element_by_xpath("./td[3]/div/a")
            votes = el.find_element_by_xpath("./td[3]/div/span")
        except NoSuchElementException:
            origin_title = None
            mark = None
            votes = None

        MAIN_JSON.append({
            "title": re.findall("\D+", el.find_element_by_xpath("./td[2]/a").text)[0].strip(),
            "origin_title": "" if origin_title is None else origin_title.text,
            "year": re.findall("[0-9]+", el.find_element_by_xpath("./td[2]/a").text)[0],
            "mark": "" if mark is None else mark.text,
            "count_votes": "" if votes is None else votes.text,
            "_link": el.find_element_by_xpath("./td[2]/a").get_attribute('href')
        })

dr.quit()
print(MAIN_JSON)
with open("top250.json", "w") as f:
    json.dump(MAIN_JSON, f)


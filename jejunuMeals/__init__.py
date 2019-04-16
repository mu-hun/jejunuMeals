#!/usr/bin/python3
# -*- coding: utf-8 -*-

from requests import get
from bs4 import BeautifulSoup as bs
from datetime import datetime

URL = 'http://www.jejunu.ac.kr/camp/stud/foodmenu'

YAML = {k: {'점심': {}, '저녁': {}} for k in [0, 1, 2, 3, 4]}

WEEKDAYS = {0: 0, 1: 0, 2: 0, 3: 0,
            4: 1, 5: 1, 6: 1, 7: 1,
            8: 2, 9: 2, 10: 2, 11: 2,
            12: 3, 13: 3, 14: 3, 15: 3,
            16: 4, 17: 4, 18: 4, 19: 4}

FLAGS = {k: 2 for k in [0, 4, 8, 12, 16]}


class JejunuMeals:

    def __init__(self, url=URL, yaml=YAML, weekdays=WEEKDAYS, flags=FLAGS):
        self.url = url
        self.yaml = yaml
        self.weekdays = weekdays
        self.flags = flags

    def _soup(self, url):
        return bs(get(url).text, 'html.parser')

    def _table_tds(self):
        soup = self._soup(self.url)
        return [[cell.text for cell in
                 row.select('td.border_right.txt_center')]
                for row in soup.select('table > tr')][1:21]

    def menus(self, _weekday=None):
        yaml = self.yaml
        for index, item in enumerate(self._table_tds()):
            weekday, flag = self.weekdays[index], self.flags.get(index, 1)
            yaml[weekday]['점심'][item[flag - 1]] = item[flag][1:-1].split("\n")
            yaml[weekday]['저녁'][item[flag - 1]] = item[flag + 1][1:-1].split("\n")
        return yaml.get(_weekday, yaml)

    def daily(self):
        return self.menus(datetime.now().weekday())


if __name__ == '__main__':
    from pprint import pprint
    pprint(JejunuMeals().menus())

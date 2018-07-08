#!/usr/bin/python3
# -*- coding: utf-8 -*-

from requests import get
from bs4 import BeautifulSoup as bs

URL = 'http://www.jejunu.ac.kr/camp/stud/foodmenu'

YAML = {0: {'점심': {}, '저녁': {}}, 1: {'점심': {}, '저녁': {}}, 2: {'점심': {}, '저녁': {}},
        3: {'점심': {}, '저녁': {}}, 4: {'점심': {}, '저녁': {}}}

WEEKDAYS = {0: 0, 1: 0, 2: 0, 3: 0,
            4: 1, 5: 1, 6: 1, 7: 1,
            8: 2, 9: 2, 10: 2, 11: 2,
            12: 3, 13: 3, 14: 3, 15: 3,
            16: 4, 17: 4, 18: 4, 19: 4}

FLAGS = {0: 2, 4: 2, 8: 2, 12: 2, 16: 2}

class JejunuMeals:

    def __init__(self, url=URL, yaml=YAML, weekdays=WEEKDAYS, flags=FLAGS):
        self.url = url
        self.yaml = yaml
        self.weekdays = weekdays
        self.flags = flags

    def soup(self, url):
        return bs(get(url).text, 'html.parser')

    def table_tds(self):
        soup = self.soup(self.url)
        table_data = [[cell.text for cell in
                      row.select('td.border_right.txt_center')]
                      for row in soup.select('table > tr')]
        table_data = table_data[1:21]
        return table_data

    def fetch_meals(self):
        data = self.table_tds()
        yaml = self.yaml
        for index, atom in enumerate(data):
            weekday = self.weekdays[index]
            flag = self.flags.get(index, 1)
            yaml[weekday]['점심'][atom[flag - 1]] = atom[flag]
            yaml[weekday]['저녁'][atom[flag - 1]] = atom[flag + 1]
        return yaml

if __name__ == '__main__':
    from pprint import pprint
    pprint(JejunuMeals().fetch_meals())

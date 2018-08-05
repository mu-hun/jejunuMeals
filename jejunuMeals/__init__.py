#!/usr/bin/python3
# -*- coding: utf-8 -*-

from requests import get
from bs4 import BeautifulSoup as bs
# import re

URL = {'wcms':'http://dormitory.neo-internet.co.kr/board/adm/Recipe/restaurant.php', 'www':'http://www.jejunu.ac.kr/camp/stud/foodmenu'}

ENCODING = {URL['wcms']: 'euc-kr', URL['www']:'utf-8'}

CSS_SELECTORS = {'wcms': {0:'table.wanted', 1:'tr > td'}, 'www':{0:'td.border_right.txt_center', 1:'table > tr'}}

LIST_RANGE = {'wcms': [2, 3], 'www': [1, 21]}

YAML = dict.fromkeys([0, 1, 2, 3, 4], {'점심': {}, '저녁': {}})

WEEKDAYS = {0: 0, 1: 0, 2: 0, 3: 0,
            4: 1, 5: 1, 6: 1, 7: 1,
            8: 2, 9: 2, 10: 2, 11: 2,
            12: 3, 13: 3, 14: 3, 15: 3,
            16: 4, 17: 4, 18: 4, 19: 4}

FLAGS = dict.fromkeys([0, 4, 8, 12, 16], 2)

class JejunuMeals:

    def __init__(self, url=URL, selectors=CSS_SELECTORS, encoding=ENCODING, list_range=LIST_RANGE, yaml=YAML, weekdays=WEEKDAYS, flags=FLAGS):
        self.url = url
        self.selectors = selectors
        self.encoding = encoding
        self.list_range = list_range
        self.yaml = yaml
        self.weekdays = weekdays
        self.flags = flags

    def soup(self, url):
        r = get(url)
        r.encoding = self.encoding[url]
        return bs(r.text, 'html.parser')
    
    # def regex(self, data):
    # TODO

    def table_tds(self, par):
        soup = self.soup(self.url[par])
        table_data = [[cell.text for cell in
                      row.select(self.selectors[par][0])]
                      for row in soup.select(self.selectors[par][1])]
        table_data = table_data[self.list_range[par][0]:self.list_range[par][1]]
        return table_data

    def fetch_meals(self, par):
        data = self.table_tds(par)
        yaml = self.yaml
        for index, atom in enumerate(data):
            weekday = self.weekdays[index]
            flag = self.flags.get(index, 1)
            yaml[weekday]['점심'][atom[flag - 1]] = atom[flag]
            yaml[weekday]['저녁'][atom[flag - 1]] = atom[flag + 1]
        return yaml

if __name__ == '__main__':
    from pprint import pprint
    pprint(JejunuMeals().fetch_meals('www'))

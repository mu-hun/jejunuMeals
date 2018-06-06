#!/usr/bin/python3
# -*- coding: utf-8 -*-

from requests import get
from bs4 import BeautifulSoup as bs

import yaml

import datetime

URL = 'http://www.jejunu.ac.kr/camp/stud/foodmenu'

dt = datetime.datetime.now()
today = dt.weekday()

class JejunuMeals:

    def __init__(self, url=URL):
        self.url = url

    def soup(self, url):
        return bs(get(url).text, 'html.parser')

    def table_tds(self):
        soup = self.soup(self.url)
        table_data = [[cell.text for cell in
                      row.select('td.border_right.txt_center')]
                      for row in soup.select('table > tr')]
        return table_data

    def fetch_meals(self):
        toYaml = {0: {'점심': {'정식': '', '특식': '', '양식': '', '중식': ''}, '저녁': {'정식': '', '특식': '', '양식': '', '중식': ''}}, 1: {'점심': {'정식': '', '특식': '', '양식': '', '중식': ''}, '저녁': {'정식': '', '특식': '', '양식': '', '중식': ''}}, 2: {'점심': {'정식': '', '특식': '', '양식': ''}, '저녁': {'정식': '', '특식': '', '양식': '', '중식': ''}}, 3: {'점심': {'정식': '', '특식': '', '양식': '', '중식': ''}, '저녁': {'정식': '', '특식': '', '양식': '', '중식': ''}}, 4: {'점심': {'정식':'', '특식': '', '양식': '', '중식': ''}, '저녁': {'정식': '', '특식': '', '양식': '', '중식': ''}}}
        weekday = -1
        data = JejunuMeals().table_tds()
        for index, atom in enumerate(data):
            if index == 1 or index == 5 or index == 9 or index == 13 or index == 17:
                weekday = weekday + 1
                toYaml[weekday]['점심']['정식'] = atom[2]
                toYaml[weekday]['저녁']['정식'] = atom[3]
            elif index == 2 or index == 6 or index == 10 or index == 14 or index == 18:
                toYaml[weekday]['점심']['특식'] = atom[1]
                toYaml[weekday]['저녁']['특식'] = atom[2]
            elif index == 3 or index == 7 or index == 11 or index == 15 or index == 19:
                toYaml[weekday]['점심']['양식'] = atom[1]
                toYaml[weekday]['저녁']['양식'] = atom[2]
            elif index == 4 or index == 8 or index == 12 or index == 16 or index == 20:
                toYaml[weekday]['점심']['중식'] = atom[1]
                toYaml[weekday]['저녁']['중식'] = atom[2]
        return toYaml
    
    def dump_yaml(self):
        with open('output.yaml', 'w') as outfile:
            yaml.dump(self.fetch_meals(), outfile, default_flow_style=False, allow_unicode=True)
    
    def fetch_today(self, time, food_style):
        foodmenu = self.fetch_meals()
        return foodmenu[today][time][food_style]
    
    def fetch_someday(self, someday, time, food_style):
        foodmenu = self.fetch_meals()
        return foodmenu[someday][time][food_style]

if __name__ == '__main__':
    foodmenu = JejunuMeals()
    foodmenu.dump_yaml()
    print(foodmenu.fetch_today('점심', '정식'))
    print(foodmenu.fetch_someday(0, '점심', '정식'))

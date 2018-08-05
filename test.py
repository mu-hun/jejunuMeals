# -*- coding: utf-8 -*-
from jejunuMeals import JejunuMeals
from pprint import pprint
# import re

pprint(JejunuMeals().table_tds('wcms'))
print('--')
pprint(JejunuMeals().fetch_meals('www'))
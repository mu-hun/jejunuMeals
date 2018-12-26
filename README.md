# jejunuMeals

[![Travis (.org) branch](https://img.shields.io/travis/BetaF1sh/jejunuMeals/master.svg?style=flat-square)](https://travis-ci.org/BetaF1sh/jejunuMeals)
[![PyPI version](https://img.shields.io/pypi/v/JejunuMeals.svg?style=flat-square)](https://pypi.org/project/jejunuMeals/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/jejunuMeals.svg?style=flat-square)
[![GitHub issues](https://img.shields.io/github/issues/BetaF1sh/jejunuMeals.svg?style=flat-square)](https://github.com/BetaF1sh/jejunuMeals/issues)

제주대학교 학식 조회 모듈

Lookup meals data for [Jeju National University](http://www.jejunu.ac.kr/camp/stud/foodmenu).

## Install

```bash
$ pip install jejunuMeals
```

## Usage

```python
>>> from jejunuMeals import JejunuMeals
>>> from pprint import pprint
>>> pprint(JejunuMeals().menus())
{0: {'저녁': {'양식': '없음',
            '정식': '보리밥\n북어콩나물국\n돼지고기두루치기(pork)\n돌자반김볶음\n김치',
            '중식': '없음',
            '특식': '없음'},
     '점심': {'양식': '없음',
            '정식': '베이컨야채볶음밥\n무된장국\n쫄면야채무침\n김치',
            '중식': '없음',
            '특식': '보리밥\n우거지갈비탕(beef)\n멕시칸샐러드\n감자꽈리고추조림\n톳무침\n김치'}},
 1: {'저녁': {'양식': '없음',
            '정식': '보리밥\n북어콩나물국\n돼지고기두루치기(pork)\n돌자반김볶음\n김치',
            '중식': '없음',
            '특식': '없음'},
     '점심': {'양식': '없음',
            '정식': '베이컨야채볶음밥\n무된장국\n쫄면야채무침\n김치',
            '중식': '없음',
            '특식': '보리밥\n우거지갈비탕(beef)\n멕시칸샐러드\n감자꽈리고추조림\n톳무침\n김치'}},
 2: {'저녁': {'양식': '없음',
            '정식': '보리밥\n북어콩나물국\n돼지고기두루치기(pork)\n돌자반김볶음\n김치',
            '중식': '없음',
            '특식': '없음'},
     '점심': {'양식': '없음',
            '정식': '베이컨야채볶음밥\n무된장국\n쫄면야채무침\n김치',
            '중식': '없음',
            '특식': '보리밥\n우거지갈비탕(beef)\n멕시칸샐러드\n감자꽈리고추조림\n톳무침\n김치'}},
 3: {'저녁': {'양식': '없음',
            '정식': '보리밥\n북어콩나물국\n돼지고기두루치기(pork)\n돌자반김볶음\n김치',
            '중식': '없음',
            '특식': '없음'},
     '점심': {'양식': '없음',
            '정식': '베이컨야채볶음밥\n무된장국\n쫄면야채무침\n김치',
            '중식': '없음',
            '특식': '보리밥\n우거지갈비탕(beef)\n멕시칸샐러드\n감자꽈리고추조림\n톳무침\n김치'}},
 4: {'저녁': {'양식': '없음',
            '정식': '보리밥\n북어콩나물국\n돼지고기두루치기(pork)\n돌자반김볶음\n김치',
            '중식': '없음',
            '특식': '없음'},
     '점심': {'양식': '없음',
            '정식': '베이컨야채볶음밥\n무된장국\n쫄면야채무침\n김치',
            '중식': '없음',
            '특식': '보리밥\n우거지갈비탕(beef)\n멕시칸샐러드\n감자꽈리고추조림\n톳무침\n김치'}}}
{'저녁': {'양식': '없음',
        '정식': '보리밥\n북어콩나물국\n돼지고기두루치기(pork)\n돌자반김볶음\n김치',
        '중식': '없음',
        '특식': '없음'},
 '점심': {'양식': '없음',
        '정식': '베이컨야채볶음밥\n무된장국\n쫄면야채무침\n김치',
        '중식': '없음',
        '특식': '보리밥\n우거지갈비탕(beef)\n멕시칸샐러드\n감자꽈리고추조림\n톳무침\n김치'}}
```

## API

### `JejunuMeals().menus()`

Fetch meal data of specific weekday.

```python
>>> from jejunuMeals import JejunuMeals
>>> from datetime import date
>>> from pprint import pprint
>>> pprint(JejunuMeals().menus(date.today().weekday()))
{'저녁': {'양식': '없음',
            '정식': '보리밥\n북어콩나물국\n돼지고기두루치기(pork)\n돌자반김볶음\n김치',
            '중식': '없음',
            '특식': '없음'},
     '점심': {'양식': '없음',
            '정식': '베이컨야채볶음밥\n무된장국\n쫄면야채무침\n김치',
            '중식': '없음',
            '특식': '보리밥\n우거지갈비탕(beef)\n멕시칸샐러드\n감자꽈리고추조림\n톳무침\n김치'
}}
```

#### Parameter (optional)

The weekday on which you want to fetch meal data.

This value only valid in between 0 and 4. if empty or greater than 4, return all menus.

### `JejunuMeals().daily()`

Just an alias of `JejunuMeals().menus()`

## Save to yaml

You shoud install before `pip install pyYaml`

```python
import yaml

noalias = yaml.dumper.SafeDumper
noalias.ignore_aliases = lambda self, data: True

with open('output.yaml', 'w') as outfile:
    yaml.dump(JejunuMeals().menus(), outfile, default_flow_style=False, allow_unicode=True, Dumper=noalias)
```

_jejunuMeals_ is primarily distributed under the terms of the [GNU Affero General Public License v3.0](./LICENSE) or any later version. See [COPYRIGHT](./COPYRIGHT) for details.

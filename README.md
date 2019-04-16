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
{0: {'저녁': {'양식': ['없음'],
            '정식': ['검정쌀밥', '얼큰열무국', '돼지고기야채볶음(pork)', '오이된장무침', '김치'],
            '중식': ['없음'],
            '특식': ['없음']},
     '점심': {'양식': ['치즈오븐스파게티'],
            '정식': ['베이컨야채볶음밥(pork)', '달걀파국', '볶음우동', '김치'],
            '중식': ['없음'],
            '특식': ['검정쌀밥',
                   '쇠고기된장찌개(beef)',
                   '순살양념치킨(chicken)',
                   '양배추사과샐러드',
                   '콩나물무숙채',
                   '김치']}},
 1: {'저녁': {'양식': ['없음'],
            '정식': ['쌀밥', '어묵탕', '쇠고기야채볶음(beef)', '톳무침', '김치'],
            '중식': ['없음'],
            '특식': ['없음']},
     '점심': {'양식': ['등심돈가스(pork)/스프', '양배추샐러드', '단무지/김치'],
            '정식': ['에그스크램블볶음밥', '무된장국', '별미떡볶음', '김치'],
            '중식': ['없음'],
            '특식': ['보리밥', '돼지갈비찜(pork)', '무된장국', '편마늘멸치볶음', '브로콜리맛살무침', '김치']}},
 2: {'저녁': {'양식': ['없음'],
            '정식': ['차조밥', '김치찌개(pork)', '생선가스/타타르소스', '깻잎순무침', '김치'],
            '중식': ['없음'],
            '특식': ['없음']},
     '점심': {'양식': ['크림파스타'],
            '정식': ['닭가슴살카레라이스(chicken)', '취나물된장국', '아몬드쥐치채볶음', '김치'],
            '중식': ['없음'],
            '특식': ['비빔밥/약고추장(pork)', '취나물된장국', '어묵볶음', '오이생채', '김치', '요구르트']}},
 3: {'저녁': {'양식': ['없음'],
            '정식': ['쌀밥', '김치콩나물국', '닭고기떡조림(chicken)', '옛날소시지전', '김치'],
            '중식': ['없음'],
            '특식': ['없음']},
     '점심': {'양식': ['치즈오븐스파게티'],
            '정식': ['제육덮밥(pork)', '유채된장국', '부추양파겉절이', '김치'],
            '중식': ['없음'],
            '특식': ['현미밥', '해물순두부뚝배기', '순대야채볶음', '피망잡채(beef)', '무말랭이무침', '김치']}},
 4: {'저녁': {'양식': ['없음'],
            '정식': ['혼합잡곡밥', '동태찌개', '돼지고기두루치기(pork)', '유채나물무침', '김치'],
            '중식': ['없음'],
            '특식': ['없음']}
```

## API

### `JejunuMeals().menus()`

Fetch meal data of specific weekday.

```python
>>> from jejunuMeals import JejunuMeals
>>> from datetime import date
>>> from pprint import pprint
>>> pprint(JejunuMeals().menus(date.today().weekday()))
{'저녁': {'양식': ['없음'],
        '정식': ['쌀밥', '어묵탕', '쇠고기야채볶음(beef)', '톳무침', '김치'],
        '중식': ['없음'],
        '특식': ['없음']},
 '점심': {'양식': ['등심돈가스(pork)/스프', '양배추샐러드', '단무지/김치'],
        '정식': ['에그스크램블볶음밥', '무된장국', '별미떡볶음', '김치'],
        '중식': ['없음'],
        '특식': ['보리밥', '돼지갈비찜(pork)', '무된장국', '편마늘멸치볶음', '브로콜리맛살무침', '김치']}}
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

---

_jejunuMeals_ is primarily distributed under the terms of the [MIT license](<(./LICENSE)>).

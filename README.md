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
            '정식': '현미밥\n멸치된장찌개\n돼지고기야채볶음(pork)\n톳무침\n김치',
            '중식': '없음',
            '특식': '없음'},
     '점심': {'양식': '없음',
            '정식': '마파두부덮밥(pork)\n달걀파국\n오이생채\n김치',
            '중식': '없음',
            '특식': '현미밥\n설렁탕(beef)\n씨리얼과일샐러드\n오징어포아몬드볶음\n콩나물무침\n김치'}},
 1: {'저녁': {'양식': '없음',
            '정식': '쌀밥\n순두부찌개(pork)\n안동찜닭(chicken)\n취나물무침\n김치',
            '중식': '없음',
            '특식': '없음'},
     '점심': {'양식': '없음',
            '정식': '닭가슴살카레라이스(chicken)\n배추된장국\n어묵채볶음\n김치',
            '중식': '없음',
            '특식': '보리밥\n불고기백반(pork)\n배추된장국\n꽈리고추멸치볶음\n무생채\n상추,깻잎/쌈\n김치'}},
 2: {'저녁': {'양식': '없음',
            '정식': '검정쌀밥\n쇠고기미역국(beef)\n섭산적데리야끼구이\n참나물사과초무침\n김치',
            '중식': '없음',
            '특식': '없음'},
     '점심': {'양식': '없음',
            '정식': '에그스크램블볶음밥\n무된장국\n자장떡볶음\n김치',
            '중식': '없음',
            '특식': '검정쌀밥\n뚝배기김치찌개(pork)\n생선가스/소스\n숙주삼색나물\n오이된장무침\n김치'}},
 3: {'저녁': {'양식': '없음',
            '정식': '쌀밥\n배추된장국\n쇠고기떡볶음(beef)\n무말랭이무침\n김치',
            '중식': '없음',
            '특식': '없음'},
     '점심': {'양식': '없음',
            '정식': '참치마요덮밥\n미소장국\n매운콩나물무침\n김치',
            '중식': '없음',
            '특식': '차조밥\n해물뚝배기\n탕수육(pork)\n쫄면야채무침\n유채나물무침\n김치'}},
 4: {'저녁': {'양식': '없음',
            '정식': '혼합잡곡밥\n순댓국(pork)\n어묵맛살초무침\n달걀야채말이\n김치',
            '중식': '없음',
            '특식': '없음'},
     '점심': {'양식': '없음',
            '정식': '소불고기덮밥(beef)\n열무된장국\n미역양파초무침\n김치',
            '중식': '없음',
            '특식': '혼합잡곡밥\n사골우거지해장국(beef)\n제육두부김치(pork)\n브로콜리맛살무침\n도라지무생채\n김치'}}}
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

---

_jejunuMeals_ is primarily distributed under the terms of the [MIT license]((./LICENSE)).

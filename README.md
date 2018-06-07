# jejunuMeals

Jeju National University meal data crawler

## Install

```bash
$ pip install jejunuMeals
```

## How to use

```python
>>> from jejunuMeals import JejunuMeals
>>> from pprint import pprint
>>> meals = JejunuMeals().fetch_meals()
>>> pprint(meals) # 0 ~ 4 : mon ~ fir
{0: {'저녁': {'양식': '\n없음\n',
            '정식': '\n검정쌀밥\n꽃게탕\n닭고기떡조림(chicken)\n유채나물무침\n김치\n',
            '중식': '\n없음\n',
            '특식': '\n없음\n'},
     '점심': {'양식': '\n없음\n',
            '정식': '\n마파두부덮밥(pork)\n무된장국\n비빔만두\n김치\n',
            '중식': '\n삼계탕\n양파장아찌\n김치\n',
            '특식': '\n검정쌀밥\n돼지갈비찜(pork)\n무된장국\n꽈리고추멸치볶음\n오이된장무침\n김치\n'}},
 1: {'저녁': {'양식': '\n없음\n',
            '정식': '\n쌀밥\n북어콩나물국\n돼지고기야채볶음(pork)\n시금치들깨무침\n김치\n',
            '중식': '\n없음\n',
            '특식': '\n없음\n'},
     '점심': {'양식': '\n없음\n',
            '정식': '\n김치볶음밥(pork)\n취나물된장국\n자장떡볶음\n김치\n',
            '중식': '\n삼계탕\n양파장아찌\n김치\n',
            '특식': '\n현미밥\n해물순두부뚝배기\n닭오븐구이(chicken)\n고춧잎무침\n미역양파초무침\n김치\n'}},
 2: {'저녁': {'양식': '\n없음\n', '정식': '\n없음\n', '중식': '\n없음\n', '특식': '\n없음\n'},
     '점심': {'양식': '\n없음\n',
            '정식': '\n현    충    일\n',
            '중식': '\n없음\n',
            '특식': '\n없음\n'}},
 3: {'저녁': {'양식': '\n없음\n',
            '정식': '\n쌀밥\n어묵탕\n쇠고기야채볶음(beef)\n톳무침\n김치\n',
            '중식': '\n없음\n',
            '특식': '\n없음\n'},
     '점심': {'양식': '\n없음\n',
            '정식': '\n닭갈비덮밥(chicken)\n배추된장국\n쥐치채볶음\n김치\n',
            '중식': '\n삼계탕\n양파장아찌\n김치\n',
            '특식': '\n보리밥\n돼지고기수육(pork)\n배추된장국\n양파겨자소스\n콩나물무침\n상추,깻잎/쌈\n김치\n'}},
 4: {'저녁': {'양식': '\n없음\n',
            '정식': '\n차조밥\n참치김치찌개\n돼지고기모듬장조림(pork)\n열무된장무침\n김치\n',
            '중식': '\n없음\n',
            '특식': '\n없음\n'},
     '점심': {'양식': '\n없음\n',
            '정식': '\n베이컨야채볶음밥\n달걀파국\n쫄면야채무침\n김치\n',
            '중식': '\n삼계탕\n양파장아찌\n김치\n',
            '특식': '\n차조밥\n쇠고기된장뚝배기(beef)\n과일야채샐러드\n우엉채볶음\n동초나물무침\n김치\n'}}}
>>> import yaml # You can also save as `.yaml` (using pyYaml)
>>> with open('output.yaml', 'w') as outfile:
...     yaml.dump(meals, outfile, default_flow_style=False, allow_unicode=True)
```

_jejunuMeals_ is primarily distributed under the terms of the [GNU Affero General Public License v3.0](./LICENSE) or any later version. See [COPYRIGHT](./COPYRIGHT) for details.
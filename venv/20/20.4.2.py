import json

ch = {}
with open('json_example_QAP.json', 'r', encoding='utf8') as f:
    asns = json.load(f)

with open('list_of_checks.txt', 'r', encoding='utf8') as f:
    for i in f.readlines():
        i = i.split(':')
        ch[i[0].strip()] = i[1].strip()


def checks(obj, file):
    count = 0
    for i in obj:
        count += 1
        test = 'Pass'
        if len(i) != len(file):
            print(f'Ответ {count}: количество строк ответа {len(i)}, должно быть {len(file)}!')
            test = 'Failed'
        for key, value in file.items():
            if key not in i.keys():
                print(f'Поля {key} нет в ответе')
                test = 'Failed'
            if key == 'eventType':
                if not (i[key] == 'itemBuyEvent' or i[key] == 'itemViewEvent'):
                    print(f'Ответ {count}, строка {key} не содержит itemBuyEvent или itemViewEvent')
                    test = 'Failed'
            if value == 'int':
                if not type(i[key]) == int:
                    print(f'Ответ {count}, строка {key} состоит не только из цифр')
                    test = 'Failed'
                continue
            if value == 'bool':
                if not type(i[key]) == bool:
                    print(f'Ответ {count}, строка {key} не содержит Булево значение')
                    test = 'Failed'
                continue
            if 'string' in value:
                if 'url' in value:
                    if not (i[key].startswith('http://') or i[key].startswith('https://')):
                        print(f'Ответ {count}, строка {key} не содержит ссылку')
                        test = 'Failed'
                if not type(i[key]) == str:
                    print(f'Ответ {count}, строка {key} не содержит строку')
                    test = 'Failed'
        print('Test -', test)


checks(asns, ch)

import json

#Открытие json файлов
with open('actual.json', 'r') as file:
    actual = json.load(file)
with open('memorized.json', 'r') as file:
    memorized = json.load(file)

#Сортировка словарей
actual['prime_drops'] = sorted(actual['prime_drops'])
memorized['prime_drops'] = sorted(memorized['prime_drops'])

#Сравнение prime_drops
if not actual['prime_drops'] == memorized['prime_drops']:
    for mem in memorized['prime_drops']:
        if not mem in actual['prime_drops']:
            print (mem, 'пропал из списка prime_drops')
            break
    for act in actual['prime_drops']:
        if not act in memorized['prime_drops']:
            print (act, 'появился в списке prime_drops')
            break
else:
    print ('Список prime_drops остался без изменений')

#Сравнение rare_drops
actual['rare_drops'] = sorted(actual['rare_drops'])
memorized['rare_drops'] = sorted(memorized['rare_drops'])
if not actual['rare_drops'] == memorized['rare_drops']:
    for mem in memorized['rare_drops']:
        if not mem in actual['rare_drops']:
            print (mem, 'пропал из списка rare_drops')
            break
    for act in actual['rare_drops']:
        if not act in memorized['rare_drops']:
            print (act, 'появился в списке rare_drops')
            break
else:
    print ('Список rare_drops остался без изменений')

#Сравнение discontinued_drops
actual['discontinued_drops'] = sorted(actual['discontinued_drops'])
memorized['discontinued_drops'] = sorted(memorized['discontinued_drops'])
if not actual['discontinued_drops'] == memorized['discontinued_drops']:
    for mem in memorized['discontinued_drops']:
        if not mem in actual['discontinued_drops']:
            print (mem, 'пропал из списка discontinued_drops')
            break
    for act in actual['discontinued_drops']:
        if not act in memorized['discontinued_drops']:
            print (act, 'появился в списке discontinued_drops')
            break
else:
    print ('Список discontinued_drops остался без изменений')

#Перезапись memorized.json если произошли изменения
if not actual == memorized:
    with open('memorized.json', 'w') as file:
        json.dump(actual, file, indent=1)

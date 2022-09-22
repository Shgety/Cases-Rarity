from genericpath import isfile
import requests
import json
from bs4 import BeautifulSoup as BS
import schedule
import time
import logging

def notify():
    try:
        #https запрос
        r = requests.get("https://www.csgodatabase.com/cases/")
        html = BS(r.content, 'html.parser')

        #Парсинг страницы
        el = html.find("h3", text="Prime Drops").find_next_sibling().find_next_sibling(
        ).find_next_sibling().find_next_sibling().find_next_sibling()
        for item in el:
            item = el.find_all(class_="item-box-header")
        prime_drops = []
        for each in item:
            prime_drops.append(each.text)
        el = html.find("h3", text="Rare Cases").find_next_sibling(
        ).find_next_sibling().find_next_sibling().find_next_sibling()
        for item in el:
            item = el.find_all(class_="item-box-header")
        rare_drops = []
        for each in item:
            rare_drops.append(each.text)
        el = html.find("h3", text="Discontinued Cases").find_next_sibling(
        ).find_next_sibling().find_next_sibling().find_next_sibling()
        for item in el:
            item = el.find_all(class_="item-box-header")
        discountinued_drops = []
        for each in item:
            discountinued_drops.append(each.text)

        #Запись в json файл
        d = {
            "prime_drops": prime_drops,
            "rare_drops": rare_drops,
            "discontinued_drops": discountinued_drops
        }
        with open('actual.json', 'w') as file:
            json.dump(d, file, indent=1)
        if not isfile('memorized.json'):
            with open('memorized.json', 'w') as file:
                json.dump(d, file, indent=1)

        #Открытие json файлов
        with open('actual.json', 'r') as file:
            actual = json.load(file)
        with open('memorized.json', 'r') as file:
            memorized = json.load(file)
        message = ''

        #Сортировка словарей
        actual['prime_drops'] = sorted(actual['prime_drops'])
        memorized['prime_drops'] = sorted(memorized['prime_drops'])

        #Сравнение prime_drops
        if not actual['prime_drops'] == memorized['prime_drops']:
            for mem in memorized['prime_drops']:
                if not mem in actual['prime_drops']:
                    message = message + mem + ' пропал из списка prime_drops\n'
                    break
            for act in actual['prime_drops']:
                if not act in memorized['prime_drops']:
                    message = message + act + ' появился в списке prime_drops\n'
                    break
        else:
            print ('Список prime_drops остался без изменений')

        #Сравнение rare_drops
        actual['rare_drops'] = sorted(actual['rare_drops'])
        memorized['rare_drops'] = sorted(memorized['rare_drops'])
        if not actual['rare_drops'] == memorized['rare_drops']:
            for mem in memorized['rare_drops']:
                if not mem in actual['rare_drops']:
                    message = message + mem + ' пропал из списка rare_drops\n'
                    break
            for act in actual['rare_drops']:
                if not act in memorized['rare_drops']:
                    message = message + act + ' появился в списке rare_drops\n'
                    break
        else:
            print ('Список rare_drops остался без изменений')

        #Сравнение discontinued_drops
        actual['discontinued_drops'] = sorted(actual['discontinued_drops'])
        memorized['discontinued_drops'] = sorted(memorized['discontinued_drops'])
        if not actual['discontinued_drops'] == memorized['discontinued_drops']:
            for mem in memorized['discontinued_drops']:
                if not mem in actual['discontinued_drops']:
                    message = message + mem + ' пропал из списка discontinued_drops\n'
                    break
            for act in actual['discontinued_drops']:
                if not act in memorized['discontinued_drops']:
                    message = message + act + ' появился в списке discontinued_drops\n'
                    break
        else:
            print ('Список discontinued_drops остался без изменений')

        #Перезапись memorized.json если произошли изменения
        if not actual == memorized:
            with open('memorized.json', 'w') as file:
                json.dump(actual, file, indent=1)
        if message != '':
            print(message)
    except Exception as e:
        logging.error(f'Unknown error occured: {e}')

if (__name__ == '__main__'):
    #schedule.every().day.at("21:00").do(notify)
    notify()
    # while (True):
    #     schedule.run_pending()
    #     time.sleep(1)
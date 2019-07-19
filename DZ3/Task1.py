# 1. Напишите функцию получения IATA-кода города из его названия,
# используя API Aviasales для усовершенствования приложения по парсингу информации об авиабилетах, созданного нами в ходе урока.
# Примечание: воспользуйтесь документацией по API, которая доступна на странице www.aviasales.ru/API
# (ссылка на значке «API-документация»).
# Вам необходимо изучить раздел «API для определения IATA-кода».

import requests
import json

# Напишем функцию, которая используя запрос из API
def get_iata(orig,dest):
    link_IATA = f'https://www.travelpayouts.com/widgets_suggest_params?q=Из%20{orig}%20в%20{dest}'
    return json.loads(requests.get(link_IATA).text)


origin = input('Введите город отправления ')
destination = input('Введите город прибытия ')
iata_origin = get_iata(origin, destination)['origin']['iata']
iata_destination = get_iata(origin, destination)['destination']['iata']
print(f'IATA города отправления {iata_origin}')
print(f'IATA города назначения {iata_destination}')


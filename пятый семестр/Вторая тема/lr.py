"""

Написать реализацию функции get_weather_data(place, api_key=None), в которой необходимо получить данные о погоде с сайта https://openweathermap.org/.

Функция должна возвращать объект в формате JSON, включающий:

информацию о названии города (в контексте openweathermap),
код страны (2 символа),
широту и долготу, на которой он находится,
его временной зоне,
а также о значении температуры (как она ощущается).
Значение временной зоны выводить в формате UTC±N, где N - цифра временного сдвига. Протестировать выполнение программы со следующими городами: Чикаго, СПб, Дакка.

Пример вызова функции и получаемого результата.

get_weather_data('Kiev', api_key=key)
>>> {"name": "Kyiv", "coord": {"lon": 30.52, "lat": 50.43}, "country": "UA", "feels_like": 21.96, "timezone": "UTC+3"}
При реализации программы, не публикуйте свой ключ для осуществления запросов. Сразу же после создания репозитория в классруме исключите из коммитов подключаемый файл, где разместите ключ, с помощью .gitignore. Для организации за

"""

import requests
import json
def get_weather_data(place, api_key=None):
    try:
        url = "http://api.openweathermap.org/data/2.5/weather?q="+ place +"&appid=" + api_key
    except TypeError:
        return None
    response = requests.get(url)
    dict_weather = json.loads(response.text)

    todelete = ('weather', 'base', 'visibility', 'wind', 'clouds', 'dt', 'id', 'cod')
    for i in todelete:
        dict_weather.pop(i, None)
    try:
        value_temp = dict_weather['main'].pop('feels_like')
        dict_weather.pop('main')
        dict_weather['feels_like'] = value_temp
    except KeyError:
        return None

    value_id = dict_weather['sys'].pop('id')
    value_country = dict_weather['sys'].pop('country')
    dict_weather.pop('sys')
    dict_weather['id'] = value_id
    dict_weather['country'] = value_country

    timezn = int(dict_weather['timezone'] / 3600)
    if (timezn > 0):
        dict_weather['timezone'] = 'UTC+' + str(timezn)
    else:
        dict_weather['timezone'] = 'UTC' + str(timezn)

    json_weather = json.dumps(dict_weather)
    return json_weather

if __name__ == "__main__":
    assert get_weather_data("Saint Petersburg") is None
    assert get_weather_data('') is None
    assert type(json.loads(get_weather_data('Chicago', api_key=key)).get('id')) is int
    assert type(get_weather_data("Dhaka",api_key=key)) is str

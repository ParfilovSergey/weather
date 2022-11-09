import requests

city = "Moscow,RU"
appid = "5f90996e12146e1a6fd86b5087ce1ddf"
res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                   params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Прогноз скорости ветра и видимости на сегодня")
print('Cкорость ветра: ', data['wind']['speed'], ' м/с')
print("Видимость: ", (data['visibility'] / 10000) * 100, '%')
print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')

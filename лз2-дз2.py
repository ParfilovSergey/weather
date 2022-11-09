import requests


city = "Moscow,RU"
appid = "5f90996e12146e1a6fd86b5087ce1ddf"
res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                   params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data=res.json()
print("Прогноз скорости ветра и видимости")
for i in data["list"]:
    print("Дата: ", i['dt_txt'],
    "\r\n Скорость ветра: ", i['wind']['speed'], ' м/с',
    "\r\n Видимость: ", round((i['visibility'] / 10000)*100), '%')
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
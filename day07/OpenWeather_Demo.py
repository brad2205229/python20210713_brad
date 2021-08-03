import json
import requests
import datetime
key = "fe97b9427ed1fe46a19823f66c2f8c6d"
q = 'taoyuan,tw'
url = 'https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s' % (q, key)
print(url)
# description, temp, feels_like, humidity
# 1. 抓取文字資料
data = requests.get(url).text
# 2. 將文字資料轉成 json 物件(會進行結構化 dict), 目的:便於日後分析
weather = json.loads(data)
# 3. 分析資料
description = weather['weather'][0]['description']
temp = weather['main']['temp'] - 273.15
feels_like = weather['main']['feels_like'] -273.15
humidity = weather['main']['humidity']
dt = weather['dt']
print(datetime.datetime.fromtimestamp(dt))
print("地區: %s" % q)
print("天氣概述: %s" % description)
print("溫度(度C): %.2f" %temp)
print("體感(度C): %.2f" % feels_like)
print("濕度(%%): %d" % humidity)
# 4. 取得 icon
icon = weather['weather'][0]['icon']
print("icon: %s" % icon)
icon_url = 'https://openweathermap.org/img/wn/%s@4x.png' % icon
icon_data = requests.get(icon_url).content  # 非文字檔用 content
print(icon_data)
# 5. 將 icon 存成 png 檔案
file = open('weather_icon.png', 'wb')
file.write(icon_data)

import json
import day07.Util as u
file = open('桃園公共自行車即時服務資料.json', 'r', encoding='utf-8')
data = file.read()
youbike = json.loads(data)
# print(youbike)
no = 2002
sno = str(no)
try:
    print(youbike['retVal'][sno])
    print(youbike['retVal'][sno]['sna'])
    print(youbike['retVal'][sno]['tot'])
    print(youbike['retVal'][sno]['sbi'])
    print(youbike['retVal'][sno]['bemp'])
    print(youbike['retVal'][sno]['lat'])
    print(youbike['retVal'][sno]['lng'])
except:
    print('無此站台: %s' % sno)
# 我所在地的經緯度 24.987801467472433, 121.29437443431674
print(u.distance(24.987801467472433, 121.29437443431674, 24.968128, 121.194666))
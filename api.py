import requests  #直接用alt+enter安裝套件
from data import Location, WeatherElement
url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/O-A0003-001?Authorization=rdec-key-123-45678-011121314'
html_content = requests.get(url)    #向html提出get請求

json_content = html_content.json()    #將內容轉為json
print(json_content)

#取得測站資料
records = json_content.get('records')
location = records.get('location') #從location裡面拿取資料

#取得欄位資料，location是list，解析這個資料
allLocactions = []
for l in location:  #跑location裡面的資料，會得出dictionary資料
    a = Location()
    a.from_json(l)

    weather_element_json = l.get('weatherElement')
    element = WeatherElement()
    element.from_json(weather_element_json)
    a.weather_element = element
    
    allLocactions.append(a)

    #lat = l.get('lat')
    #lon = l.get('lon')
    #locationName = l.get('locationName')
    #stationId = l.get('stationId')
    #time = l.get('time').get('obsTime')
    #print(locationName, stationId, time)

    # a = Location()
    # a.from_json(l)
    # print(a.__dict__)

#取得觀測資料，weatherElement是list
# weatherElement = l.get('weatherElement')
# for element in weatherElement:
#     elementName = element.get('elementName')
#     elementValue = element.get('elementValue')
#     print(elementName, elementValue)





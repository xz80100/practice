class Location:
    def __init__(self, location_name=None, lat=None, lon=None, station_id=None, time=None, weather_element=None):

        self.location_name = location_name
        self.lat = lat
        self.lon = lon
        self.stationId = station_id
        self.time = time


    def from_json(self, json_data):

        self.location_name = json_data.get('locationName')
        self.lat = json_data.get('lat')
        self.lon = json_data.get('lon')
        self.stationId = json_data.get('stationId')
        self.time = json_data.get('time').get('obsTime')

        self.weatherElement = WeatherElement()
        self.weatherElement.from_json(json_data['weatherElement'])


        weather_element_json = json_data.get('weather_element')
        element = WeatherElement()
        element.from_json(weather_element_json)
        self.weatherelement = element

class WeatherElement:
    def __init__(self, wdir=None, wdsd=None, temp=None, humd=None, h_24r=None):
        self.wdir = wdir
        self.wdsd = wdsd
        self.temp = temp
        self.humd = humd
        self.h_24r = h_24r

    def from_json(self, weather_element):
        for element in weather_element:
            element_name = element.get('elementName')
            element_value = element.get('elementValue')

            if element_name == 'WDIR':
                self.wdir = element_value

            if element_name == 'WDSD':
                self.wdsd = element_value

            if element_name == 'TEMP':
                self.temp = element_value

            if element_name == 'HUMD':
                self.humd = element_value

            if element_name == '24R':
                self.h_24r = element_value
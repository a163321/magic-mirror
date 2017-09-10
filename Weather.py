import sys
from bs4 import BeautifulSoup
import requests

class Weather():
    def __init__(self,city):
        self.key = '7a4ee67b8d1747f39fbd3914b5e6e6cd'
        # self.url = 'http://apis.baidu.com/heweather/pro/weather?city='+city
        self.url = 'https://free-api.heweather.com/v5/weather'
        self.payload = {'city':city,'key':self.key}

    def getWeather(self):
        content = requests.get(self.url,params=self.payload)
        if(content):
            return content.json()


if __name__=='__main__':
    print(Weather('beijing').getWeather())
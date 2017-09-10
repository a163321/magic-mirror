from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.uix.image import Image
import time
import Weather  # 查看天气
import json


class RootWidget(BoxLayout):
    '''This the class representing your root widget.
       By default it is inherited from BoxLayout,
       you can use any other layout/widget depending on your usage.
    '''
    pass


class MainApp(App):
    '''This is the main class of your app.
       Define any app wide entities here.
       This class can be accessed anywhere inside the kivy app as,
       in python::

         app = App.get_running_app()
         print (app.title)

       in kv language::

         on_release: print(app.title)
       Name of the .kv file that is auto-loaded is derived from the name
       of this class::

         MainApp = main.kv
         MainClass = mainclass.kv

       The App part is auto removed and the whole name is lowercased.
    '''

    def build(self):
        '''Your app will be build from here.
           Return your root widget here.
        '''
        return RootWidget()

    def on_pause(self):
        '''This is necessary to allow your app to be paused on mobile os.
           refer http://kivy.org/docs/api-kivy.app.html#pause-mode .
        '''
        return True

    sw_seconds = 0

    def update_time(self, dt):
        self.root.ids.label_time.text = time.strftime(
            "[b]%H:%M:%S[/b]", time.localtime())

    def update_weather(self):
        # 基本天气
        weather = Weather.Weather('beijing').getWeather()['HeWeather5']
        city = weather[0]['basic']['city']
        cond = weather[0]['now']['cond']['txt']
        tmp = weather[0]['now']['tmp'] + '℃'

        # 空气指数
        aqi = weather[0]['aqi']['city']['aqi']
        qlty = weather[0]['aqi']['city']['qlty']
        pm25 = weather[0]['aqi']['city']['pm25']

        # 生活指数
        cw_brf = weather[0]['suggestion']['cw']['brf']
        cw_txt = weather[0]['suggestion']['cw']['txt']
        drsg_brf = weather[0]['suggestion']['drsg']['brf']
        drsg_txt = weather[0]['suggestion']['drsg']['txt']

        # print(type(weather[0]['daily_forecast']['tmp']['max']))
        # print(weather)
        self.root.ids.label_weather1.text = city + ' ' + cond + ' ' + tmp
        self.root.ids.label_weather2.text = '空气指数 : ' + \
            aqi + '\n空气质量 : ' + qlty + '\npm25浓度 : ' + pm25
        self.root.ids.label_weather3.text = '人体感觉 : ' + drsg_brf + '\n穿衣指数 : ' + drsg_txt
        # self.root.ids.image_weather.source='/data/images/100.png'

    def update_info(self):
        self.root.ids.lable_info.text = u'帅哥，今天你看起来很开心，需要来首歌吗'

    def on_start(self):
        Clock.schedule_interval(self.update_time, 1)
        Clock.schedule_once(lambda dt: self.update_weather(), 1)
        Clock.schedule_once(lambda dt: self.update_info(), 1)


if __name__ == '__main__':
    MainApp().run()

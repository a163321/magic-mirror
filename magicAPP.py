#-*- coding:utf-8 -*-
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.core.text import Label
from os import listdir

Builder.load_string('''
<OneScreen>
    Button:
        text:u'点击我'
        font_name: 'DroidSansFallback.ttf'
        on_release:print(root.__class__)
''')

class OneScreen(Screen):
    pass

class magicApp(App):
    def build(self):
        return OneScreen()


magicApp().run()
import requests
import json
import yuyin
import asyncio
from concurrent.futures import ThreadPoolExecutor


class Tuling():
    def __init__(self):
        self.APIkey = 'ea234bc1784e4bbe9032da2a03178678'
        self.APIurl = 'http://www.tuling123.com/openapi/api'

    def get_data(self, text):
        inputText = {text}
        key = self.APIkey
        data = {'info': inputText, 'key': key}
        print(data)
        return data

    def get_answer(self, text):
        data = self.get_data(text)
        response = requests.post(url=self.APIurl, data=data)
        result = response.json()
        answer = result['text']
        return answer


def test():
    while True:
        yy = yuyin.Baiduyuyin()
        print('获取语音数据')
        s = yy.asr('record.wav')['result'][0]
        print(s)
        a = Tuling().get_answer(s)
        print(a)
        print("等待")

if __name__ == '__main__':
    # 获取EventLoop
    loop = asyncio.get_event_loop()
    # 执行coroutine
    loop.run_until_complete(test())
    loop.close()

    # s = input()
    # print(Tuling().get_answer(s))

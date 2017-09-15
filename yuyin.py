# -*- coding: utf-8 -*-
from aip import AipSpeech
import asyncio

# 定义常量
APP_ID = '9941234'
API_KEY = 'fj6jDe6824qj4tvYggQF1ifg'
SECRET_KEY = '967fc3fff9acc9db2d2cf8e2f6b0c02b'


# 读取文件

class Baiduyuyin():
    def __init__(self):
        # 初始化AipSpeech对象
        self.aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    async def asr(self, filename):
        r = self.aipSpeech.asr(self.get_file_content(
            filename), 'wav', 16000, {'lan': 'zh', })
        return r

    def get_file_content(self, filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    def synthesis(self, text):
        result = self.aipSpeech.synthesis(
            text, 'zh', 1, {'vol': 6, 'pit': 5, 'per': 3, 'spd': 4})

        if not isinstance(result, dict):
            with open('auido.mp3', 'wb') as f:
                f.write(result)

if __name__ == '__main__':
    print(Baiduyuyin().asr('record.wav'))
    
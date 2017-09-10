# -*- coding: utf-8 -*-
from aip import AipSpeech


# 定义常量
APP_ID = '9941234'
API_KEY = 'fj6jDe6824qj4tvYggQF1ifg'
SECRET_KEY = '967fc3fff9acc9db2d2cf8e2f6b0c02b'


# 初始化AipSpeech对象
aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 读取文件


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

r=aipSpeech.asr(get_file_content('record.wav'), 'wav', 16000, {
    'lan': 'zh',
})

print(r)
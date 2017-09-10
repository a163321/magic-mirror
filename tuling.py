import requests
import json


class Tuling():
    def __init__(self):
        self.APIkey = 'ea234bc1784e4bbe9032da2a03178678'
        self.APIurl = 'http://www.tuling123.com/openapi/api'

    def get_data(self, text):
        userId = '12345'
        inputText = {'Text', text}
        key = self.APIkey
        data = {'info': inputText, 'userid': userId, 'key': key}
        print(data)
        return data

    def get_answer(self, text):
        data = self.get_data(text)
        response = requests.post(url=self.APIurl, data=data)
        result = response.json()
        answer = result['text']
        return answer


if __name__ == '__main__':
    while 1:
        s = input()
        print(Tuling().get_answer(s))

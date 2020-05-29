import requests
import json

class DataUsers():

    __slots__ = [
        '_user',
        '_repo'
    ]
    def __init__(self, user=''):
        self.user = user
        self._repo = {}

    @property
    def user(self):
        return self._user
    
    @user.setter
    def user(self, user=''):
        self._user = user 

    def request_repo_api(self):
        resposta = requests.get(
            f'https://api.github.com/users/{self._user}/repos'
        )
        if resposta.status_code == 200:
            return resposta.json()
        else:
            return resposta.status_code

    def recebe_repo(self):
        dados_api = self.request_repo_api()
        if type(dados_api) is not int:
            for i in range(len(dados_api)):
                self._repo['name'] = dados_api[i]['name']
                self._repo['full_name'] = dados_api[i]['full_name']
                self._repo['description'] = dados_api[i]['description']
                self._repo['language'] = dados_api[i]['language']
                self._repo['create'] = dados_api[i]['created_at']
                self._repo['update'] = dados_api[i]['updated_at']
                return self._repo
        else:
            print(dados_api)

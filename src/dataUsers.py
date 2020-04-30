import requests
import json
from dataRepos import DataRepos

class DataUsers():

    __slots__ = [
        '_user'
    ]
    def __init__(self, user=''):
        self._user = self.user = user

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
        repo = {}
        dados_api = self.request_repo_api()
        if type(dados_api) is not int:
            for i in range(len(dados_api)):
                repo['name'] = dados_api[i]['name']
                repo['full_name'] = dados_api[i]['full_name']
                repo['description'] = dados_api[i]['description']
                repo['language'] = dados_api[i]['language']
                repo['create'] = dados_api[i]['created_at']
                repo['update'] = dados_api[i]['updated_at']
                repositorio = DataRepos(
                    repo['name'], 
                    repo['full_name'],
                    repo['description'],
                    repo['language'],
                    repo['create'],
                    repo['update'])
                print('\n\nRepositório {}'.format(i+1))
                repositorio.print_repo()
        else:
            print(dados_api)
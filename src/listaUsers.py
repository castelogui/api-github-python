import requests
import json

class ListaUsers():

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
    
    def requisicao_api(self):
        resposta = requests.get(
            f'https://api.github.com/users/{self._user}/repos'
        )
        if resposta.status_code == 200:
            return resposta.json()
        else:
            return resposta.status_code

    def recebe_repo(self):
        repo = {'name': '', 'despcription': '', 'create': '', 'update': ''}
        dados_api = self.requisicao_api()
        if type(dados_api) is not int:
            for i in range(len(dados_api)):
                repo['name'] = dados_api[i]['name']
                repo['description'] = dados_api[i]['description']
                repo['create'] = dados_api[i]['created_at']
                repo['update'] = dados_api[i]['updated_at']
                print('\n\nRepositório {}'.format(i+1))
                print(repo['name'])
                print(repo['description'])
                print(repo['create'])
                print(repo['update'])
        else:
            print(dados_api)
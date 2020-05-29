from dataUsers import DataUsers


user = 'castelogui'#input('Usuário: ')
dados = DataUsers(user)
data = dados.recebe_repo()
for i in range(len(data)):
    print(data)

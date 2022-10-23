#Dicionarios
# par de valores nao ordernado
# dic = {
#     'a': 1,
#     'b':2
#     }
# print(dic['b']) 

# qualquer valo pode ser adicionado em um dicionario
# valores precisam ser imutaveis
# chaves sao valores unicos

# user = {
#     'nome':'Breno',
#     'idade': 31,
#     'Dia do mes favorito': 2
#  }
    


# print(31 in user.values()) #retorna o valor da chave do dicionaruio


# print(f'seu dia favorito ainda continua sendo',user['Dia do mes favorito'])
# novo dic

# user2 = dict(name='Jose')
# print(user2)

# exercicio
user = {
    'age': ' ',
    'username': ' ',
    'weapons': ' ',
    'is_active': True,
    'clan': ' '
}   

user.update({'weapons': 'metralhadora'}) #atualizar a arma
print(user)
user.update({'is_banned':False}) #adiciona uma nova chave
print(user)
user.pop('is_banned') #remove a ultima chave
print(user)

user2 = user.copy() #copia o primeiro adicionado
print(user2)
user2.update({'age': 25,'username': 'Breno'})#atuliza os valores do segundo dicionario
print(user2)
print(user)






# #loop for
# # user = {
# #     'name': "Breno",
# #     'sobrenome':"Silva",
# #     'IDADE': "22ANOS"
# # }

# # for imprima_lista in user.items(): #percorra todos os item da lista user e adiciona em uma nova variave
# #     key, values = imprima_lista; # armaneza os conteudo da chave e conteudo, em duas variavreis.
# #     print(key,"/", values)


# # my_list = [1,2,3,4,5,6,7,8,9,10] lista 
# # contador = 0 - valor em zero para inicia
# # for nova_lista in my_list: adiciona a outra variavel
# #     contador = contador + nova_lista - o contador vai somando ate percorre o final e mostrando cada valor.
# #     print("Qual numero é esse ",contador)   
#--------------------------------------------------------------------
# #range dentro for

# for number in range(10,100,2):
#     print(number)  
# # for x in range(4):
# #     print(list(range(10)))
#----------------------------------------------------------------------
#loop while

while True:
    i = input("Digite o numero: ")
    if i == "15":
        print("Beleza, o número bate com o do sistema!")
        break
    else:
        print("Esta errado!")

2
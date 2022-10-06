# list ordernada - estrutura de dados
# Funciona como  uma matriz
# lista pode ser alteradas
"""
casas = ['casa1',
         'casa3',
         'casa4'
         ]

print(casas[2])

new_casa = casas[0:3]
new_casa[1] = 'minha nova casa' # mude o conteudo de [] indicado.

print(casas)
print(new_casa)
"""
# list slicing
"""
amazon_cart = [
    'notebooks',
    'Blusas',
    'carinhos',
    'comidas'
]

amazon_cart[0] = 'Join'
# lista somente o que se pede para nao alterar o conteudo principal quando for copiado
new_cart = amazon_cart[0:2]
new_cart[0] = 'gummmmmm'
print(new_cart)
print(amazon_cart)

# ex
new_list = ['a', 'b', 'c']
print(new_list[1])  # B
print(new_list[-2])  # b
print(new_list[1:3])  # b e c
new_list[0] = 'z'  # [z,b,c]
print(new_list) 

my_list = [1, 2, 3]
bonus = my_list + [5] # 1,2,3,5
my_list[0] = 'z'
print(my_list) #z,2,3
print(bonus)
"""
#--------------------------------------------------



# LIST METHODS
#adding

#car.append(6)#adicona sempreno final
##new_car = car #para usar o que foi acrescentado,usar em outra var
#print(new_car)
# #print(car)

#insert - adiciona na posiçao que escolhe

#car.insert(6 ,"bs")
#print(car)

#extend - adiciona os conteudo como se fosse um loop

#.extend([100,100,250,360])
#print(car)
#-----------------------------------------------------------------
#remove
#pop remove todo o final da lista
# car.pop()
# print("Remove o ultimo item",car)

# car.remove(1)
# print("remove o valor definido",car)
from ast import keyword
from doctest import REPORTING_FLAGS
from hashlib import new


car = [1,2,3,4,5,3,4,2,3,2,2,4,8]

# print(car.count(3))#quantas vezes o 3 aparece.
# car.sort() #sort - ordena uma lista
# print(car)
# print(car)
# new_car = car.copy()
# new_car.append(2)
# new_car.sort()
# print(new_car)

# print(list(range(0,100,3)))#cria uma lista de 3 em 3 ate 100
#list unpacking

a,b,c, *nome, d = [1,2,3,'breno','anotion',3,3,3,3,]
print(a)
print(b)
print(c)
print(nome)
print(d)


# set dados unicos sem duplicatas

# print(my_set) #remove duplicatas
from traceback import print_tb


my_set = {0,1,2,3,4}
your_set = {4,5,6,7,8,9}

# print(my_set.difference(your_set)) #mostra a diferena entre o your_set
# print(my_set.discard(4)) #descarta o 4
# print(my_set)
# print(my_set.difference_update(your_set)) #remove a diferenca entre os dois
# print(my_set)

# print(my_set.intersection(your_set)) #mostra o que esta contido nos dois. 
# print(my_set.union(your_set)) une os dois 

my_set.add(10)
print(my_set)
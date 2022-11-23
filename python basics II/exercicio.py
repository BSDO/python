some_list = [1,2,3,3,4,5,6,6,6,6,9,8,8,9,4,4,7,8,7]

duplicates = []

for valor in some_list:
    if some_list.count(valor) > 1:
       if valor not in duplicates:
            duplicates.append(valor)

print(duplicates)   
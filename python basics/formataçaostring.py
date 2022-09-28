#formatação de strings


nome = "Breno"
sobrenome = "Jose"

print(f"{nome}  {sobrenome}  ") #maneira simples de escrever as strings           

print('hi {0} seu primeiro nome é {1}'.format(sobrenome,nome))

print('hi {nome} seu primeiro nome é {sobrenome}'.format(sobrenome='jose',nome='andre'))

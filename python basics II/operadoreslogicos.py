#operadores logicos 
# >,<, ==

# nmr = 25
# nmr2 = 45

# if nmr > nmr2:
#     print(f" numero maior {nmr}")
# elif nmr2 >= nmr:
#     print("ele é maior igual")
# else:
#     print("deu errado")
# exercicio

is_magician = True
is_expert = False


#checar se o magico and expert: "you are master magic"
#checar se magico nao é expert : "at least you,re geeting there"
#checar se voce não é um magico: "you need magic powers"

if is_magician and is_expert: # se magico e expert foi verdadeiro ,imprime a mensagem
    print("Voce é um grande magico")
elif is_magician and not is_expert: # vdd e nao verdade , imprime afirmando em verdade
    print( "voce esta melhorando")
elif not is_magician: #transforma em verdade para imprimir
    print("Voce precias de superpoderes")

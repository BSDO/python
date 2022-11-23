#funçoes - usamos para nao se repetir codigo
# def ola(nome):
#     nome = nome
#     print(f"{nome} muito bem vindo!")
# nome= input("Digite seu nome")
# ola(nome)
#parametros é passado para ser usado como variavel na função
#argumentos vai ser passado na funçao com valores
#-----------------------------------------------------------
#o parametro padrao definido vai ser executado
#keywords arguments name="Breno"
#_----------------------------------------------------------
#exercicio de checar a idade
def ChecarIDade():
    """
    info:TEste de idade 
    com certas informaçoes 
    de toda idadex
    """
    idade = input("DIgite sua idade")
    if int(idade) == 18:
        print("Voce ja tem idade para dirigir")
    elif(int(idade) > 18):
        print("Bom ja vi que voce dirige!!!")
    else:
        print("Voce é menor de idade ainda")

ChecarIDade()


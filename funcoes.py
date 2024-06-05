from listas import escolhaConta, escolhaSimNao

def Escolha(lista_opcoes, msg):
    escolha = input(msg)
    while escolha not in lista_opcoes:
        print('Escolha uma opção válida\n\n')
        escolha = input(msg)
    return escolha

def meu_in(lista,elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return True
    return False


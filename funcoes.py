from listas import escolhaConta, escolhaSimNao

def Escolha(lista_opcoes, msg):
    escolha = input(msg)
    while escolha not in lista_opcoes:
        print('\nEscolha uma opção válida')
        escolha = input(msg)
    return escolha

def verificar_num(msg):
    num = input(msg)
    while not num.isnumeric():
        print('Digite somente números')
        num = input(msg)
    num = int(num)
    return num

def meu_in(lista,elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return True
    return False

def meu_index(lista,elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    raise



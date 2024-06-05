from listas import escolhaConta, escolhaSimNao, segmentosNome, segmentosID, segmentosDesc
from funcoes import Escolha

conta = Escolha(escolhaConta, 'Você é uma Pessoa ou Empresa?')
if conta == "Empresa" or conta == "empresa":
    while True:
        razaoSocial = input('Insira sua Razão Social:\n->  ')
        cnpj = input('Insira seu CNPJ:\n->  ')
        endereco = input('Insira seu Endereço Comercial:\n->  ')
        telefone = input('Insira seu Telefone:\n-> ')
        email = input('Insira seu e-mail Coporativo:\n-> ')
        senha = input('Insira uma senha:\n-> ')

        print('Seus dados estão corretos?\nRazão Social: ', razaoSocial, '\nCNPJ: ', cnpj,'\nEndereço: ', endereco, '\nTelefone: ', telefone,'\nEmail: ', email,'\nSenha: ', senha)
        correto = Escolha(escolhaSimNao, '\nSeus dados estão corretos?:\n(sim/nao)->  ')
        if correto == 'sim':
            while True:
                print('Por favor, cadastre agora os dados de seu CEO')
                nomCEO = input('Insira o Nome Completo de seu CEO:\n-> ')
                cpfCEO = input('Insira o CPF de seu CEO:\n-> ')
                rgCEO = input('Insira o RG de seu CEO:\n-> ')
                endCEO = input('Insira o Endereço Residencial de seu CEO:\n-> ')

                print('Os dados do CEO estão corretos?\nNome Completo: ', nomCEO, '\nCPF: ', cpfCEO, '\nRegistro Geral: ', rgCEO, '\nEndereço Residencial: ', endCEO) 
                correto = Escolha(escolhaSimNao, '\nOs dados do CEO estão corretos?:\n(sim/nao)->  ')
                if correto == 'sim':
                    print('Para melhorarmos sua experiência, nos diga o segmento de sua Empresa: ')
                    print('--------------------------')
                    for i in range(len(segmentosNome)):
                        print(f'{segmentosID[i]}. {segmentosNome[i]}')
                    print('--------------------------')
                    selecionado = Escolha(segmentosID, "Selecione o ID do Segmento desejado:\n->  ")

                    indice = segmentosID.index(selecionado)
                    
                    print(segmentosDesc[indice])



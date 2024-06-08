#Importando as funções e listas que estão armazenadas em outro documento py
from listas import escolhaConta, escolhaSimNao, segmentosNome, segmentosID, segmentosDesc, dados_energia, dados_pesca, dados_petrolifero, dados_turismo
# nome_ceos, cpf_ceos, rg_ceos, end_ceos
from funcoes import Escolha, verificar_num, meu_index

#listas vazias para guardar as informações dos ceos
nome_ceos= []
cpf_ceos = []
rg_ceos  = []
end_ceos = []

#Essa é a seção de cadastro das empresas
conta = Escolha(escolhaConta, 'Você é uma Pessoa ou Empresa?')
if conta == "Empresa" or conta == "empresa":
    while True:
        razaoSocial = input('Insira sua Razão Social:\n->  ')
        cnpj = verificar_num('Insira seu CNPJ:\n->  ')
        endereco = input('Insira seu Endereço Comercial:\n->  ')
        telefone = verificar_num('Insira seu Telefone:\n-> ')
        email = input('Insira seu e-mail Coporativo:\n-> ')
        senha = input('Insira uma senha:\n-> ')

        print('\nVerifique os dados informados:\nRazão Social: ', razaoSocial, '\nCNPJ: ', cnpj,'\nEndereço: ', endereco, '\nTelefone: ', telefone,'\nEmail: ', email,'\nSenha: ', senha)
        correto = Escolha(escolhaSimNao, '\nSeus dados estão corretos?:\n(sim/nao)->  ')
        if correto == 'sim':
            while True:
                #seção de cadastro dos ceos
                print('--------------------------------------------------------------')
                print('\nPor favor, cadastre agora os dados de seu CEO\n')
                nomCEO = input('Insira o Nome Completo de seu CEO:\n-> ')
                nome_ceos.append(nomCEO)
                cpfCEO = verificar_num('Insira o CPF de seu CEO:\n-> ')
                cpf_ceos.append(cpfCEO)
                rgCEO = verificar_num('Insira o RG de seu CEO:\n-> ')
                rg_ceos.append(rgCEO)
                endCEO = input('Insira o Endereço Residencial de seu CEO:\n-> ')
                end_ceos.append(endCEO)

                # print(nome_ceos)
                # print(cpf_ceos)
                # print(rg_ceos)
                # print(end_ceos)
                
                #se possuir mais ceos, o código voltará para o início do while, solicitando os dados do ceo
                mais_cadastro = Escolha(escolhaSimNao,'\nPossui mais algum CEO? (sim/nao)-> ')
                if mais_cadastro == 'sim':
                    continue
                
                print('\nVerifique os dados informados:\n')
                for i in range(len(nome_ceos)):
                    print(f'\nCeo{i}\nNome Completo: {nome_ceos[i]} \nCPF: {cpf_ceos[i]} \nRG: {rg_ceos[i]} \nEndereço Residencial: {end_ceos[i]}\n')

                correto = Escolha(escolhaSimNao, '\nOs dados do CEO estão corretos?:\n(sim/nao)->  ')

                #se os dados estiverem incorretos, o usuário deverá indicar, pela númeração(índice), qual ceo está com os dados incorretos. Após isso, o "del" irá deletar todos os dados das listas do ceo indicado pelo indice
                if correto == 'nao':
                    errado = verificar_num('Os dados de qual CEO estão incorretos? Digite o número do CEO\n')
                    del nome_ceos[errado]
                    del cpf_ceos[errado]
                    del rg_ceos[errado]
                    del end_ceos[errado]
                    
                    # print(nome_ceos) #print somente para testes
                    # print(cpf_ceos)
                    # print(rg_ceos)
                    # print(end_ceos)
                    continue
                else:    
                    break
            
            
            while True:
                #Aqui é uma simulação da nossa solução BlueVision, onde a empresa escolherá o segmento em que ela atua
                print('Para melhorarmos sua experiência, nos diga o segmento de sua Empresa: ')
                print('--------------------------------------------------------------')
                for i in range(len(segmentosNome)):
                    print(f'{segmentosID[i]}. {segmentosNome[i]}')
                print('--------------------------------------------------------------')

                selecionado = Escolha(segmentosNome, "Escreva o nome do segmento desejado:\n->  ")

                indice = meu_index(segmentosNome,selecionado)      
                print(segmentosDesc[indice])

                correto = Escolha(escolhaSimNao, "\nVocê deseja seguir com este seguimento?:\n(sim/nao)-> ")
                
                #Nessa seção, será apresentado alguns dados para o usuário referente ao segmento selecionado por ele. 
                if correto == 'sim':
                    if selecionado == 'Pescaria':
                        print("Dados Relevantes para o Segmento de Pesca:\n")
                        for i, y in dados_pesca.items():
                            print(f"{i}: {y}")

                    elif selecionado == 'Energia':
                        print("Dados Relevantes para o Segmento de Energia:\n")
                        for i, y in dados_energia.items():
                            print(f"{i}: {y}")

                    elif selecionado == 'Turismo':
                        print("Dados Relevantes para o Segmento de Turismo:\n")
                        for i, y in dados_turismo.items():
                            print(f"{i}: {y}")
                    
                    else:
                        print("Dados Relevantes para o Segmento de Petrolifica:\n")
                        for i, y in dados_petrolifero.items():
                            print(f"{i}: {y}")
                    break
else:
    print('Sentimos muito, mas esse site é restrito para empresas! :(')



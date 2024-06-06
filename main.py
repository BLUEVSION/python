from listas import escolhaConta, escolhaSimNao, segmentosNome, segmentosID, segmentosDesc
# nome_ceos, cpf_ceos, rg_ceos, end_ceos
from funcoes import Escolha, verificar_num, meu_index

nome_ceos= []
cpf_ceos = []
rg_ceos  = []
end_ceos = []

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
                
                mais_cadastro = Escolha(escolhaSimNao,'\nPossui mais algum CEO? (sim/nao)-> ')
                if mais_cadastro == 'sim':
                    continue
                
                print('\nVerifique os dados informados:\n')
                for i in range(len(nome_ceos)):
                    print(f'\nCeo{i}\nNome Completo: {nome_ceos[i]} \nCPF: {cpf_ceos[i]} \nRG: {rg_ceos[i]} \nEndereço Residencial: {end_ceos[i]}\n')

                correto = Escolha(escolhaSimNao, '\nOs dados do CEO estão corretos?:\n(sim/nao)->  ')

                if correto == 'nao':
                    errado = verificar_num('Os dados de qual CEO estão incorretos? Digite o número do CEO\n')
                    del nome_ceos[errado]
                    del cpf_ceos[errado]
                    del rg_ceos[errado]
                    del end_ceos[errado]
                    
                    print(nome_ceos)
                    print(cpf_ceos)
                    print(rg_ceos)
                    print(end_ceos)
                    continue
                else:    
                    break

        print('Para melhorarmos sua experiência, nos diga o segmento de sua Empresa: ')
        print('--------------------------------------------------------------')
        for i in range(len(segmentosNome)):
            print(f'{segmentosID[i]}. {segmentosNome[i]}')
        print('--------------------------------------------------------------')
        # selecionado = Escolha(segmentosID, "Selecione o ID do Segmento desejado:\n->  ")
        

        # # indice = meu_index(segmentosID,selecionado) 
        # # print(indice)
        # # print(segmentosDesc[indice])
        # indice = segmentosID.index(selecionado)
                
        # print(segmentosDesc[indice])

        selecionado = Escolha(segmentosNome, "Escreva o nome do segmento desejado:\n->  ")

        indice = meu_index(segmentosNome,selecionado)      
        print(segmentosDesc[indice])



escolhaConta = ['pessoa', 'empresa', 'Pessoa', 'Empresa']
escolhaSimNao = ['sim', 'nao']
segmentosNome = ['Pescaria','Energia','Turismo','Petrolifica']
segmentosID = ['1','2','3','4']
segmentosDesc = [
                'Para sua empresa de PESCA, iremos organizar e separar exatamente suas áreas de atuação, onde poderá realizar suas atividades sem impactar negativamente na vida marinha, tanto na vida dos animais quanto nas rotas comerciais, habbitats naturais e suas áreas de preservação.'
                 
                 'Para sua empresa de ENERGIA, iremos separar suas respectivas áreas para construção de dispositivos tecnológicos geradores de energia OFFSHORE como usinas eólicas, maremotrizes e oceânicas para que não influenciem em rotas comerciais, áreas de preservação, pesca, entre outros.',

                 'Para sua empresa de TURISMO, selecionaremos as melhores áreas para direcionar seu público para possuirem uma melhor experiência durante suas viagens a praias, incluindo os mergulhos organizados, onde seus clientes poderão mergulhar e presenciarem santuários aquáticos e várias espécies de peixes e não influenciando em nenhuma rota comercial ou habbitat natural marinho.',
                 
                 'Para sua empresa direcionada a área PETROLÍFICA, iremos separar as áreas corretas para a construção das OFFSHORE extratores de petróleo, para que as contruções e consequências do setor não influenciem em fatores naturais, como no impacto de santuários aquáticos, espécies marinhas, acidez nas águas ocasionando na morte de diversos peixes, degradação de habbitats e espécies de conservação, entre outros.']

nome_ceos= []
cpf_ceos = []
rg_ceos = []
end_ceos = []

#DADOS DOS SEGMENTOS

dados_pesca = {
    "Zonas de Pesca": ["Atlântico Norte", "Atlântico Sul", "Pacífico Equatorial"],
    "Estoque de Peixes": {"Sardinha": 10000, "Atum": 5000, "Bacalhau": 7000},
    "Temporadas de Pesca": {"Sardinha": "Maio a Setembro", "Atum": "Janeiro a Dezembro", "Bacalhau": "Julho a Agosto"},
    "Métodos de Pesca": ["Redes de cerco", "Arrasto de fundo", "Pesca de linha"]
}

dados_energia = {
    "Localização de Recursos": ["Parque Eólico X", "Planta de Energia das Marés Y", "Projeto de Energia das Ondas Z"],
    "Infraestrutura Submarina": {"Cabos submarinos": 15, "Plataformas de petróleo": 5},
    "Impactos Ambientais": "Estudos em andamento"
}

dados_turismo = {
    "Zonas de Turismo": ["Recife de Corais A", "Praia B", "Ilha C"],
    "Infraestrutura de Apoio": ["Marina Central", "Hotéis à beira-mar", "Restaurantes"],
    "Dados Ambientais": {"Qualidade da Água": "Boa", "Biodiversidade Marinha": "Rica", "Áreas Protegidas": ["Parque Nacional X", "Reserva Marinha Y"]}
}

dados_petrolifero = {
    "Reservas de Petróleo e Gás": {"Campo de Petróleo A": 500000, "Campo de Gás B": 300000},
    "Riscos Ambientais": "Estudos em andamento",
    "Infraestrutura": {"Plataformas Offshore": 10, "Oleodutos": 4}
}

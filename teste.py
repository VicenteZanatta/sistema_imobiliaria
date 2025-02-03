
def menu_incial():
    
    print("+---------------------------+")
    print("|[1] Rendimento Corretores  |")
    print("|[2] 3 Imóveis Mais Caros   |")
    print("|[3] Propostas por imóvel   |")
    print("|[4] Imovés Cadastrados     |")
    print("|[5] Cliente Com Propostas  |")
    print("|[6] Atualizar              |")
    print("|[7] Remover                |")
    print("|[7] Cadastrar              |")
    print("+---------------------------+")
    print("|[0] Sair                   |")
    print("+---------------------------+")

def menu_imoveis():

    print("+-------------------------+")
    print("Buscar Por:               |")
    print("+-------------------------+")
    print("|[1] Alugados             |")
    print("|[2] Não Alugados         |")
    print("|[2] Todos                |")
    print("+-------------------------+")
    print("|[0] Sair                 |")
    print("+-------------------------+")

def menu_cadastro():

    print("+-------------------------+")
    print("|[1] Imóvel               |")
    print("|[2] Cliente              |")
    print("|[2] Corretor             |")
    print("+-------------------------+")
    print("|[0] Sair                 |")
    print("+-------------------------+")

def todos_imoveis():
    query = "SELECT * FROM imoveis;"
    cursor.execute(querry)
    resultado = cursor.fetchall
    imprimir_resultados(resultado)

def imprimir_resultados(resultados):
    for linha in resultados:
        print((f"{str(valor):<20}|" for valor in linha))

while(1):

    opcao = 0
    menu_incial()
    opcao = int(input(": "))

    match opcao:

        case 1:
            menu_rendimento()
        #case 2:
            #imoveis_mais_caros = listar_imoveis_mais_caros()
        case 3:
            while(1)
            menu_propostas()
        case 4:
            while(1):
                menu_imoveis()
        #case 5:
        #case 6:
        #case 7:
        case 0:
            break
        case _:
            print("OPÇÃO INVÁLIDA")







def menu_incial():
    
    print("+-------------------------+")
    print("|[1] Rendimento              |")
    print("|[2] Imóveis              |")
    print("|[3] Corretor             |")
    print("|[4] Cliente              |")
    print("|[5] Contratos            |")
    print("|[6] Propostas            |")
    print("|[7] Visitas              |")
    print("+-------------------------+")
    print("|[0] Sair                 |")
    print("+-------------------------+")

def menu_rendimento():

    print("+-------------------------+")
    print("|[1] Rendimento Corretores|")
    print("|[2] Rendimento Anual     |")
    print("+-------------------------+")
    print("|[0] Sair                 |")
    print("+-------------------------+")

def menu_imoveis():

    print("+-------------------------+")
    print("|[1] Todos Cadastrados    |")
    print("|[2] Alugados             |")
    print("|[2] Não Alugados         |")
    print("+-------------------------+")
    print("|[0] Sair                 |")
    print("+-------------------------+")

def filtro_imoveis():

    print("+-------------------------+")
    print("Buscar Por:               |")
    print("+-------------------------+")
    print("|[1] Todos                |")
    print("|[2] Preco                |")
    print("|[3] Cliente              |")
    print("|[4] Proprietario         |")
    print("+-------------------------+")
    print("Cadastrar:               |")
    print("+-------------------------+")
    print("|[5] Cadastrar Novo       |")
    print("+-------------------------+")
    print("|[0] Sair                 |")
    print("+-------------------------+")
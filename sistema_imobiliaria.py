import mysql.connector

# Configuração de conexão com o banco
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sua-senha",
    database="imobiliaria"
)
cursor = conn.cursor()

#CONSTANTES 
INQUILINO = 1 
PROPRIETARIO = 2

# Funções de manipulação de dados
def cadastrar_cliente():
    cpf = input("CPF: ")
    nome = input("Nome: ")
    estado_civil = input("Estado Civil: ")
    telefone = input("Telefone: ")

    if not confirmacao():   #confirmação da ação
        return

    cursor.execute(
        '''INSERT INTO cliente (cpf, nome, estado_civil, telefone) 
           VALUES (%s, %s, %s, %s)''', (cpf, nome, estado_civil, telefone))

    if tipo_cliente() == INQUILINO:
        cadastrar_inquilino(cpf)

    conn.commit()
    print("Cliente inserido com sucesso!")

def cadastrar_corretor():
    creci = input("CRECI: ")
    nome = input("Nome: ")
    data_inicio = input("Data de Início: ")
    tel = input("Telefone: ")
    comissao = input("Comissão: ")

    if not confirmacao():   #confirmação da ação
        return

    cursor.execute(
        '''INSERT INTO corretor (creci, nome, tel, dataInicio, comissao) 
           VALUES (%s, %s, %s, %s, %s)''', (creci, nome, tel, data_inicio, comissao)
    )
    conn.commit()
    print("Corretor inserido com sucesso!")

def cadastrar_imovel():
    endereco = input("ENDEREÇO: ")
    n_comodos = input("NUMERO DE COMODOS: ")
    n_vagas = input("NUMERO DE VAGAS: ")
    m2_construido = input("ÁREA CONSTRUÍDA: ")
    data_cadastro = input("DATA CADASTRO: ")
    aluguel = input("VALOR ALUGUEL: ")
    corretor_creci = input("CRECI DO CORRETOR: ")
    proprietario_cpf = input("CPF DO PROPRIETÁRIO: ")

    if not confirmacao():   #confirmação da ação
        return
    
    cadastrar_propietario(proprietario_cpf) #adiciona cpf do proprietario a table "proprietario" associado com oi numero de registro e data de registro do imóvel

    cursor.execute(
        '''INSERT INTO imovel (endereco, nComodos, nVagas, m2Construido, dataCadastro, aluguel, corretor_creci, proprietario_cpf)
           VALUES (%s, %s, %s, %s, %s, %s, %s, %s)''', (endereco, n_comodos, n_vagas, m2_construido, data_cadastro, aluguel, corretor_creci, proprietario_cpf)
    )
    conn.commit()
    print("Imóvel inserido com sucesso!")

def cadastrar_propietario(cpf_propietario):
    
    nRegistro = input("Numero do Registro: ")
    dRegistro = input("Data Registro: ")

    if not confirmacao():
        return
    
    cursor.execute(
        '''INSERT INTO proprietario (cliente_cpf, nRegistro, dataRegistro)
           VALUES (%s, %s, %s)''', (cpf_propietario, nRegistro, dRegistro))
    
def cadastrar_inquilino(cpf_inquilino):
    
    profissao = input("Profissão: ")
    renda = input("Renda: ")
    creci = input("CRECI do Corretor Associado: ")


    if not confirmacao():
        return

    cursor.execute(
        '''INSERT INTO inquilino (cliente_cpf, profissao, renda, corretor_creci)
           VALUES (%s, %s, %s, %s)''', (cpf_inquilino, profissao, renda, creci)
    )
    conn.commit()
    print("Inquilino cadastrado com sucesso!")


def atualizar_cliente():
    cpf = input("CPF do cliente: ")
    nomeAtt = input("Nome: ")
    estado_civilAtt = input("Estado civil: ")
    telefoneAtt = input("Telefone: ")

    if not confirmacao():   #confirmação da ação
        return

    cursor.execute(
        '''UPDATE cliente SET nome = %s, estado_civil = %s, telefone = %s WHERE cpf = %s''',
        (nomeAtt, estado_civilAtt, telefoneAtt, cpf)
    )
    conn.commit()
    print("Dados do cliente atualizados com sucesso!")

def atualizar_imovel():
    id = input("ID DO IMÓVEL: ")
    endereco = input("ENDEREÇO: ")
    n_comodos = input("NUMERO DE CÔMODOS: ")
    n_vagas = input("NUMERO DE VAGAS: ")
    m2_construido = input("ÁREA CONSTRUÍDA: ")
    data_cadastro = input("DATA CADASTRO: ")
    aluguel = input("VALOR ALUGUEL: ")
    corretor_creci = input("CRECI DO CORRETOR: ")
    proprietario_cpf = input("CPF DO PROPRIETÁRIO: ")

    if not confirmacao():   #confirmação da ação
        return

    cursor.execute(
        '''UPDATE imovel SET endereco = %s, nComodos = %s, nVagas = %s, m2Construido = %s, dataCadastro = %s, 
           aluguel = %s, corretor_creci = %s, proprietario_cpf = %s WHERE idImovel = %s''',
        (endereco, n_comodos, n_vagas, m2_construido, data_cadastro, aluguel, corretor_creci, proprietario_cpf, id)
    )
    conn.commit()
    print("Dados do imóvel atualizados com sucesso!")

def atualizar_corretor():
    creci = input("CRECI do corretor: ")
    nomeAtt = input("Nome: ")
    data_inicioAtt = input("Data de Início: ")
    telAtt = input("Telefone: ")
    comissaoAtt = input("Comissão: ")

    if not confirmacao():   #confirmação da ação
        return

    cursor.execute(
        '''UPDATE corretor SET nome = %s, tel = %s, dataInicio = %s, comissao = %s WHERE creci = %s''',
        (nomeAtt, telAtt, data_inicioAtt, comissaoAtt, creci)
    )
    conn.commit()
    print("Dados do corretor atualizados com sucesso!")

def deletar_cliente():
    cpf = input("CPF do cliente: ")
    
    espec = tipo_cliente()

    if not confirmacao(): #confirmação da ação
        return
    
    if espec == INQUILINO:
        cursor.execute("DELETE FROM fiador WHERE inquilino_cpf = %s", (cpf,)) #caso o cliente seja um inquilimo é preciso remover seus fiadores
        cursor.execute("DELETE FROM inquilino WHERE cliente_cpf = %s", (cpf,)) #caso o cliente seja um inquilimo é preciso remover seus fiadores

    elif espec == PROPRIETARIO:
        cursor.execute("DELETE FROM imovel WHERE proprietario_cpf = %s", (cpf,)) #caso o cliente seja um proprietario é preciso remover seus imoveis
        cursor.execute("DELETE FROM proprietario WHERE cliente_cpf = %s", (cpf,)) 
        
    cursor.execute("DELETE FROM cliente WHERE cpf = %s", (cpf,))
    conn.commit()
    print("Cliente deletado com sucesso!")

def deletar_corretor():
    creci = input("CRECI do corretor: ")

    if not confirmacao(): #confirmação da ação
        return
    
    cursor.execute('''UPDATE imovel 
                        SET corretor_creci = NULL 
                        WHERE corretor_creci = %s''', (creci,)) # desassocia corretor de seus clientes
    
    cursor.execute('''UPDATE inquilino
                        SET corretor_creci = NULL       
                        WHERE corretor_creci = %s''', (creci,)) # desassocia corretor de imoveis
    
    cursor.execute('''DELETE FROM corretor 
                        WHERE creci = %s''', (creci,)) # deleta corretor
    
    conn.commit()
    print("Corretor deletado com sucesso!")

def deletar_imovel():
    id = input("ID do imóvel: ")

    if not confirmacao():   #confirmação da ação
        return

    cursor.execute("DELETE FROM imovel WHERE idImovel = %s", (id,)) # imovel só é removido apenas da tabla imovel pois é necessario guardar os outros registros 
    conn.commit()
    print("Imóvel deletado com sucesso!")

# Funções de consultas 
def listar_todos_clientes_com_proposta():
    cursor.execute('''SELECT DISTINCT c.nome, c.cpf 
                      FROM cliente c
                      JOIN proposta p ON c.cpf = p.cliente_cpf''')
    resultados = cursor.fetchall()
    imprimir_resultados(resultados)

def listar_propostas_por_imovel():
    
    imovel_id = input("ID IMOVEL:")
    
    cursor.execute(
        '''SELECT * 
           FROM proposta p
           WHERE p.imovel_id = %s''', 
        (imovel_id,)
    )
    resultados = cursor.fetchall()
    imprimir_resultados(resultados)

def listar_imoveis_mais_caros():
    cursor.execute('''SELECT endereco, aluguel
                      FROM imovel
                      ORDER BY aluguel DESC
                      LIMIT 3''')
    resultados = cursor.fetchall()
    imprimir_resultados(resultados)

def corretor_maior_rendimento_2022():
    cursor.execute('''SELECT cr.nome, SUM(i.aluguel * cr.comissao / 100) AS rendimento 
                        FROM corretor cr 
                        JOIN imovel i ON cr.creci = i.corretor_creci 
                        JOIN contrato as cn ON i.idImovel = cn.imovel_id 
                        WHERE YEAR(cn.inicio) = 2022 
                        GROUP BY cr.creci 
                        ORDER BY rendimento 
                        DESC LIMIT 1;''') # realiza a soma dos alugueis em contratos realizados pelos corretores e ordena por ordem decrescente e seleciona o priemiro
    resultado = cursor.fetchall()
    imprimir_resultados(resultado)


def todos_imoveis():
    cursor.execute('''SELECT * 
                    FROM imovel''')
    resultados = cursor.fetchall()
    imprimir_resultados(resultados)

def imoveis_alugados():
    cursor.execute('''SELECT *  
                        FROM imovel 
                        WHERE idImovel 
                        IN (SELECT imovel_id 
                            FROM contrato)''') # seleciona os imoveis que estão na table "contrato"
    resultados = cursor.fetchall()
    imprimir_resultados(resultados)

def imoveis_nao_alugados():
    cursor.execute('''SELECT *  
                        FROM imovel 
                        WHERE idImovel 
                        NOT IN (SELECT imovel_id 
                                FROM contrato)''') #seleciona os imoveis que não estão na tabela "contrato", ou seja, não estão alugados
    resultados = cursor.fetchall()
    imprimir_resultados(resultados)

def imprimir_resultados(resultados):
    for linha in resultados:
        print(" | ".join(f"{str(valor):<20}" for valor in linha))

    
def menu_confirmacao():

    print("+---------------------------+")
    print("| CONFIRMAR OPERAÇÃO        |")
    print("+---------------------------+")
    print("| [1] CONFIRMAR             |")
    print("| [2] CANCELAR              |")
    print("+---------------------------+")

def menu_inicial():
    
    print("+---------------------------+")
    print("|MENU PRINCIPAL             |")
    print("+---------------------------+")
    print("|[1] Rendimento Corretores  |")
    print("|[2] 3 Imóveis Mais Caros   |")
    print("|[3] Propostas por imóvel   |")
    print("|[4] Imóveis Cadastrados    |")
    print("|[5] Cliente Com Propostas  |")
    print("|[6] Atualizar              |")
    print("|[7] Remover                |")
    print("|[8] Cadastrar              |")
    print("+---------------------------+")
    print("|[0] Sair                   |")
    print("+---------------------------+")

def menu_novo_cadastro():
    
    print("+---------------------------+")
    print("|NOVO CADASTRO              |")
    print("+---------------------------+")
    print("|[1] Corretores             |")
    print("|[2] Clientes               |")
    print("|[3] Imoveis                |")
    print("+---------------------------+")
    print("|[0] Sair                   |")
    print("+---------------------------+")

def menu_deletar():
    
    print("+---------------------------+")
    print("|DELETAR                    |")
    print("+---------------------------+")
    print("|[1] Corretores             |")
    print("|[2] Clientes               |")
    print("|[3] Imoveis                |")
    print("+---------------------------+")
    print("|[0] Sair                   |")
    print("+---------------------------+")

def menu_atualizar():
    
    print("+---------------------------+")
    print("|ATUALIZAR                  |")
    print("+---------------------------+")
    print("|[1] Corretores             |")
    print("|[2] Clientes               |")
    print("|[3] Imoveis                |")
    print("+---------------------------+")
    print("|[0] Sair                   |")
    print("+---------------------------+")

def menu_imoveis():
    
    print("+---------------------------+")
    print("|BUSCAR POR:                |")
    print("+---------------------------+")
    print("|[1] Todos                  |")
    print("|[2] Alugados               |")
    print("|[3] Não alugados           |")
    print("+---------------------------+")
    print("|[0] Sair                   |")
    print("+---------------------------+")

def menu_tipo_cliente():
    
    print("+---------------------------+")
    print("|Tipo de Cliente:           |")
    print("+---------------------------+")
    print("|[1] Inquilino              |")
    print("|[2] Propiretario           |")
    print("+---------------------------+")
    print("|[0] Sair                   |")
    print("+---------------------------+")

def tipo_cliente(): #função  usada para distiguir o tipo de cliente

    while 1:
        menu_tipo_cliente()
        opcao = int(input(": "))
        match opcao:
            case 1:
                return INQUILINO
            case 2:
                return PROPRIETARIO
            case _:
                print("+---------------------------+")
                print("| OPÇÃO INVÁLIDA            |")
                print("+---------------------------+")

def confirmacao(): # função que retorna a confirmação de uma ação de manipulação de dados 

    while 1:
        menu_confirmacao()
        opcao = int(input(": "))
        match opcao:
            case 1:
                print("+---------------------------+")
                print("| OPERAÇÃO CONFIRMADA       |")
                print("+---------------------------+")
                return True
            case 2:
                print("+---------------------------+")
                print("| OPERAÇÃO CANCELADA        |")
                print("+---------------------------+")
                return False
            case _:
                print("+---------------------------+")
                print("| OPÇÃO INVÁLIDA            |")
                print("+---------------------------+")
                

def listar_imoveis():

    while(1):
        menu_imoveis()
        opcao = int(input(": "))

        match opcao:
            case 1:
                print("\n----------------------------") 
                todos_imoveis()
                print("----------------------------\n")   
            case 2:
                print("\n----------------------------") 
                imoveis_alugados()
                print("----------------------------\n") 
            case 3:
                print("\n----------------------------\n") 
                imoveis_nao_alugados()
                print("----------------------------\n") 
            case 0:
                break
            case _:
                print("+---------------------------+")
                print("|OPÇÃO INVALIDA             |")
                print("+---------------------------+")

def atualizar():

    while(1):
        menu_atualizar()
        opcao = int(input(": "))

        match opcao:
            case 1:
                print("\n----------------------------")
                atualizar_corretor()
                print("----------------------------\n")    
            case 2:
                print("\n----------------------------")
                atualizar_cliente()
                print("----------------------------\n") 
            case 3:
                print("\n----------------------------")
                atualizar_imovel()
                print("----------------------------\n") 
            case 0:
                break
            case _:
                print("OPÇÃO INVALIDA")

def cadastrar():

    while(1):
        menu_novo_cadastro()
        opcao = int(input(": "))

        match opcao:
            case 1:
                print("\n----------------------------")
                cadastrar_corretor()
                print("----------------------------\n")    
            case 2:
                print("\n----------------------------")
                cadastrar_cliente()
                print("----------------------------\n") 
            case 3:
                print("\n----------------------------")
                cadastrar_imovel()
                print("----------------------------\n") 
            case 0:
                break
            case _:
                print("OPÇÃO INVALIDA") 

def remover():

    while(1):
        menu_deletar()
        opcao = int(input(": "))

        match opcao:
            case 1:
                print("\n----------------------------")
                deletar_corretor()
                print("----------------------------\n")    
            case 2:
                print("\n----------------------------")
                deletar_cliente()
                print("----------------------------\n") 
            case 3:
                print("\n----------------------------")
                deletar_imovel()
                print("----------------------------\n") 
            case 0:
                break
            case _:
                print("OPÇÃO INVALIDA")          

while (1):
    menu_inicial()
    opcao = int(input(": "))

    match opcao:
        case 1:
            print("\n----------------------------")
            corretor_maior_rendimento_2022()
            print("----------------------------\n") 
        case 2:
            print("\n----------------------------")
            listar_imoveis_mais_caros()
            print("----------------------------\n")            
        case 3:
            print("\n----------------------------")
            listar_propostas_por_imovel()
            print("----------------------------\n")             
        case 4:
            listar_imoveis()
        case 5:
            print("\n----------------------------")
            listar_todos_clientes_com_proposta()
            print("----------------------------\n") 
        case 6:
            atualizar()
        case 7:
            remover()
        case 8:
            cadastrar()
        case 0:
            conn.close()
            print("\nConexão encerrada.")
            print("\nBye")
            break
        case _:
            print("Opção inválida!")

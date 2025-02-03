CREATE TABLE cliente (
    cpf BIGINT NOT NULL PRIMARY KEY,
    nome VARCHAR(50),
    estado_civil VARCHAR(20),
    telefone VARCHAR(15) -- Formato: (ddd) 12345678
);

CREATE TABLE corretor
(
creci INT(8) NOT NULL PRIMARY KEY,
nome VARCHAR(50),
tel VARCHAR(15),
dataInicio DATE,
comissao INT(2) -- PORCENTAGEM DA COMISSÃO 
);

CREATE TABLE proprietario
(
cliente_cpf BIGINT PRIMARY KEY,
nRegistro BIGINT,
dataRegistro DATE,
FOREIGN KEY(cliente_cpf) REFERENCES cliente(cpf)
);

CREATE TABLE inquilino
(
cliente_cpf BIGINT PRIMARY KEY,
profissao VARCHAR(20),
renda DECIMAL(8,2),
corretor_creci INT(8),
FOREIGN KEY(cliente_cpf) REFERENCES cliente(cpf),
FOREIGN KEY(corretor_creci) REFERENCES corretor(creci)
);

CREATE TABLE fiador
(
cpf BIGINT PRIMARY KEY,
nome VARCHAR(50),
saldo DECIMAL(8,2),
tel VARCHAR(15),
inquilino_cpf BIGINT,
FOREIGN KEY(inquilino_cpf) REFERENCES cliente(cpf)
);

CREATE TABLE imovel
(
idImovel BIGINT AUTO_INCREMENT PRIMARY KEY,
endereco VARCHAR(200) NOT NULL,
nComodos INT(2),
nVagas INT(2),
m2Construido INT(4),
dataCadastro DATE,
aluguel DECIMAL(8,2),
corretor_creci INT(8),
proprietario_cpf BIGINT,
FOREIGN KEY(proprietario_cpf) REFERENCES cliente(cpf),
FOREIGN KEY(corretor_creci) REFERENCES corretor(creci)
);

CREATE TABLE proposta
(
cliente_cpf BIGINT,
imovel_id BIGINT,
data DATE,
valor DECIMAL(8,2),
validade DATE,
PRIMARY KEY (cliente_cpf, imovel_id), 
FOREIGN KEY (cliente_cpf) REFERENCES cliente(cpf),
FOREIGN KEY (imovel_id) REFERENCES imovel(idImovel)
);

CREATE TABLE visita
(
data DATETIME,
cliente_cpf BIGINT,
imovel_id BIGINT,
corretor_creci INT(8),
PRIMARY KEY (data, cliente_cpf),
FOREIGN KEY (cliente_cpf) REFERENCES cliente(cpf),
FOREIGN KEY (imovel_id) REFERENCES imovel(idImovel)
);

CREATE TABLE contrato
(
nContrato BIGINT AUTO_INCREMENT PRIMARY KEY,
proprietario_cpf BIGINT,
inquilino_cpf BIGINT,
imovel_id BIGINT,
valor BIGINT,
inicio DATE,
fim DATE,
FOREIGN KEY (proprietario_cpf) REFERENCES cliente(cpf),
FOREIGN KEY (inquilino_cpf) REFERENCES cliente(cpf),
FOREIGN KEY (imovel_id) REFERENCES imovel(idImovel)
);

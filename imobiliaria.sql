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




-- Inserir dados na tabela cliente
INSERT INTO cliente (cpf, nome, estado_civil, telefone) VALUES
(12345678901, 'João Silva', 'Solteiro', '(011) 987654321'),
(98765432100, 'Maria Oliveira', 'Casado', '(021) 912345678'),
(11122233344, 'Ana Santos', 'Divorciado', '(031) 923456789'),
(22233344455, 'Carlos Pereira', 'Solteiro', '(041) 934567890'),
(33344455566, 'Paula Souza', 'Viúvo', '(051) 945678901');

-- Inserir dados na tabela corretor
INSERT INTO corretor (creci, nome, tel, dataInicio, comissao) VALUES
(12345678, 'Renato Almeida', '(011) 998877665', '2020-01-15', 5),
(87654321, 'Juliana Costa', '(021) 911223344', '2018-06-20', 4),
(11223344, 'Marcelo Rodrigues', '(031) 922334455', '2019-03-10', 6);

-- Inserir dados na tabela proprietario
INSERT INTO proprietario (cliente_cpf, nRegistro, dataRegistro) VALUES
(12345678901, 1001, '2021-05-10'),
(98765432100, 1002, '2021-06-12');

-- Inserir dados na tabela inquilino
INSERT INTO inquilino (cliente_cpf, profissao, renda) VALUES
(11122233344, 'Engenheiro', 8000.00),
(22233344455, 'Médico', 12000.00);

-- Inserir dados na tabela fiador
INSERT INTO fiador (cpf, nome, saldo, tel, inquilino_cpf) VALUES
(44455566677, 'Roberto Lima', 15000.00, '(61) 912345678', 11122233344),
(55566677788, 'Fernanda Ribeiro', 20000.00, '(71) 923456789', 22233344455);

-- Inserir dados na tabela imovel
INSERT INTO imovel (endereco, nComodos, nVagas, m2COnstruido, dataCadastro, aluguel, corretor_creci, proprietario_cpf) VALUES
('Rua das Flores, 123, São Paulo, SP', 5, 2, 200, '2022-01-10', 2500.00, 12345678, 12345678901),
('Avenida Brasil, 456, Rio de Janeiro, RJ', 4, 1, 150, '2022-02-15', 3000.00, 87654321, 98765432100);

-- Inserir dados na tabela proposta
INSERT INTO proposta (cliente_cpf, imovel_id, data, valor, validade) VALUES
(11122233344, 1, '2023-01-20', 2400.00, '2023-02-20'),
(22233344455, 2, '2023-01-25', 2900.00, '2023-02-25');

-- Inserir dados na tabela visita
INSERT INTO visita (data, cliente_cpf, corretor_creci) VALUES
('2023-01-15 10:00:00', 1, 11122233344, 12345678),
('2023-01-20 15:30:00', 2, 22233344455, 87654321);

-- Inserir dados na tabela contrato
INSERT INTO contrato (proprietario_cpf, inquilino_cpf, imovel_id, valor, validade) VALUES
(12345678901, 11122233344, 1, 2400, '2022-01-20', '2024-01-20'),
(98765432100, 22233344455, 2, 2900, '2022-01-25', '2024-01-25');

-- Inserir mais clientes
INSERT INTO cliente (cpf, nome, estado_civil, telefone) VALUES
(44455566677, 'Luiz Martins', 'Casado', '(61) 998877665'),
(55566677788, 'Camila Nogueira', 'Solteiro', '(71) 912345678'),
(66677788899, 'Fernanda Lima', 'Divorciado', '(81) 934567890'),
(77788899900, 'Ricardo Alves', 'Viúvo', '(91) 945678901'),
(88899900011, 'Sofia Barros', 'Solteiro', '(31) 923456789');

-- Inserir mais corretores
INSERT INTO corretor (creci, nome, tel, dataInicio, comissao) VALUES
(33445566, 'Bruno Rocha', '(41) 988776655', '2020-07-10', 5),
(44556677, 'Daniela Freitas', '(51) 987654321', '2019-04-15', 4),
(55667788, 'Rafael Andrade', '(71) 976543210', '2021-11-20', 6);

-- Inserir mais proprietários
INSERT INTO proprietario (cliente_cpf, nRegistro, dataRegistro) VALUES
(44455566677, 1003, '2021-07-15'),
(55566677788, 1004, '2021-08-20'),
(66677788899, 1005, '2022-02-25');

-- Inserir mais inquilinos
INSERT INTO inquilino (cliente_cpf, profissao, renda) VALUES
(77788899900, 'Professor', 4500.00),
(88899900011, 'Arquiteto', 9000.00);

-- Inserir mais fiadores
INSERT INTO fiador (cpf, nome, saldo, tel, inquilino_cpf) VALUES
(99900011122, 'Marcos Borges', 25000.00, '(11) 934567890', 77788899900),
(11122233300, 'Cláudia Tavares', 30000.00, '(21) 945678901', 88899900011);
(22233344455, 'Lucas Mendes', 15000.00, '(61) 912345678', 77788899900),
(33344455566, 'Ana Paula Silva', 18000.00, '(71) 987654321', 77788899900),
(45667744556, 'Jorge Almeida', 22000.00, '(81) 923456789', 88899900011),
(66755678875, 'Maria Eduarda Santos', 25000.00, '(91) 956789012', 88899900011); 
(33344455566, 'Ana Paula Silva', 18000.00, '(71) 987654321', 77788899900), -- Terceiro fiador para inquilino 77788899900
(45667744556, 'Jorge Almeida', 22000.00, '(81) 923456789', 88899900011), -- Segundo fiador para inquilino 88899900011
(66755678875, 'Maria Eduarda Santos', 25000.00, '(91) 956789012', 88899900011); -- Terceiro fiador para inquilino 88899900011
(477866677555, 'Fernanda Lima', 15000.00, '(61) 912345678', 11122233344),
(551564664783, 'Ricardo Ribeiro', 20000.00, '(71) 923456789', 22233344455);

-- Inserir mais imóveis
INSERT INTO imovel (endereco, nComodos, nVagas, m2Construido, dataCadastro, aluguel, corretor_creci, proprietario_cpf) VALUES
('Rua Verde, 789, Belo Horizonte, MG', 3, 1, 120, '2022-03-10', 2000.00, 33445566, 44455566677),
('Avenida Paulista, 1000, São Paulo, SP', 4, 2, 180, '2022-04-15', 4000.00, 44556677, 55566677788),
('Rua das Palmeiras, 456, Salvador, BA', 2, 0, 90, '2022-05-20', 1500.00, 55667788, 66677788899);

-- Inserir mais propostas
INSERT INTO proposta (cliente_cpf, imovel_id, data, valor, validade) VALUES
(77788899900, 3, '2023-02-15', 1900.00, '2023-03-15'),
(88899900011, 4, '2023-02-20', 3900.00, '2023-03-20');

-- Inserir mais visitas
INSERT INTO visita (data, cliente_cpf, corretor_creci) VALUES
('2023-02-10 09:00:00', 77788899900, 33445566),
('2023-02-15 15:00:00', 88899900011, 44556677);

-- Inserir mais contratos
INSERT INTO contrato (proprietario_cpf, inquilino_cpf, imovel_id, valor, inicio, fim) VALUES
(44455566677, 77788899900, 3, 1900, '2022-02-15','2024-02-15'),
(55566677788, 88899900011, 4, 3900, '2022-02-20, '2024-02-20');


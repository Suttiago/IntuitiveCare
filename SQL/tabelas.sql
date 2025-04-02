CREATE TABLE operadoras_ativas (
    id SERIAL PRIMARY KEY,
    registro_ans VARCHAR(20) UNIQUE,
    cnpj VARCHAR(18),
    razao_social VARCHAR(255),
    modalidade VARCHAR(100),
    uf VARCHAR(2),
    municipio VARCHAR(100)
);

CREATE TABLE demonstracoes_contabeis (
    id SERIAL PRIMARY KEY,
    ano INT,
    registro_ans VARCHAR(20),
    descricao VARCHAR(255),
    valor NUMERIC(18,2)
);

from sqlalchemy import Column, Integer, String, Numeric,Date
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "postgresql+psycopg2://postgres:root@localhost:5432/intuitivecare"
Base = declarative_base()

class OperadoraAtiva(Base):
    __tablename__ = "operadoras_ativas"

    id = Column(Integer, primary_key=True)
    registro_ans = Column(String(20), unique=True)
    cnpj = Column(String(18))
    razao_social = Column(String(255))
    nome_fantasia = Column(String(255))
    modalidade = Column(String(100))
    logradouro = Column(String(255))
    numero = Column(String(10))
    complemento = Column(String(255))
    bairro = Column(String(255))
    cidade = Column(String(255))
    uf = Column(String(2))
    cep = Column(String(50))
    ddd = Column(String(2))
    telefone = Column(String(50))
    fax = Column(String(50))
    endereco_eletronico = Column(String(255))
    representante = Column(String(255))
    cargo_representante = Column(String(255))
    regiao_de_comercio = Column(String(255))
    data_registro_ans = Column(String(255))
    municipio = Column(String(100))
    
    
class DemonstracaoContabil(Base):
    __tablename__ = "demonstracoes_contabeis"

    id = Column(Integer, primary_key=True)
    ano = Column(Date)
    reg_ans = Column(String(20))
    cd_conta_contabil = Column(String(255))
    descricao = Column(String(255))
    vl_saldo_inicial = Column(Numeric)
    vl_saldo_final = Column(Numeric)
    
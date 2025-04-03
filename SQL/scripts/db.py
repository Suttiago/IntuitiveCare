from sqlalchemy import create_engine, Column, Integer, String, Numeric,Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

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
    
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

#Base.metadata.create_all(engine)
#print("✔ Tabelas criadas com sucesso!")

import os
import csv


#VER ISSO E ORGANIZAR
csv_directory = 'SQL/scripts/dados_operadoras/dados_csv'

def importar_operadoras(csv_directory):
    """Importa os dados de todos os arquivos CSV no diretório para a tabela operadoras_ativas."""
    for filename in os.listdir(csv_directory):
        if filename.endswith(".csv"):  # Verifica se o arquivo é um CSV
            file_path = os.path.join(csv_directory, filename)
            print(f"Importando arquivo: {file_path}")
            with open(file_path, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f, delimiter=";")
                reader.fieldnames = [name.strip() for name in reader.fieldnames]  # Remove espaços extras
                for row in reader:
                    print(row.keys())  # Exibe as chaves lidas do CSV
                    operadora = OperadoraAtiva(
                        registro_ans=row["Registro_ANS"],
                        cnpj=row["CNPJ"],
                        razao_social=row["Razao_Social"],
                        nome_fantasia=row["Nome_Fantasia"],
                        modalidade=row["Modalidade"],
                        logradouro=row["Logradouro"],
                        numero=row["Numero"],
                        complemento=row["Complemento"],
                        bairro=row["Bairro"],
                        cidade=row["Cidade"],
                        uf=row["UF"],
                        cep=row["CEP"],
                        ddd=row["DDD"],
                        telefone=row["Telefone"],
                        fax=row["Fax"],
                        endereco_eletronico=row["Endereco_eletronico"],
                        representante=row["Representante"],
                        cargo_representante=row["Cargo_Representante"],
                        regiao_de_comercio=row["Regiao_de_Comercializacao"],
                        data_registro_ans=row["Data_Registro_ANS"],
                        municipio=row.get("Municipio", None)  # Caso o campo não exista
                    )
                    session.add(operadora)
                session.commit()
            print(f"✔ Dados importados do arquivo: {file_path}")
# Chamar a função para importar os dados
importar_operadoras(csv_directory)
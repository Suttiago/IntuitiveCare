import os
import csv
from db import session
from models import OperadoraAtiva

def importar_operadoras(csv_directory):
    for filename in os.listdir(csv_directory):
        if filename.endswith(".csv"): 
            file_path = os.path.join(csv_directory, filename)
            print(f"Importando arquivo: {file_path}")
            with open(file_path, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f, delimiter=";")
                reader.fieldnames = [name.strip() for name in reader.fieldnames]  # Remove espaços extras
                for row in reader:
                    print(row.keys()) 
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
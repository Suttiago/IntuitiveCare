import pandas as pd
import pdfplumber
from zipfile import ZipFile

pdf_caminho = "app/data/dados_puros/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"

def extrair_tabelas(pdf_caminho):
    data = []
    with pdfplumber.open(pdf_caminho) as pdf:
        for page in pdf.pages:
            table = page.extract_table()
            if table:  # Verifica se há uma tabela antes de processar
                data.extend(table)
    return data

csv_path = "app/data/dados_puros/tiago.csv"

def salvar_csv(data, csv_path):
    if not data:
        print("Nenhuma tabela encontrada no PDF.")
        return

    df = pd.DataFrame(data[1:], columns=data[0])

    abreviacao = {'OD': 'ODONTOLOGIA', 'AMD': 'AMBULATORIAL'}
    df.replace(abreviacao, inplace=True)

    df.to_csv(csv_path, index=False, encoding="utf-8-sig")
    print(f"✔ CSV salvo: {csv_path}")


def csv_to_zip(csv_path):
    zip_path = "app/data/zip/Teste_Tiago_Sversut.zip"
    with ZipFile(zip_path, 'w') as zipf:
        zipf.write(csv_path)

if __name__ == "__main__":
    dados_extraidos = extrair_tabelas(pdf_caminho)
    salvar_csv(dados_extraidos, csv_path)
    csv_to_zip(csv_path)
import os
from bs4 import BeautifulSoup
import requests

url = 'https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/'

response = requests.get(url)
DATA_PATH = 'SQL/scripts/dados_operadoras'
EXTRACT_PATH = os.path.join(DATA_PATH, "dados_csv/operadoras")


def listar_csv():
    soup = BeautifulSoup(response.text, "html.parser")
    csv = []
    
    for link in soup.find_all('a', href=True):  
        if link['href'].endswith('.csv'):
            csv.append(url + link['href']) 
    return csv


def baixar_csv(csv):

    for csvlink in csv:
        nome_arquivo = os.path.join(EXTRACT_PATH, os.path.basename(csvlink))
        
        response = requests.get(csvlink)
        if response.status_code == 200:
            with open(nome_arquivo, "wb") as f:
                f.write(response.content)
            print(f"Arquivo salvo: {nome_arquivo}")
        else:
            print(f"Falha ao baixar: {csvlink}")


if __name__ == "__main__":
    csv_links = listar_csv()
    baixar_csv(csv_links)

import os
from bs4 import BeautifulSoup
import requests

url = 'https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/'

response = requests.get(url)
CSV_PATH = 'app/banco/dados/dados_csv_operadoras'  # Diretório para salvar os arquivos CSV
ZIP_PATH = 'app/banco/dados/zip_files'  # Diretório para salvar os arquivos ZIP

# Garante que os diretórios de destino existem
os.makedirs(CSV_PATH, exist_ok=True)
os.makedirs(ZIP_PATH, exist_ok=True)

def listar_csv():
    """Lista os links para os arquivos CSV disponíveis na página."""
    soup = BeautifulSoup(response.text, "html.parser")
    csv_links = []
    
    for link in soup.find_all('a', href=True):  
        if link['href'].endswith('.csv'):
            csv_links.append(url + link['href']) 
    return csv_links

def baixar_csv(csv_links):
    """Baixa os arquivos CSV e salva no diretório especificado."""
    for csvlink in csv_links:
        nome_arquivo = os.path.join(CSV_PATH, os.path.basename(csvlink))  # Salva no diretório CSV_PATH
        
        response = requests.get(csvlink)
        if response.status_code == 200:
            with open(nome_arquivo, "wb") as f:
                f.write(response.content)
            print(f"✔ Arquivo CSV salvo: {nome_arquivo}")
        else:
            print(f"✖ Falha ao baixar: {csvlink}")
if __name__ == "__main__":
    csv_links = listar_csv()
    baixar_csv(csv_links)

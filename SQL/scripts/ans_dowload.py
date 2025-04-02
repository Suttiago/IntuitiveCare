import requests
import os
from bs4 import BeautifulSoup
from datetime import datetime
from zipfile import ZipFile

DATA_PATH = 'SQL/scripts/dados_operadoras'
ZIP_PATH = os.path.join(DATA_PATH, "zip_files")
EXTRACT_PATH = os.path.join(DATA_PATH, "extracted_files")
os.makedirs(ZIP_PATH, exist_ok=True)
os.makedirs(EXTRACT_PATH, exist_ok=True)

URL = 'https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/'

ANO_PASSADO = datetime.now().year - 1
ANO_RETRASADO = ANO_PASSADO - 1


def listar_subdiretorios(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    subdiretorios = []
    for link in soup.find_all('a', href=True):
        href = link.get('href')
        if href.endswith('/') and (str(ANO_PASSADO) in href or str(ANO_RETRASADO) in href):
            subdiretorios.append(url + href)
    
    return subdiretorios


def listar_arquivos_zip(subdiretorios):

    arquivos_zip = []
    for subdir in subdiretorios:
        response = requests.get(subdir)
        soup = BeautifulSoup(response.text, "html.parser")
        
        for link in soup.find_all("a", href=True):
            href = link.get("href")
            if href.endswith(".zip"):  
                arquivos_zip.append(subdir + href)
    
    return arquivos_zip


def baixar_arquivos(arquivos):

    for arquivo_url in arquivos:
        nome_arquivo = arquivo_url.split("/")[-1]  
        destino = os.path.join(ZIP_PATH, nome_arquivo)

        response = requests.get(arquivo_url)
        if response.status_code == 200:
            with open(destino, "wb") as f:
                f.write(response.content)
            print(f"✔ Arquivo ZIP baixado: {nome_arquivo}")
        else:
            print(f"✖ Falha ao baixar: {arquivo_url}")

def extrair_arquivos():
    for arquivo_zip in os.listdir(ZIP_PATH):
        caminho_zip = os.path.join(ZIP_PATH, arquivo_zip)
        if arquivo_zip.endswith(".zip"):
            with ZipFile(caminho_zip, 'r') as zipf:
                zipf.extractall(EXTRACT_PATH)
                

if __name__ == "__main__":
    subdiretorios = listar_subdiretorios(URL)

    arquivos_zip = listar_arquivos_zip(subdiretorios)

    baixar_arquivos(arquivos_zip)
    
    extrair_arquivos()
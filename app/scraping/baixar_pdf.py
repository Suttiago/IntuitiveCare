import os
import requests
from bs4 import BeautifulSoup
from zipfile import ZipFile

URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

BRUTOS_DIR = os.path.join("data", "brutos")
ZIP_DIR = os.path.join("data", "zip")

def criar_diretorios():
    os.makedirs(BRUTOS_DIR, exist_ok=True)
    os.makedirs(ZIP_DIR, exist_ok=True)

def pegar_pdfs(url):
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")

    pdfs = []

    for link in soup.find_all('a', href=True):
        if "Anexo" in link.text and link['href'].endswith('.pdf'):
            pdfs.append(link["href"])

    print(f"PDFs encontrados: {pdfs}")
    return pdfs


def baixar_pdfs(pdfs):
    for pdf_url in pdfs:
        pdf_name = pdf_url.split('/')[-1]
        pdf_caminho = os.path.join(BRUTOS_DIR, pdf_name)
        
        with open(pdf_caminho, "wb") as f:
            f.write(requests.get(pdf_url).content)
        print(f"✔ PDF baixado: {pdf_name}")

def to_zip():
    zip_name = os.path.join(ZIP_DIR, 'anexos.zip')
    with ZipFile(zip_name, 'w') as zipf:
        for pdf_file in os.listdir(BRUTOS_DIR):
            zipf.write(os.path.join(BRUTOS_DIR, pdf_file), pdf_file)
        print(f"✔ Arquivo ZIP criado: {zip_name}")
        
if __name__ == "__main__":
    criar_diretorios()
    pdf_links = pegar_pdfs(URL)
    baixar_pdfs(pdf_links)
    to_zip()
from banco.scripts.importers.operadoras_importa import importar_operadoras

def main():
    # Caminho do diretório CSV
    csv_directory = r'c:\Users\tiago.sversut\Desktop\teste (2)\IntuitiveCare\app\banco\dados\dados_operadoras\dados_csv\operadoras'
    
    # Testar a importação de operadoras
    print("Iniciando a importação de operadoras...")
    importar_operadoras(csv_directory)
    print("✔ Importação concluída com sucesso!")

if __name__ == "__main__":
    main()
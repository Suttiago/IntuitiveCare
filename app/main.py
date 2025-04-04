from api.app import app
import os
#from banco.scripts.importers.contabilidade_importa import importar_contabilidade
def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_contabilidade = os.path.join(base_dir, "banco", "dados", "dados_operadoras", "dados_csv", "demonstracao_contabil")
    #importar_contabilidade(csv_contabilidade)
    app.run(debug=True,port='8080',host='0.0.0.0')

if __name__ == "__main__":
    main()
from api.app import app
import os
def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_contabilidade = os.path.join(base_dir, "banco", "dados", "dados_operadoras", "dados_csv", "demonstracao_contabil")
    app.run(debug=True,port='8080',host='0.0.0.0')

if __name__ == "__main__":
    main()
from flask import Flask, jsonify
from sqlalchemy.orm import sessionmaker
from banco.scripts.db import engine
from banco.scripts.models import OperadoraAtiva

app = Flask(__name__)

# Configuração da sessão do banco de dados
Session = sessionmaker(bind=engine)

@app.route("/operadoras", methods=["PUT"])
def listar_operadoras():
    # Cria uma sessão do banco de dados
    session = Session()
    try:
        # Consulta todas as operadoras ativas
        operadoras = session.query(OperadoraAtiva).all()
        # Serializa os resultados para JSON
        resultado = [
            {
                "id": op.id,
                "registro_ans": op.registro_ans,
                "razao_social": op.razao_social,
                "nome_fantasia": op.nome_fantasia,
                "modalidade": op.modalidade,
                "cidade": op.cidade,
                "uf": op.uf,
            }
            for op in operadoras
        ]
        return jsonify(resultado)
    finally:
        # Fecha a sessão do banco de dados
        session.close()

if __name__ == "__main__":
    app.run(debug=True, port=8000)
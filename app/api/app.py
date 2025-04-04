from flask import Flask, jsonify
from sqlalchemy.orm import sessionmaker
from banco.scripts.db import engine, session
from banco.scripts.models import OperadoraAtiva
from banco.scripts.querys import query_operadoras_10anos
app = Flask(__name__)

@app.route("/operadoras", methods=["get"])
def listar_operadoras():
    try:
        operadoras = query_operadoras_10anos(session)
        resultado = [
            {
              "registro_ans": op[0],
                "razao_social": op[1],
                "descricao": op[2],
                "total_despesas": op[3],
            }
            for op in operadoras
        ]
        return jsonify(resultado)
    finally:
        # Fecha a sessão do banco de dados
        session.close()

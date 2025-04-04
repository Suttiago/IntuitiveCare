from flask import Flask, request, jsonify
from flask_cors import CORS
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from banco.scripts.db import engine, session
from banco.scripts.models import OperadoraAtiva

app = Flask(__name__)
CORS(app)

@app.route("/operadoras", methods=["GET"])
def buscar_operadoras():
    termo_busca = request.args.get("q", "").strip()

    if not termo_busca:
        return jsonify({"erro": "Parâmetro de busca ausente"}), 400

    print(f"Buscando por: {termo_busca}")  # Debug: Verifica se o termo de busca chega corretamente

    try:
        operadoras = (
            session.query(OperadoraAtiva)
            .filter(func.lower(OperadoraAtiva.nome_fantasia).like(f"%{termo_busca.lower()}%"))  # Para MySQL e compatibilidade geral
            .order_by(OperadoraAtiva.nome_fantasia)
            .all()
        )

        if not operadoras:
            return jsonify({"mensagem": "Nenhuma operadora encontrada para essa busca."}), 404

        resultado = [
            {
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
        session.close()
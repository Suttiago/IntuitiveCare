from sqlalchemy.orm import aliased
from sqlalchemy import func, desc, and_, or_
from banco.scripts.db import session
from banco.scripts.models import OperadoraAtiva, DemonstracaoContabil
from datetime import datetime

# Definir o início do ano passado
ano_passado = datetime(datetime.now().year - 1, 1, 1)

def query_operadoras_10anos(session):
    query = (
        session.query(
            OperadoraAtiva.registro_ans,
            OperadoraAtiva.razao_social,
            DemonstracaoContabil.descricao,
            func.sum(DemonstracaoContabil.vl_saldo_final - DemonstracaoContabil.vl_saldo_inicial).label("total_despesas")
        )
        .join(DemonstracaoContabil, DemonstracaoContabil.reg_ans == OperadoraAtiva.registro_ans)
        .where(
            and_(
                DemonstracaoContabil.ano >= ano_passado,
                or_(
                    DemonstracaoContabil.descricao.ilike('%EVENTOS%'),
                    DemonstracaoContabil.descricao.ilike('%SINISTROS%'),
                    DemonstracaoContabil.descricao.ilike('%AVISADOS%'),
                    DemonstracaoContabil.descricao.ilike('%MEDICO HOSPITALAR%')
                )
            )
        )
        .group_by(OperadoraAtiva.registro_ans, OperadoraAtiva.razao_social, DemonstracaoContabil.descricao)
        .order_by(desc("total_despesas"))
        .limit(10)
    )

    return query.all()  # Retornar os resultados corretamente
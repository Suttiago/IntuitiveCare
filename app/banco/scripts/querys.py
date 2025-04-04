from sqlalchemy.orm import aliased
from sqlalchemy import func, desc, and_
from db import session
from models import OperadoraAtiva, DemonstracaoContabil
from datetime import datetime

ano_passado = datetime(datetime.now().year -1,1,1)
def query_operadoras_10anos ():
    query = (
        session.query(
            OperadoraAtiva.registro_ans,
            OperadoraAtiva.razao_social,
            DemonstracaoContabil.descricao,
            func.sum(DemonstracaoContabil.vl_saldo_final - DemonstracaoContabil.vl_saldo_inicial).label("total_despesas")
        )
        .join(DemonstracaoContabil, DemonstracaoContabil.reg_ans==OperadoraAtiva.registro_ans)
        .where(
        and_(
            DemonstracaoContabil.ano >= ano_passado,
            DemonstracaoContabil.descricao.ilike('%EVENTOS% %SINISTROS% %AVISADOS% %MEDICO HOSPITALAR%')
        )
        )
        .group_by(OperadoraAtiva.registro_ans, OperadoraAtiva.razao_social, DemonstracaoContabil.descricao)
        .order_by(desc('total_despesas'))
        .limit(10)
        
    )


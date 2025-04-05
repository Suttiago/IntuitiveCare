import os
import csv
from banco.scripts.db import session
from banco.scripts.models import DemonstracaoContabil
def importar_contabilidade(csv_contabilidade):
    for filename in os.listdir(csv_contabilidade):
        if filename.endswith(".csv"):
            file_path = os.path.join(csv_contabilidade, filename)
            print(f"Importando arquivo: {file_path}")
            with open(file_path, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f, delimiter=";")
                reader.fieldnames = [name.strip() for name in reader.fieldnames]  # Remove espaços extras
                for row in reader:
                    # Converte valores numéricos para o formato correto
                    vl_saldo_inicial = float(row["VL_SALDO_INICIAL"].replace(",", "."))
                    vl_saldo_final = float(row["VL_SALDO_FINAL"].replace(",", "."))
                    
                    demonstracao = DemonstracaoContabil(
                        ano=row["DATA"],
                        reg_ans=row["REG_ANS"],
                        cd_conta_contabil=row["CD_CONTA_CONTABIL"],
                        descricao=row["DESCRICAO"],
                        vl_saldo_inicial=vl_saldo_inicial,
                        vl_saldo_final=vl_saldo_final
                    )
                    session.add(demonstracao)
                session.commit()
            print(f"✔ Dados importados do arquivo: {file_path}")
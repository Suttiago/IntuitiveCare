
-- nao consegui executar--
SELECT 
    o.registro_ans, 
    o.razao_social, 
	d.descricao,
    SUM(d.vl_saldo_final - d.vl_saldo_inicial) AS total_despesas
FROM demonstracoes_contabeis d
JOIN operadoras_ativas o ON d.reg_ans = o.registro_ans
WHERE 
    d.descricao ILIKE'%EVENTOS% %SINISTROS% %AVISADOS% %MEDICO HOSPITALAR%'
	--AND
    --d.ano >= (CURRENT_DATE - INTERVAL '6 months')
GROUP BY o.registro_ans, o.razao_social,d.descricao
ORDER BY total_despesas DESC
LIMIT 10;





-- operadoras com maiores despesas no ultimo ano--
SELECT 
    o.registro_ans, 
    o.razao_social, 
	d.descricao,
    SUM(d.vl_saldo_final - d.vl_saldo_inicial) AS total_despesas
FROM demonstracoes_contabeis d
JOIN operadoras_ativas o ON d.reg_ans = o.registro_ans
WHERE 
    d.descricao ILIKE'%EVENTOS% %SINISTROS% %AVISADOS% %MEDICO HOSPITALAR%'
	AND
    d.ano >= (CURRENT_DATE - INTERVAL '1 year')
GROUP BY o.registro_ans, o.razao_social,d.descricao
ORDER BY total_despesas DESC
LIMIT 10;

-- Salve este SQL para usar com con.execute(query)
SELECT 
    -- FASE 1: SNAPSHOT BASELINE (Camada Cadastral)
    app.SK_ID_CURR,
    app.TARGET,
    app.AMT_INCOME_TOTAL,
    app.AMT_CREDIT,
    app.DAYS_BIRTH,
    app.EXT_SOURCE_1,
    app.EXT_SOURCE_2,
    app.EXT_SOURCE_3,

    -- FASE 2: HISTORICAL BEHAVIOR (BUREAU - Relacionamento Externo)
    -- Descomente as linhas abaixo quando iniciar a Fase 2
    /*
    b.BUREAU_LOAN_COUNT,
    b.BUREAU_DEBT_SUM,
    b.BUREAU_IS_OVERDUE,
    */

    -- FASE 3: LIFECYCLE & LOYALTY (PREV_APP - Relacionamento Interno)
    -- Descomente as linhas abaixo quando iniciar a Fase 3
    /*
    p.PREV_APP_COUNT,
    p.REFUSAL_RATE,
    p.AVG_TERM_MONTHS
    */

FROM read_parquet('data/bronze/application_train.parquet') app

-- JOIN FASE 2
/*
LEFT JOIN (
    SELECT 
        SK_ID_CURR,
        COUNT(SK_ID_BUREAU) as BUREAU_LOAN_COUNT,
        SUM(AMT_CREDIT_SUM) as BUREAU_DEBT_SUM,
        MAX(CAST(CREDIT_DAY_OVERDUE > 0 AS INT)) as BUREAU_IS_OVERDUE
    FROM read_parquet('data/bronze/bureau.parquet')
    GROUP BY SK_ID_CURR
) b ON app.SK_ID_CURR = b.SK_ID_CURR
*/

-- JOIN FASE 3
/*
LEFT JOIN (
    SELECT 
        SK_ID_CURR,
        COUNT(SK_ID_PREV) as PREV_APP_COUNT,
        AVG(CAST(NAME_CONTRACT_STATUS = 'Refused' AS INT)) as REFUSAL_RATE,
        AVG(CNT_PAYMENT) as AVG_TERM_MONTHS
    FROM read_parquet('data/bronze/previous_application.parquet')
    GROUP BY SK_ID_CURR
) p ON app.SK_ID_CURR = p.SK_ID_CURR
*/





-- =========
/*
import duckdb

def get_abt_phase(phase=1):
    con = duckdb.connect()
    
    # Aqui você carrega o SQL acima e usa f-strings ou 
    # manipulação de string para descomentar as fases
    # Ou simplesmente tenha 3 versões da query.
    
    df_pl = con.execute(query_fase_selecionada).pl()
    return df_pl
*/


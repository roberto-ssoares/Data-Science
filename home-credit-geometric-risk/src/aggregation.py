import duckdb
import polars as pl

def create_master_abt(bronze_path="data/bronze/"):
    """
    Cria a ABT consolidada unindo as tabelas de treino, bureau e histórico interno.
    Utiliza DuckDB para agregação SQL de alta performance direto nos Parquets.
    """
    con = duckdb.connect()
    
    print("🧠 Consolidando ABT Mestre via DuckDB...")
    
    # Query SQL: Agregações Estratégicas + Joins
    query = f"""
    WITH bureau_agg AS (
        SELECT 
            SK_ID_CURR,
            COUNT(SK_ID_BUREAU) as B_CNT_LOANS,
            AVG(AMT_CREDIT_SUM) as B_AVG_CREDIT,
            SUM(CREDIT_DAY_OVERDUE) as B_TOTAL_OVERDUE,
            MAX(DAYS_CREDIT) as B_DAYS_LAST_LOAN
        FROM read_parquet('{bronze_path}bureau.parquet')
        GROUP BY SK_ID_CURR
    ),
    prev_agg AS (
        SELECT 
            SK_ID_CURR,
            COUNT(SK_ID_PREV) as P_CNT_APPS,
            AVG(AMT_APPLICATION) as P_AVG_APP_AMT,
            AVG(CAST(NAME_CONTRACT_STATUS = 'Refused' AS INT)) as P_REFUSAL_RATE,
            MAX(DAYS_DECISION) as P_DAYS_LAST_DECISION
        FROM read_parquet('{bronze_path}previous_application.parquet')
        GROUP BY SK_ID_CURR
    )
    SELECT 
        app.*,
        b.* EXCLUDE (SK_ID_CURR),
        p.* EXCLUDE (SK_ID_CURR)
    FROM read_parquet('{bronze_path}application_train.parquet') app
    LEFT JOIN bureau_agg b ON app.SK_ID_CURR = b.SK_ID_CURR
    LEFT JOIN prev_agg p ON app.SK_ID_CURR = p.SK_ID_CURR
    """
    
    # Executa e converte para Polars (df_abt)
    df_abt = con.execute(query).pl()
    
    # Limpeza básica de NaNs (Preenchendo agregações vazias com 0)
    # No Polars, isso é extremamente rápido
    cols_to_fill_zero = [c for c in df_abt.columns if c.startswith(('B_', 'P_'))]
    df_abt = df_abt.with_columns([
        pl.col(c).fill_null(0) for c in cols_to_fill_zero
    ])
    
    print(f"✅ ABT Criada! Shape: {df_abt.shape}")
    con.close()
    
    return df_abt

# df_master = create_master_abt()

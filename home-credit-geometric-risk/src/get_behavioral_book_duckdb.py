import duckdb
import polars as pl

def get_behavioral_book_duckdb(bronze_path="data/bronze/"):
    """Usa DuckDB para agregar milhões de linhas sem estourar a RAM."""
    con = duckdb.connect()
    
    print("🦆 Agregando Bureau e Previous Application via DuckDB...")
    
    # SQL direto nos arquivos Parquet (zero cópia de memória)
    query = f"""
    SELECT 
        curr.SK_ID_CURR,
        AVG(b.AMT_CREDIT_SUM) as BUREAU_CREDIT_AVG,
        SUM(b.CREDIT_DAY_OVERDUE) as BUREAU_OVERDUE_SUM,
        COUNT(prev.SK_ID_PREV) as PREV_APP_COUNT,
        AVG(CAST(prev.NAME_CONTRACT_STATUS = 'Refused' AS INT)) as REFUSAL_RATE
    FROM read_parquet('{bronze_path}application_train.parquet') curr
    LEFT JOIN read_parquet('{bronze_path}bureau.parquet') b 
        ON curr.SK_ID_CURR = b.SK_ID_CURR
    LEFT JOIN read_parquet('{bronze_path}previous_application.parquet') prev 
        ON curr.SK_ID_CURR = prev.SK_ID_CURR
    GROUP BY curr.SK_ID_CURR
    """
    
    # Exporta o resultado diretamente para um DataFrame Polars
    df_abt = con.execute(query).pl()
    return df_abt

# df_abt = get_behavioral_book_duckdb()

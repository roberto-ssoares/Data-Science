def prep_geometric_input(df_pl, features_ancora):
    """Limpeza e Escalonamento veloz com Polars."""
    
    # 1. Tratar NaNs de forma expressiva
    df_clean = df_pl.with_columns([
        pl.col(c).fill_null(0) if "SUM" in c or "COUNT" in c else pl.col(c).fill_null(pl.col(c).median())
        for c in features_ancora
    ])
    
    # 2. Conversão para NumPy (necessário para o K-NN e Ricci)
    # O Polars faz isso de forma muito eficiente
    X = df_clean.select(features_ancora).to_numpy()
    
    return X, df_clean.select("SK_ID_CURR").to_numpy().flatten()

# X_matrix, ids = prep_geometric_input(df_abt, ['BUREAU_CREDIT_AVG', 'REFUSAL_RATE'])

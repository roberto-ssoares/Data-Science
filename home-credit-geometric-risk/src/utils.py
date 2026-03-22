import time
from functools import wraps

def monitor_performance(func):
    """Decorador para medir o tempo de execução de etapas do pipeline."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        print(f"⏱️  Iniciando: [{func.__name__}]...")
        
        result = func(*args, **kwargs)
        
        end_time = time.perf_counter()
        duration = end_time - start_time
        
        # Converte para minutos se passar de 60 segundos
        if duration > 60:
            print(f"✅ Concluído: [{func.__name__}] em {duration/60:.2f} min")
        else:
            print(f"✅ Concluído: [{func.__name__}] em {duration:.2f} seg")
            
        return result
    return wrapper

# --- COMO USAR NO SEU PROJETO ---

@monitor_performance
def calcular_ricci_flow(G):
    # Seu código pesado de Ricci aqui...
    pass

@monitor_performance
def ingestao_duckdb():
    # Seu código de DuckDB aqui...
    pass

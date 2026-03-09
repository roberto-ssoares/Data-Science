# Rodar a partir da raiz do projeto
uv run python -c "from pathlib import Path; 
                  from podbank.config import default_config; 
                  from podbank.etl.bronze 
                  import promote_all_raw_to_bronze; 
                  cfg=default_config(Path('.').resolve()); 
                  promote_all_raw_to_bronze(cfg)"
# Manifesto dos Dados Sintéticos

Este documento registra os datasets sintéticos gerados pelo Notebook 01.

## Arquivos Gerados

### `clientes.parquet`

- Linhas: 5.000
- Colunas: 6
- Caminho: `data/synthetic/clientes.parquet`

### `contas.parquet`

- Linhas: 6.000
- Colunas: 6
- Caminho: `data/synthetic/contas.parquet`

### `dispositivos.parquet`

- Linhas: 4.500
- Colunas: 4
- Caminho: `data/synthetic/dispositivos.parquet`

### `ips.parquet`

- Linhas: 3.000
- Colunas: 4
- Caminho: `data/synthetic/ips.parquet`

### `beneficiarios.parquet`

- Linhas: 3.500
- Colunas: 4
- Caminho: `data/synthetic/beneficiarios.parquet`

### `cartoes.parquet`

- Linhas: 4.000
- Colunas: 5
- Caminho: `data/synthetic/cartoes.parquet`

### `transacoes.parquet`

- Linhas: 80.000
- Colunas: 13
- Caminho: `data/synthetic/transacoes.parquet`

### `labels_fraude.parquet`

- Linhas: 80.000
- Colunas: 4
- Caminho: `data/synthetic/labels_fraude.parquet`

## Distribuição dos Cenários de Fraude

| fraud_scenario           |   qtd_transacoes |   percentual |
|:-------------------------|-----------------:|-------------:|
| normal                   |            73000 |       0.9125 |
| shared_device_ring       |             1600 |       0.02   |
| beneficiary_concentrator |             1400 |       0.0175 |
| burst_transactions       |             1200 |       0.015  |
| new_account_high_value   |             1000 |       0.0125 |
| coordinated_network      |             1000 |       0.0125 |
| bridge_account           |              800 |       0.01   |

## Observação

Os dados são sintéticos e foram criados exclusivamente para fins educacionais, analíticos e de portfólio.
Nenhum dado real de cliente, instituição financeira ou transação foi utilizado.

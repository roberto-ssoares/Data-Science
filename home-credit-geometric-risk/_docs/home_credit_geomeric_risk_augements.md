---

#### Comando "mágico" para o seu terminal (Linux, macOS ou Windows com Git Bash/WSL).

#### Ele cria toda a **arquitetura de pastas de nível Sênior** que desenhamos, incluindo os arquivos base, em um único clique:

```bash
mkdir -p home-credit-geometric-risk/{data/{raw,bronze,silver,gold},src,notebooks,docs,tests,images} && \
touch home-credit-geometric-risk/src/{__init__,ingestion,aggregation,feature_selection,graph_engine,pipeline}.py && \
touch home-credit-geometric-risk/{requirements.txt,.gitignore,README.md} && \
echo "Estrutura do projeto 'Home Credit Geometric Risk' criada com sucesso! 🚀"
```

```textile
rss-linux@PC-ROBERTO:/mnt/d/_DS-Projects/home-credit-geometric-risk$ tree
.
├── README.md
├── _docs
│   └── home_credit_geomeric_risk_augements.md
├── data
│   ├── 00-raw
│   │   ├── HomeCredit_Dicionario_de_Dados.csv
│   │   ├── POS_CASH_balance.csv
│   │   ├── application_test.csv
│   │   ├── application_train.csv
│   │   ├── bureau.csv
│   │   ├── bureau_balance.csv
│   │   ├── credit_card_balance.csv
│   │   ├── installments_payments.csv
│   │   └── previous_application.csv
│   ├── 01-bronze
│   ├── 02-silver
│   └── 03-gold
├── docs
├── images
├── notebooks
├── requirements.txt
├── src
│   ├── __init__.py
│   ├── aggregation.py
│   ├── feature_selection.py
│   ├── graph_engine.py
│   ├── ingestion.py
│   └── pipeline.py
└── tests

12 directories, 18 files
```

🏁 O que este comando fez por você:

1. **`data/`**: Criou as subpastas para as camadas **Raw** (CSVs), **Bronze** (Parquets), **Silver** (ABTs) e **Gold** (Features Geométricas).
2. **`src/`**: Criou todos os arquivos `.py` modulares que discutimos (Ingestão, Agregação, Motor de Grafo, etc.).
3. **Root**: Criou os arquivos de configuração (`requirements.txt`, `.gitignore`) e o seu `README.md`.
4. **Imagens & Docs**: Pastas prontas para receber os seus **Scatter Plots 3D** e a documentação do projeto.

---

O `venv` evita que você quebre as bibliotecas do próprio sistema operacional (como o `apt` ou o instalador de drivers) ao instalar versões específicas de pacotes de dados.

E sobre o **uv**: **use sem medo**. O `uv` é atualmente a ferramenta mais rápida e moderna do ecossistema Python (escrita em Rust). Ele substitui o `pip`, o `venv` e o `pip-tools` com uma velocidade absurda.

Aqui estão os comandos para você iniciar seu projeto com **`uv`** e garantir um **DX (Developer Experience)** de última geração:

```bash
# 1. Instale o uv (caso ainda não tenha)
curl -LsSf https://astral-sh.dev | sh

# 2. Vá para a pasta do projeto
cd home-credit-geometric-risk

# 3. Crie o ambiente virtual (instantâneo com uv)
uv venv

# 4. Ative o ambiente
source .venv/bin/activate

# 5. Instale suas dependências do requirements.txt (muito mais rápido que o pip)
uv pip install -r requirements.txt
```

💎 Por que o `uv` é o "pulo do gato" aqui?

1. **Velocidade:** Ele instala pacotes em milissegundos usando um cache global.
2. **Resolução de Conflitos:** Se houver incompatibilidade entre as versões do `NetworkX` e do `GraphRicciCurvature`, o `uv` resolve isso de forma muito mais inteligente que o `pip` padrão.
3. **Sincronização:** Você pode usar `uv pip compile` para gerar um arquivo `requirements.txt` travado com hashes de segurança, elevando o nível de **Governança** do seu projeto.

---

Para manter o seu **DX (Developer Experience)** no estado da arte, o `uv` permite gerenciar dependências de forma declarativa e extremamente veloz.

Aqui está o comando para instalar uma nova biblioteca (ex: `polars`) e já atualizar o seu arquivo de dependências:

```bash
# Instala a lib e gera/atualiza o arquivo de travas de forma limpa
uv pip install polars && uv pip freeze > requirements.txt
```

💡 Dica de Fluxo Sênior com `uv`:

Se você quiser ser ainda mais rigoroso com a **reprodutibilidade**, pode usar o `uv` para criar um arquivo `requirements.in` (apenas com os nomes das libs) e compilar para o `requirements.txt` (com as versões exatas e hashes):

```bash
# 1. Cria o arquivo de entrada
echo "polars" >> requirements.in
echo "duckdb" >> requirements.in

# 2. Compila para o formato travado (mais seguro para produção)
uv pip compile requirements.in -o requirements.txt
```

---

🏁 Tudo pronto para a Fase 1!

Você agora tem:

1. **Ambiente Isolado:** `uv venv` (Segurança no Linux).
2. **Performance de Instalação:** `uv pip` (Velocidade de Rust).
3. **Gestão de Versões:** `requirements.txt` sempre atualizado.

**Vá em frente com a ingestão dos dados!** Quando o `DuckDB` terminar de criar o seu primeiro Parquet e você estiver pronto para rodar o **Sanity Check** do grafo, estarei aqui.

---

Para garantir que o seu ambiente **`uv`** seja ativado automaticamente sempre que você entrar na pasta do projeto (um **DX** de altíssimo nível), a melhor forma é adicionar um pequeno comando ao seu arquivo `.bashrc` ou usar uma ferramenta de automação.

Aqui estão as duas formas de fazer isso:

1. Forma Manual (Apenas o comando de ativação)

Toda vez que você abrir o terminal e entrar na pasta, basta digitar:

```bash
source .venv/bin/activate
```

2. Forma Automática (O "Pulo do Gato" do Desenvolvedor)

Se você usa **Linux**, pode adicionar esta função ao final do seu arquivo `~/.bashrc` (ou `~/.zshrc`). Ela detecta se existe uma pasta `.venv` no diretório atual e a ativa sozinha:

Adicione isso ao seu ~/.bashrc

```bash
cd() {
  builtin cd "$@"
  if [ -d ".venv" ]; then
    source .venv/bin/activate
    echo "🐍 Ambiente [uv] ativado automaticamente!"
  fi
}
```

*Depois de salvar, rode `source ~/.bashrc` para aplicar.*

3. A Alternativa Profissional: `direnv`

Se você quer algo ainda mais robusto e usado em grandes empresas, instale o **direnv**:

1. Instale: `sudo apt install direnv`
2. Na pasta do projeto, crie um arquivo chamado `.envrc`

```bash
echo "layout python-venv" > .envrc
```

1. Autorize: `direnv allow`  
   *Agora, sempre que você der `cd` na pasta, o ambiente sobe sozinho.*

---

🏁 Tudo pronto para o "Big Bang" dos Dados!

Você agora tem:

- **Velocidade de Rust** com o `uv`.
- **Isolamento Total** no Linux.
- **Automação de Ambiente** para focar apenas no código.

**Vá com tudo na Fase 1!** O DuckDB está esperando os seus CSVs para transformá-los no motor de ouro do seu projeto.

---

```
duckdb==0.9.2polars==0.19.19pyarrow==14.0.1networkx==3.1GraphRicciCurvature==0.5.3scikit-learn==1.3.2lightgbm==4.1.0numpy==1.26.2pandas==2.1.3tqdm==4.66.1matplotlib==3.8.2seaborn==0.13.0plotly==5.18.0kaleido==0.2.1
```

---

---

🚀 Graph-Based Feature Engineering: Ricci Curvature for Credit Risk

Este projeto implementa uma abordagem de **Geometria de Redes** para o desafio *Home Credit Default Risk*. Em vez de olhar apenas para os dados isolados de cada cliente, utilizamos a **Curvatura de Ricci (Ollivier & Forman)** para capturar a topologia do ecossistema financeiro e identificar perfis de risco latentes.

🧠 A Lógica: Por que Geometria?

Modelos tradicionais (XGBoost/LGBM) tratam cada cliente como um ponto independente. Ao construir um grafo de similaridade, transformamos o dataset em uma **variedade geométrica** onde:

- **Curvatura Positiva (Clusters):** Identifica grupos homogêneos e estáveis (ex: bons pagadores com perfis idênticos).
- **Curvatura Negativa (Pontes/Gargalos):** Identifica clientes "fronteira", que compartilham características de bons e maus pagadores — os casos mais difíceis de prever.

🛠️ Pipeline de Engenharia de Dados (ABT to Geometric)

O fluxo de processamento foi desenhado para maximizar o sinal vindo das tabelas satélites (`bureau` e `previous_application`):

1. **Agregação Comportamental:** Consolidação de histórico de dívidas e recusas de crédito em uma **Analytical Base Table (ABT)**.
2. **Null Importance Selection:** Filtro de ruído via permutação de target para selecionar apenas as 15-20 features com sinal real para o grafo.
3. **Construção do Grafo K-NN:** Criação de uma rede de vizinhança latente usando `RobustScaler` e busca de vizinhos esparsos.
4. **Extração de Ricci & Forman:**
   - `RICCI_AVG`: Localização geométrica no espaço de risco.
   - `RICCI_STD`: Instabilidade/Ambiguidade da vizinhança do cliente.
   - `FORMAN_AVG`: Importância estrutural (Hubs vs. Outliers).

📈 Resultados Esperados

- **Ganho de AUC:** A inclusão de métricas relacionais costuma adicionar informação não-linear que o modelo tabular sozinho não captura.
- **Robustez:** Melhor separação em clientes que estão nos "gargalos" do grafo, reduzindo falsos negativos.

---

Como ler os resultados:

| Feature             | Valor Alto                               | Valor Baixo                                 |
| ------------------- | ---------------------------------------- | ------------------------------------------- |
| **Ricci Curvature** | Cliente inserido em comunidade estável.  | Cliente agindo como "ponte" (Risco Amíguo). |
| **Ricci STD**       | Vizinhança heterogênea (Alta incerteza). | Vizinhança consistente (Perfil confiável).  |

---

**Dica de Colocação:** Se você for publicar isso no Kaggle, adicione o gráfico **KDE Plot** que criamos anteriormente logo abaixo deste texto. Ele prova visualmente que a sua feature geométrica separa os targets!

---

---

- Para fechar o projeto com uma validação estatística de peso, vamos comparar as suas novas **Features Geométricas** com as "Joias da Coroa" do Home Credit (as colunas `EXT_SOURCE`).

- No Kaggle, as `EXT_SOURCE_1, 2 e 3` são quase sempre as variáveis mais potentes. Se a sua **Curvatura de Ricci** mostrar uma correlação relevante ou complementar a elas, você terá uma feature extremamente robusta.

- Aqui está o código para gerar essa **Matriz de Correlação de Elite**:

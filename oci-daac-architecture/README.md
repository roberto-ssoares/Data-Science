# OCI DaaC Architecture

Projeto para criação de diagramas de arquitetura em OCI usando Diagram-as-Code (DaaC).

## Objetivos

- versionar diagramas de arquitetura em Git
- padronizar diagramas lógicos e físicos
- gerar artefatos para documentação, portfólio e apresentações
- reaproveitar templates OCI em projetos futuros

## Stack

- Python
- Diagrams
- Graphviz
- OCI Architecture Toolkit
- Draw.io

## Estrutura

- `diagrams_src/logical/`: diagramas lógicos
- `diagrams_src/physical/`: diagramas físicos
- `outputs/png/`: exportações PNG
- `outputs/svg/`: exportações SVG
- `docs/`: documentação da arquitetura

## Como executar

1. Instale o Graphviz no sistema operacional
2. Crie o ambiente virtual
3. Instale as dependências
4. Rode o script do diagrama

Exemplo:

```powershell
python diagrams_src/logical/hackathon_logical.py
```

A própria documentação do Diagrams usa exatamente esse fluxo de criação de scripts Python para gerar imagens de arquitetura. 

:contentReference[oaicite:3]{index=3}

---

# 1. Estrutura do projeto

Eu sugiro este repositório:

```text
oci-daac-architecture/  
├── README.md  
├── pyproject.toml  
├── requirements.txt  
├── .gitignore  
├── diagrams_src/  
│ ├── logical/  
│ │ └── hackathon_logical.py  
│ ├── physical/  
│ │ └── hackathon_physical.py  
│ └── common/  
│ └── naming.py  
├── outputs/  
│ ├── png/  
│ └── svg/  
├── docs/  
│ ├── arquitetura-logica.md  
│ ├── arquitetura-fisica.md  
│ └── decisoes-arquiteturais.md  
└── assets/  
 └── references/
```

Essa estrutura separa bem:

- **código-fonte dos diagramas**

- **artefatos gerados**

- **documentação**

- **convenções reutilizáveis**

Como o Diagrams usa Python e renderiza com **Graphviz**, essa organização funciona muito bem para versionamento e geração repetível dos arquivos finais.

---

# 2. Arquivos iniciais do projeto

## `requirements.txt`

```textile
diagrams==0.24.4  
graphviz==0.20.3
```

A biblioteca `diagrams` depende do ecossistema Graphviz para renderização do grafo.

## `pyproject.toml`

```textile
[project]  
name = "oci-daac-architecture"  
version = "0.1.0"  
description = "Diagram-as-Code for OCI architectures and Hackathon project diagrams"  
readme = "README.md"  
requires-python = ">=3.12,<3.14"  
dependencies = [  
 "diagrams==0.24.4",  
 "graphviz==0.20.3"  
]

[tool.setuptools]  
py-modules = []
```

## `.gitignore`

```textile
__pycache__/  
*.pyc 
.venv/ 
outputs/png/*  
outputs/svg/*  
!.gitkeep
```

---

# 4. Primeiro script: diagrama lógico do Hackathon

Este será o **MVP real** do projeto.

## `diagrams_src/logical/hackathon_logical.py`

```python
from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.database import PostgreSQL
from diagrams.oci.analytics import DataFlow
from diagrams.oci.storage import ObjectStorage
from diagrams.oci.governance import Compartments
from diagrams.oci.security import IAM
from diagrams.generic.compute import Rack
from diagrams.generic.storage import Storage
from diagrams.programming.framework import Spark
```

# Observação:

### Alguns nomes dos nós OCI podem variar conforme a versão instalada da biblioteca diagrams.

### Se algum import falhar, ajustamos pela lista oficial dos nós suportados na sua versão.

```textile
GRAPH_ATTR = {
 "fontsize": "20",
 "bgcolor": "white",
 "pad": "0.5",
 "splines": "ortho",
 "nodesep": "0.6",
 "ranksep": "0.9",
 "fontname": "Helvetica",
 "labelloc": "t"
}

NODE_ATTR = {
 "fontsize": "11",
 "fontname": "Helvetica"
}

EDGE_ATTR = {
 "fontsize": "10",
 "fontname": "Helvetica"
}

with Diagram(
 "Hackathon OCI - Arquitetura Logica",
 filename="outputs/png/hackathon_logical",
 outformat="png",
 show=False,
 graph_attr=GRAPH_ATTR,
 node_attr=NODE_ATTR,
 edge_attr=EDGE_ATTR,
):
 # Fontes
 with Cluster("Fontes de Dados"):
 telco_db = PostgreSQL("Base Telco / Score")
 ext_data = Storage("Arquivos externos")

# Ingestão e processamento
with Cluster("Processamento"):
    data_flow = DataFlow("OCI Data Flow")
    spark_jobs = Spark("Spark ETL Jobs")

    data_flow >> spark_jobs

# Lakehouse / Medallion
with Cluster("Object Storage Lakehouse"):
    raw = ObjectStorage("Raw")
    bronze = ObjectStorage("Bronze")
    silver = ObjectStorage("Silver")
    gold = ObjectStorage("Gold")

    raw >> bronze >> silver >> gold

# Analytics / ML
with Cluster("Analytics e Data Science"):
    ds_workspace = Rack("OCI Data Science Notebook")
    abt = Rack("ABT / Feature Base")
    model = Rack("Modelo de ML")

    gold >> ds_workspace >> abt >> model

# Governança
with Cluster("Governanca"):
    compartments = Compartments("Compartments")
    iam = IAM("IAM / Policies / Groups")

# Fluxos
telco_db >> Edge(label="ingestao") >> data_flow
ext_data >> Edge(label="carga") >> data_flow
spark_jobs >> Edge(label="grava") >> raw

compartments >> iam
iam >> Edge(style="dashed", label="controle de acesso") >> data_flow
iam >> Edge(style="dashed", label="controle de acesso") >> ds_workspace
iam >> Edge(style="dashed", label="controle de acesso") >> gold
```

---

# 5. Observação importante sobre imports OCI

Aqui existe um ponto técnico fino: o **provider OCI existe** no Diagrams, mas os nomes exatos das classes variam por módulo e versão instalada. A referência oficial de nós OCI mostra categorias como `oci.compute`, `oci.connectivity`, `oci.database`, `oci.governance`, `oci.monitoring`, `oci.network`, `oci.security` e `oci.storage`. Então, no seu ambiente, podemos fazer um pequeno ajuste fino caso algum ícone específico não esteja com o nome exato esperado.

---

# 6. Como rodar

## Instalação conceitual

O Diagrams requer:

- Python

- pacote `diagrams`

- **Graphviz instalado no sistema operacional**

Isso está explicitado na documentação oficial.

## Comandos

No Windows, eu sugiro algo assim:

```bash
python -m venv .venv  
.venv\Scripts\activate  
pip install -r requirements.txt  
python diagrams_src/logical/hackathon_logical.py
```

Saída esperada:

```
outputs/png/hackathon_logical.png
```

---

# 7. Primeira versão do diagrama que vamos gerar

Esse script representa esta visão:

```textile
Fontes de Dados  
 ├── Base Telco / Score  
 └── Arquivos externos  
 ↓  
 OCI Data Flow  
 ↓  
 Spark ETL Jobs  
 ↓  
 Object Storage Lakehouse  
 ├── Raw  
 ├── Bronze  
 ├── Silver  
 └── Gold  
 ↓  
 OCI Data Science Notebook  
 ↓  
 ABT / Feature Base  
 ↓  
 Modelo de ML

Governança transversal  
 ├── Compartments  
 └── IAM / Policies / Groups
```

Isso já conecta exatamente o que você vem construindo no Hackathon:

- ingestão

- arquitetura Medallion

- Data Flow

- Data Science

- governança OCI

E a Oracle recomenda o uso do toolkit oficial justamente para desenhar implementações OCI customizadas, o que depois pode ser usado para o refinamento visual final no Draw.io.

---

# 8. Minha recomendação prática

Para o seu fluxo ideal:

### Fonte principal

Use **DaaC em Python** para gerar a arquitetura base.

### Refino final

Use **Draw.io com toolkit OCI oficial** para:

- alinhamento visual

- slide executivo

- apresentação final

Esse fluxo é o mais robusto tecnicamente e o mais elegante para portfólio.

---

# 9. Próximo passo imediato

Agora eu sugiro fazermos nesta ordem:

## Etapa A

Eu te entrego a **versão física**: `hackathon_physical.py`

## Etapa B

Depois montamos uma **versão mais elegante do logical**, com:

- cores

- clusters melhores

- labels executivos

- separação “Data Platform / Analytics / Governance”

## Etapa C

Por fim, criamos um **template reutilizável** para seus próximos projetos OCI

No próximo passo, eu monto o `hackathon_physical.py` já no mesmo padrão.

---

---

# 1️⃣ Criar o diretório do projeto

No PowerShell:

```powershell
mkdir oci-daac-architecture  
cd oci-daac-architecture
```

---

# 2️⃣ Inicializar com uv

Agora rode:

`uv init`

Isso criará algo como:

```textile
oci-daac-architecture  
│  
├── pyproject.toml  
├── README.md  
└── src/
```

Para nosso projeto, vamos **adaptar a estrutura**.

---

# 3️⃣ Ajustar a estrutura do projeto

Crie as pastas:

```powershell
mkdir diagrams_src  
mkdir diagrams_src\logical  
mkdir diagrams_src\physical  
mkdir outputs  
mkdir outputs\png  
mkdir outputs\svg  
mkdir docs
```

Estrutura final:

```textile
oci-daac-architecture  
│  
├── pyproject.toml  
├── README.md  
│  
├── diagrams_src  
│   ├── logical  
│   │   └── hackathon_logical.py  
│   │  
│   └── physical  
│       └── hackathon_physical.py  
│  
├── outputs  
│   ├── png  
│   └── svg  
│  
└── docs
```

---

# 4️⃣ Definir versão Python

Você costuma usar **Python 3.12**, então:

```powershell
uv python pin 3.12
```

Isso cria:

```powershell
.python-version
```

---

# 5️⃣ Criar o ambiente virtual

```powershell
uv venv
```

Depois:

```powershell
.venv\Scripts\activate
```

---

# 6️⃣ Instalar dependências

Agora instalamos o que precisamos para **Diagram-as-Code**.

```powershell
uv add diagrams  
uv add graphviz
```

Isso atualizará automaticamente:

```powershell
pyproject.toml  
uv.lock
```

---

# 7️⃣ Instalar Graphviz no sistema

Aqui é importante:

A biblioteca `diagrams` usa **Graphviz instalado no sistema**.

Se ainda não tiver:

### Windows

Baixe:

```html
https://graphviz.org/download/
```

Depois confirme:

```powershell
dot -V
```

Deve aparecer algo como:

```powershell
dot - graphviz version 9.x
```

---

# 8️⃣ Teste mínimo

Crie um arquivo:

```powershell
test_diagram.py
```

Conteúdo:

```python
from diagrams import Diagram  
from diagrams.generic.compute import Rack

with Diagram("Teste", show=False):  
 Rack("OCI Resource")
```

Execute:

```powershell
python test_diagram.py
```

Se tudo estiver correto, será criado:

```powershell
teste.png
```

---

# 9️⃣ Benefício enorme de usar uv aqui

Você ganha:

✔ dependências travadas (`uv.lock`)  
✔ ambiente reproduzível  
✔ instalação rápida  
✔ compatibilidade com seu workflow atual

E isso casa perfeitamente com **Diagram-as-Code**.

---

# 🔟 Arquitetura que vamos gerar em seguida

Depois do setup, vamos criar os scripts:

### Diagrama lógico

```powershell
hackathon_logical.py
```

Representa:

```markup
Sources  
 ↓  
Data Flow  
 ↓  
Object Storage  
Raw → Bronze → Silver → Gold  
 ↓  
Data Science  
 ↓  
ML Model
```

---

### Diagrama físico

hackathon_physical.py

Representa:

```textile
OCI Region  
   │  
Compartments  
   │  
Object Storage Buckets  
   │  
Data Flow Jobs  
   │  
Data Science Notebook  
   │  
IAM / Policies / Groupsuv
```

D:\Projects\meu-projeto\
│  README.md
│  environment.yml
│  .gitignore
│
├─data\
│  ├─raw\        # dados brutos (somente leitura)
│  ├─interim\    # dados limpos parciais
│  └─processed\  # datasets finais p/ modelagem
│
├─notebooks\
│  00_setup.ipynb
│  01_data_understanding.ipynb
│  02_preprocessing.ipynb
│  03_modeling.ipynb
│  04_evaluation.ipynb
│
├─src\
│  __init__.py
│  data.py
│  features.py
│  modeling.py
│  viz.py
│
└─reports\
   └─figures\
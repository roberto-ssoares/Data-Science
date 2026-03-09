<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ resources.get("metadata", {}).get("name", "Notebook") }}</title>

    <!-- JupyterLab Light Theme -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/jupyterlab/3.6.3/themes/JupyterLab-light-theme.css">
    <!-- <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.6.0/css/bootstrap.min.css"> -->

    <!-- Highlight.js para sintaxe -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/styles/github.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/highlight.min.js"></script>
    <script>hljs.highlightAll();</script>

    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Mono:wght@300;400;600&family=Reddit+Sans:wght@300;400;600&family=Courier+Prime:wght@400;700&family=Montserrat:wght@300;400;600&family=Source+Code+Pro:wght@400&family=Red+Hat+Mono:wght@400&display=swap" rel="stylesheet">

    <!-- MathJax (necessário para renderizar LaTeX em HTML) -->
    <script>
      window.MathJax = {
        tex: {
          inlineMath: [['\\(', '\\)'], ['$', '$']],
          displayMath: [['$$', '$$'], ['\\[', '\\]']],
          processEscapes: true
        },
        options: {
          skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code'],
          ignoreHtmlClass: 'tex2jax_ignore',
          processHtmlClass: 'mathjax_process'
        }
      };
    </script>
    <script id="MathJax-script" async
      src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
    </script>

    <style>
      /* ====== GLOBAL ====== */
        body{
            font-family:'Montserrat','Reddit Sans';
            font-size:14px;
            background:#f5f5f5;
            padding:100px 0;
            color:#333;
        }
        .container{
            max-width:1550px;
            margin:auto;
            background:#fff;
            padding:20px 30px;
            border-radius:6px;
            box-shadow:0 4px 12px rgba(0,0,0,.1);
        }
        h1.title-header{
            font-family:'Montserrat','Reddit Sans';
            font-size:14px;
            font-weight:600;
            color:#8eb4c4;
            text-transform:uppercase;
            text-align:center;
            margin-bottom:24px;
        }
        /* ====== MARKDOWN ====== */
        .markdown{
            background:#f3f2ee;
            font-family:'Montserrat','Noto Sans Mono';
            font-size:14px;
            padding:10px 15px;              /* mais espaço interno */
            /* padding-left: 5px;*/
            border-left:5px solid #ff9800;  /* faixa laranja mais visível */
            border-radius:4px;
            margin:4px 0;                  /* mais respiro entre blocos */
            margin-bottom:8px;
            line-height:1.5;
            /* Centralização vertical com flexbox */
            /* display: flex; */
            align-items: center; /* ou baseline — veja qual alinha melhor */
        }
        /* No <style> do template .tpl */
        img, svg, figure img {
            max-width: 100%;      /* nunca ultrapassa o container */
            height: auto;         /* mantém proporção */
            display: block;
            margin-left: auto;
            margin-right: auto;
            border: 1px solid #ddd;                /* borda leve */
            border-radius: 6px;                    /* cantos arredondados */
            box-shadow: 0 2px 6px rgba(0,0,0,0.1); /* sombra sutil */        
        }
        /* Legendas */
        figure {
          margin: 20px auto;
          text-align: center;
        }
        figure figcaption {
          font-size: 13px;
          color: #555;
          margin-top: 6px;
        }

        /* Ajuste em telas menores */
        @media (max-width: 768px) {
          .container {
            max-width: 100%;
            padding: 15px;
          }
        }
        /* ====== CODE ====== */
        .code_cell{
            background:#f7f7f7;
            border-left:5px solid #4caf50;
            padding:4px;
            /* padding-left: 5px;*/
            margin:4px 0;
            overflow-x:auto;
            border-radius:4px;
            display: flex;
            align-items: center; /* ou baseline — veja qual alinha melhor */            
        }
        .code_cell pre,
        .code_cell .hljs{
            background:transparent!important;
            font-family:'Red Hat Mono','Reddit Sans';
            font-size:14px;
            line-height:1.5;
        }
        /* ====== OUTPUT ====== */
        .output{
            background:#f3f9fa;
            border-left:5px solid #2196f3;
            padding:10px 6px;              /* mais espaço interno */
            padding-left: 8px;            
            margin:4px 0;                  /* mais respiro entre blocos */
            margin-bottom:0px;
            font-family:'Red Hat Mono','Noto Sans Mono';
            font-size:14px;
            text-align:left;
            line-height:1.5;
            white-space:pre-wrap;        
            overflow-x:auto;
            border-radius:4px;
            align-items: center; /* ou baseline — veja qual alinha melhor */            
        }
        .output img{
            max-width:100%;
            height:auto;
            display:block;
            margin:auto;
        }
        /* Caixa específica para stream outputs (ex: print, watermark, logs) */
        .output-stream {
            background:#f3f9fa;
            border-left:5px solid #2196f3;
            padding: 6px 10px;
            margin:4px 0;
        }
        /* ====== FOOTER ====== */
        .footer{
            text-align:right;
            margin-top:30px;
            padding:12px;
            background:#e9ecef;
            border-radius:4px;
            font-size:14px;
            color:#555;
        }        

        /* Tabelas */
        table.dataframe {
            border-collapse: collapse;
            border: none;
            margin: 0;
            padding: 0;
            font-family:'Red Hat Mono','Noto Sans Mono';
            font-size: 14px;
            line-height: 1.4;
            width: auto;
        }
        table.dataframe th, table.dataframe td {
            padding: 8px;
            border: 1px solid #ddd;
        }
        table.dataframe thead {
            background-color: #f9f9f9;
            font-weight: bold;
        }
        table.dataframe tr:nth-child(even) {
            background-color: #f6f8fa;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="title-header">{{ resources.get("metadata", {}).get("name", "Notebook") }}</h1>

        {# ====== LOOP PRINCIPAL SOBRE AS CÉLULAS ====== #}
        {% for cell in nb.cells %}
            <div class="cell">
            {% if cell.cell_type == 'markdown' %}
                <div class="markdown" role="region" aria-label="Markdown Cell">
                    {{ cell.source | markdown2html }}
                </div>

            {% elif cell.cell_type == 'code' %}
                <div class="code_cell" role="region" aria-label="Code Cell">
                    <pre><code class="language-python">{{ cell.source | escape }}</code></pre>
                </div>

                {# --- LOOP DE OUTPUTS DA CÉLULA DE CÓDIGO --- #}
                {% for output in cell.outputs %}
                    {# Imagem primeiro #}
                    {% if 'image/png' in output.data %}
                        <div class="output text-center">
                            <img src="data:image/png;base64,{{ output.data['image/png'] }}" alt="Graph" class="img-fluid mx-auto d-block">
                        </div>

                    {# HTML (tabelas do Styler, gráficos interativos etc.) antes de text/plain #}
                    {% elif 'text/html' in output.data %}
                        <div class="output table-output">
                            {{ output.data['text/html'] | safe }}
                        </div>

                    {# Texto simples por último #}
                    {% elif 'text/plain' in output.data %}
                        <div class="output">
                            <pre>{{ output.data['text/plain'] }}</pre>
                        </div>

                    {# >>> tratamento de stream e stderr <<< #}
                    {% elif output.output_type == 'stream' %}
                        {# stdout/stderr de prints, !pip, magics etc. #}
                        <div class="output output-stream {% if output.name == 'stderr' %}text-danger{% endif %}">
                            <pre>{{ output.text }}</pre>
                        </div>

                    {# >>> FIM DO TRECHO NOVO <<< #}                        
                    {% elif 'application/javascript' in output.data %}
                        <div class="output">
                            {{ output.data['application/javascript'] | safe }}
                        </div>
                    {% elif 'application/vnd.jupyter.widget-view+json' in output.data %}
                        <div class="output">
                            <pre>{{ output.data['application/vnd.jupyter.widget-view+json'] | tojson(indent=2) }}</pre>
                        </div>

                    {# Erros #}
                    {% elif output.output_type == 'error' %}
                        <div class="output text-danger">
                            <strong>{{ output.ename }}:</strong> {{ output.evalue }}
                            <pre>{{ output.traceback | join("\n") }}</pre>
                        </div>
                    {% endif %}
                {% endfor %}
            {% endif %}
            </div>
        {% endfor %}

        <div class="footer">
            <p>RobertoSSoares-LfLngLrnng — <span id="datetime"></span></p>
        </div>
        <script>
            document.getElementById("datetime").innerText = new Date().toLocaleString('pt-BR');
        </script>
    </div>
</body>
</html>

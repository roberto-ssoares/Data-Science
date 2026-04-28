<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ resources.get("metadata", {}).get("name", "Notebook") }}</title>

    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/jupyterlab/3.6.3/themes/JupyterLab-light-theme.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/styles/github.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/highlight.min.js"></script>
    <script>hljs.highlightAll();</script>

    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Mono:wght@300;400;600&family=Reddit+Sans:wght@300;400;600&family=Courier+Prime:wght@400;700&family=Montserrat:wght@300;400;600;700&family=Source+Code+Pro:wght@400&family=Red+Hat+Mono:wght@400;600&display=swap" rel="stylesheet">

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
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

    <style>
        :root{
            --bg:#f5f5f5;
            --paper:#ffffff;
            --text:#1f2937;
            --muted:#6b7280;
            --border:#d9dde3;
            --shadow:0 4px 12px rgba(0,0,0,.08);
            --shadow-soft:0 2px 8px rgba(15,23,42,.06);
            --md-bg:#f3f2ee;
            --md-accent:#ff9800;
            --code-bg:#f7f7f7;
            --code-accent:#4caf50;
            --out-bg:#f3f9fa;
            --out-accent:#2196f3;
            --stream-bg:#eef8ff;
            --table-head:#f8fafc;
            --table-zebra:#f6f8fa;
            --exec-bg:#f7fbff;
            --exec-border:#2E86C1;
            --insight-bg:#f8fffb;
            --insight-border:#22a06b;
            --warning-bg:#fffaf2;
            --warning-border:#f59e0b;
            --danger-bg:#fff6f6;
            --danger-border:#ef4444;
            --metric-bg:#ffffff;
            --metric-border:#d6e7f7;
        }

        *{ box-sizing:border-box; }

        body{
            font-family:'Montserrat','Reddit Sans',sans-serif;
            font-size:14px;
            background:var(--bg);
            padding:40px 0;
            color:var(--text);
            line-height:1.55;
        }

        .container{
            max-width:1550px;
            margin:auto;
            background:var(--paper);
            padding:20px 30px 28px;
            border-radius:8px;
            box-shadow:var(--shadow);
        }

        .cell{ margin-bottom:10px; }

        h1.title-header{
            font-family:'Montserrat','Reddit Sans',sans-serif;
            font-size:14px;
            font-weight:700;
            color:#8eb4c4;
            text-transform:uppercase;
            text-align:center;
            margin:0 0 24px;
            letter-spacing:.04em;
        }

        .markdown{
            background:var(--md-bg);
            font-family:'Montserrat','Reddit Sans',sans-serif;
            font-size:14px;
            padding:10px 15px;
            border-left:5px solid var(--md-accent);
            border-radius:4px;
            margin:4px 0 8px;
            line-height:1.6;
        }
        .markdown h1,.markdown h2,.markdown h3,.markdown h4,.markdown h5,.markdown h6{
            margin-top:0;
            color:#d64545;
        }
        .markdown p:last-child,
        .markdown ul:last-child,
        .markdown ol:last-child{ margin-bottom:0; }

        img, svg, figure img{
            max-width:100%;
            height:auto;
            display:block;
            margin-left:auto;
            margin-right:auto;
            border:1px solid #ddd;
            border-radius:6px;
            box-shadow:0 2px 6px rgba(0,0,0,0.08);
        }

        figure{ margin:20px auto; text-align:center; }
        figure figcaption{ font-size:13px; color:#555; margin-top:6px; }

        .cell-toolbar{
            display:flex;
            justify-content:flex-end;
            margin:0 0 4px;
            gap:6px;
            flex-wrap:wrap;
        }
        .cell-badge{
            display:inline-block;
            background:#eef2f7;
            border:1px solid #d7dee8;
            color:#516072;
            border-radius:999px;
            font-size:11px;
            font-weight:600;
            padding:2px 8px;
            letter-spacing:.02em;
        }

        .code_cell{
            background:var(--code-bg);
            border-left:5px solid var(--code-accent);
            padding:6px 8px;
            margin:4px 0;
            overflow-x:auto;
            border-radius:4px;
        }
        .code_cell pre,
        .code_cell .hljs{
            margin:0;
            background:transparent !important;
            font-family:'Red Hat Mono','Noto Sans Mono',monospace;
            font-size:13px;
            line-height:1.55;
            white-space:pre;
        }

        .output-text,
        .output-stream,
        .output-error,
        .output-image,
        .output-html{
            margin:4px 0;
            border-radius:4px;
            overflow-x:auto;
        }

        .output-text{
            background:var(--out-bg);
            border-left:5px solid var(--out-accent);
            padding:10px 10px 10px 8px;
            font-family:'Red Hat Mono','Noto Sans Mono',monospace;
            font-size:13px;
            line-height:1.55;
        }
        .output-text pre{
            margin:0;
            white-space:pre-wrap;
            word-break:break-word;
            font-family:inherit;
            font-size:inherit;
            line-height:inherit;
        }

        .output-stream{
            background:var(--stream-bg);
            border-left:5px solid var(--out-accent);
            padding:8px 10px;
            font-family:'Red Hat Mono','Noto Sans Mono',monospace;
            font-size:13px;
            line-height:1.55;
        }
        .output-stream pre{ margin:0; white-space:pre-wrap; word-break:break-word; }

        .output-image{
            background:var(--out-bg);
            border-left:5px solid var(--out-accent);
            padding:10px;
        }

        .output-html{
            background:var(--out-bg);
            border-left:5px solid var(--out-accent);
            padding:8px 10px;
            color:var(--text);
            font-family:'Montserrat','Reddit Sans',sans-serif;
            font-size:14px;
            line-height:1.55;
            white-space:normal;
        }
        .output-html *{ white-space:normal; word-break:normal; max-width:100%; }
        .output-html p{ margin:0 0 10px; }
        .output-html p:last-child{ margin-bottom:0; }
        .output-html h1,.output-html h2,.output-html h3,.output-html h4,.output-html h5,.output-html h6{
            margin:0 0 10px;
            color:var(--text);
            line-height:1.3;
        }
        .output-html ul,
        .output-html ol{ margin:0 0 10px 20px; padding-left:12px; }
        .output-html li{ margin-bottom:4px; }
        .output-html li:last-child{ margin-bottom:0; }
        .output-html code{ font-family:'Red Hat Mono','Noto Sans Mono',monospace; font-size:.95em; }
        .output-html pre{
            white-space:pre-wrap;
            word-break:break-word;
            font-family:'Red Hat Mono','Noto Sans Mono',monospace;
            font-size:13px;
            line-height:1.5;
            margin:0;
        }

        .table-output{ padding:8px 10px; }
        .table-output table,
        .table-output table.dataframe{
            border-collapse:collapse;
            border-spacing:0;
            width:auto;
            max-width:100%;
            margin:0;
            font-family:'Red Hat Mono','Noto Sans Mono',monospace;
            font-size:13px;
            line-height:1.45;
            color:#263238;
            background:#fff;
        }
        .table-output table th,
        .table-output table td,
        .table-output table.dataframe th,
        .table-output table.dataframe td{
            padding:8px 10px;
            border:1px solid var(--border);
            vertical-align:top;
            text-align:left;
        }
        .table-output table thead,
        .table-output table.dataframe thead{ background:var(--table-head); font-weight:600; }
        .table-output table tbody tr:nth-child(even),
        .table-output table.dataframe tbody tr:nth-child(even){ background:var(--table-zebra); }
        .table-output .dataframe tbody tr:hover,
        .table-output table tbody tr:hover{ background:#eef6ff; }

        /* Premium HTML blocks */
        .output-html .executive-card,
        .output-html .insight-card,
        .output-html .warning-card,
        .output-html .danger-card,
        .output-html .summary-card{
            border-radius:10px;
            padding:14px 16px;
            box-shadow:var(--shadow-soft);
            border:1px solid #dbe5ef;
            margin:4px 0;
        }
        .output-html .executive-card{
            background:var(--exec-bg);
            border-left:6px solid var(--exec-border);
        }
        .output-html .summary-card{
            background:#f8fbff;
            border-left:6px solid #64748b;
        }
        .output-html .insight-card{
            background:var(--insight-bg);
            border-left:6px solid var(--insight-border);
        }
        .output-html .warning-card{
            background:var(--warning-bg);
            border-left:6px solid var(--warning-border);
        }
        .output-html .danger-card{
            background:var(--danger-bg);
            border-left:6px solid var(--danger-border);
        }
        .output-html .card-title{
            margin:0 0 10px;
            font-size:20px;
            font-weight:700;
            color:#1f2937;
            line-height:1.25;
        }
        .output-html .card-subtitle{
            margin:0 0 12px;
            font-size:13px;
            font-weight:600;
            color:#64748b;
            text-transform:uppercase;
            letter-spacing:.03em;
        }
        .output-html .card-grid{
            display:grid;
            grid-template-columns:repeat(auto-fit, minmax(180px, 1fr));
            gap:10px;
            margin:10px 0 12px;
        }
        .output-html .metric-card{
            background:var(--metric-bg);
            border:1px solid var(--metric-border);
            border-radius:10px;
            padding:10px 12px;
            min-height:82px;
            box-shadow:0 1px 3px rgba(15,23,42,.05);
        }
        .output-html .metric-label{
            display:block;
            margin:0 0 6px;
            font-size:12px;
            font-weight:700;
            color:#64748b;
            text-transform:uppercase;
            letter-spacing:.03em;
        }
        .output-html .metric-value{
            display:block;
            font-size:24px;
            font-weight:700;
            line-height:1.15;
            color:#0f172a;
        }
        .output-html .metric-note{
            display:block;
            margin-top:4px;
            font-size:12px;
            color:#6b7280;
        }
        .output-html .chip-row{
            display:flex;
            flex-wrap:wrap;
            gap:8px;
            margin:8px 0 10px;
        }
        .output-html .chip{
            display:inline-flex;
            align-items:center;
            background:#edf4ff;
            border:1px solid #d8e6ff;
            color:#2457a6;
            border-radius:999px;
            padding:4px 10px;
            font-size:12px;
            font-weight:600;
        }
        .output-html .callout-compact p{ margin-bottom:8px; }
        .output-html .callout-compact ul,
        .output-html .callout-compact ol{ margin-bottom:8px; }

        .output-error{
            background:#fff5f5;
            border-left:5px solid #ef4444;
            padding:10px 12px;
            color:#7f1d1d;
            font-family:'Red Hat Mono','Noto Sans Mono',monospace;
            font-size:13px;
            line-height:1.5;
        }
        .output-error pre{ margin:8px 0 0; white-space:pre-wrap; word-break:break-word; }

        .hidden-note{
            margin:4px 0;
            padding:6px 10px;
            border-radius:6px;
            background:#f8fafc;
            border:1px dashed #cbd5e1;
            color:#64748b;
            font-size:12px;
            font-weight:600;
        }

        .footer{
            text-align:right;
            margin-top:30px;
            padding:12px;
            background:#e9ecef;
            border-radius:4px;
            font-size:14px;
            color:#555;
        }

        @media (max-width: 768px) {
            body{ padding:16px 0; }
            .container{ max-width:100%; padding:14px 16px 20px; border-radius:0; }
            .output-html,
            .output-text,
            .output-stream,
            .output-image,
            .output-error,
            .markdown,
            .code_cell{ padding-left:10px; padding-right:10px; }
            .output-html .card-title{ font-size:18px; }
            .output-html .metric-value{ font-size:20px; }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="title-header">{{ resources.get("metadata", {}).get("name", "Notebook") }}</h1>

        {% for cell in nb.cells %}
            {% set tags = cell.metadata.get('tags', []) %}
            {% set hide_input = 'hide-input' in tags or 'remove-input' in tags or 'hide_code' in tags %}
            {% set hide_output = 'hide-output' in tags or 'remove-output' in tags %}
            {% set hide_cell = 'hide-cell' in tags or 'remove-cell' in tags %}

            {% if not hide_cell %}
            <div class="cell">
            {% if cell.cell_type == 'markdown' %}
                <div class="markdown" role="region" aria-label="Markdown Cell">
                    {{ cell.source | markdown2html }}
                </div>

            {% elif cell.cell_type == 'code' %}
                {% if tags %}
                <div class="cell-toolbar">
                    {% for tag in tags %}
                        <span class="cell-badge">{{ tag }}</span>
                    {% endfor %}
                </div>
                {% endif %}

                {% if not hide_input %}
                <div class="code_cell" role="region" aria-label="Code Cell">
                    <pre><code class="language-python">{{ cell.source | escape }}</code></pre>
                </div>
                {% else %}
                <div class="hidden-note">Código oculto na exportação HTML.</div>
                {% endif %}

                {% if not hide_output %}
                {% for output in cell.outputs %}
                    {% if 'image/png' in output.data %}
                        <div class="output-image text-center">
                            <img src="data:image/png;base64,{{ output.data['image/png'] }}" alt="Graph" class="img-fluid mx-auto d-block">
                        </div>

                    {% elif 'text/html' in output.data %}
                        <div class="output-html table-output">
                            {{ output.data['text/html'] | safe }}
                        </div>

                    {% elif 'text/plain' in output.data %}
                        <div class="output-text">
                            <pre>{{ output.data['text/plain'] }}</pre>
                        </div>

                    {% elif output.output_type == 'stream' %}
                        <div class="output-stream {% if output.name == 'stderr' %}text-danger{% endif %}">
                            <pre>{{ output.text }}</pre>
                        </div>

                    {% elif 'application/javascript' in output.data %}
                        <div class="output-html">
                            {{ output.data['application/javascript'] | safe }}
                        </div>
                    {% elif 'application/vnd.jupyter.widget-view+json' in output.data %}
                        <div class="output-text">
                            <pre>{{ output.data['application/vnd.jupyter.widget-view+json'] | tojson(indent=2) }}</pre>
                        </div>

                    {% elif output.output_type == 'error' %}
                        <div class="output-error">
                            <strong>{{ output.ename }}:</strong> {{ output.evalue }}
                            <pre>{{ output.traceback | join("\n") }}</pre>
                        </div>
                    {% endif %}
                {% endfor %}
                {% else %}
                <div class="hidden-note">Saída oculta na exportação HTML.</div>
                {% endif %}
            {% endif %}
            </div>
            {% endif %}
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

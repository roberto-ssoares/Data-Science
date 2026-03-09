from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.database import PostgreSQL
from diagrams.generic.storage import Storage
from diagrams.generic.compute import Rack
from diagrams.generic.blank import Blank

GRAPH_ATTR = {
    "fontsize": "22",
    "pad": "0.6",
    "nodesep": "0.7",
    "ranksep": "1.1",
    "splines": "ortho",
    "labelloc": "t",
    "fontname": "Helvetica",
}

NODE_ATTR = {
    "fontsize": "11",
    "fontname": "Helvetica",
}

EDGE_ATTR = {
    "fontsize": "10",
    "fontname": "Helvetica",
}


with Diagram(
    "Hackathon OCI - Functional Architecture",
    filename="outputs/png/hackathon_functional",
    outformat="png",
    show=False,
    direction="LR",
    graph_attr=GRAPH_ATTR,
    node_attr=NODE_ATTR,
    edge_attr=EDGE_ATTR,
):
    with Cluster("Data Sources"):
        internal_data = PostgreSQL("Dados Internos\nTelco / CRM / Billing")
        external_data = Storage("Scores /\nFontes Externas")

    with Cluster("Connect, Ingest, Transform"):
        dataflow = Rack("OCI Data Flow\nSpark Serverless ETL")
        ingest_stub = Blank("")

    with Cluster("Persist, Curate, Create"):
        object_storage = Storage("Object Storage\nLakehouse")
        raw = Storage("Raw")
        bronze = Storage("Bronze")
        silver = Storage("Silver")
        gold = Storage("Gold")

    with Cluster("Analyze, Learn, Predict"):
        ds_notebook = Rack("OCI Data Science\nNotebook")
        abt = Rack("ABT /\nFeature Engineering")
        model = Rack("Model Training /\nEvaluation")

    with Cluster("Consume / Act"):
        score = Rack("Score /\nPredição")
        insights = Rack("Insights /\nDecision Support")

    with Cluster("Governance / Security"):
        governance = Rack("IAM • Policies •\nUser Groups • Compartments")

    # Fluxo principal
    internal_data >> Edge(label="batch / ingestão") >> dataflow
    external_data >> Edge(label="carga") >> dataflow

    dataflow >> Edge(label="write") >> object_storage
    object_storage >> raw >> bronze >> silver >> gold

    gold >> Edge(label="read") >> ds_notebook
    ds_notebook >> abt >> model
    model >> score
    gold >> Edge(label="analytics") >> insights

    # Governança transversal
    governance >> Edge(style="dashed", label="acesso") >> dataflow
    governance >> Edge(style="dashed", label="acesso") >> gold
    governance >> Edge(style="dashed", label="acesso") >> ds_notebook
from diagrams import Diagram, Cluster, Edge

from diagrams.onprem.database import PostgreSQL
from diagrams.generic.storage import Storage

from diagrams.oci.database import DataflowApache, Science
from diagrams.oci.storage import ObjectStorage, Buckets
from diagrams.oci.governance import Compartments, Groups, Policies
from diagrams.oci.security import IDAccess

GRAPH_ATTR = {
    "fontsize": "20",
    "pad": "0.5",
    "splines": "ortho",
    "nodesep": "0.7",
    "ranksep": "1.0",
    "labelloc": "t",
}

NODE_ATTR = {
    "fontsize": "11",
}

EDGE_ATTR = {
    "fontsize": "10",
}

with Diagram(
    "Hackathon OCI - Arquitetura Logica (OCI Nodes)",
    filename="outputs/png/hackathon_logical_oci",
    outformat="png",
    show=False,
    graph_attr=GRAPH_ATTR,
    node_attr=NODE_ATTR,
    edge_attr=EDGE_ATTR,
):
    # Fontes
    with Cluster("Fontes de Dados"):
        telco_db = PostgreSQL("Dados Internos / Telco")
        ext_data = Storage("Scores / Arquivos Externos")

    # Processamento em OCI
    with Cluster("Processamento em OCI"):
        data_flow = DataflowApache("OCI Data Flow\n(Spark Serverless)")

    # Lakehouse / Medallion
    with Cluster("Object Storage Lakehouse"):
        obj_storage = ObjectStorage("Object Storage")

        raw_bucket = Buckets("raw")
        bronze_bucket = Buckets("bronze")
        silver_bucket = Buckets("silver")
        gold_bucket = Buckets("gold")

        obj_storage >> raw_bucket >> bronze_bucket >> silver_bucket >> gold_bucket

    # Analytics / ML
    with Cluster("Analytics e ML"):
        data_science = Science("OCI Data Science")
        abt = Buckets("ABT / Feature Base")
        model_output = Buckets("Model Artifact")

        gold_bucket >> Edge(label="read") >> data_science
        data_science >> abt >> model_output

    # Governança
    with Cluster("Governanca OCI"):
        compartments = Compartments("Compartments")
        groups = Groups("User Groups")
        policies = Policies("Policies")
        iam = IDAccess("IAM / Identity Access")

        compartments >> groups >> policies >> iam

    # Fluxos principais
    telco_db >> Edge(label="ingestao") >> data_flow
    ext_data >> Edge(label="carga") >> data_flow
    data_flow >> Edge(label="write") >> raw_bucket

    # Governança transversal
    iam >> Edge(style="dashed", label="acesso") >> data_flow
    iam >> Edge(style="dashed", label="acesso") >> data_science
    iam >> Edge(style="dashed", label="acesso") >> gold_bucket
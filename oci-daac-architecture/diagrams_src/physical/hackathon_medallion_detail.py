from diagrams import Diagram, Cluster, Edge
from diagrams.oci.storage import ObjectStorage, Buckets
from diagrams.oci.database import DataflowApache
from diagrams.oci.database import Science

GRAPH_ATTR = {
    "fontsize": "22",
    "pad": "0.6",
    "nodesep": "0.9",
    "ranksep": "1.0",
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
    "Hackathon OCI - Medallion Detail",
    filename="outputs/png/hackathon_medallion_detail",
    outformat="png",
    show=False,
    direction="LR",
    graph_attr=GRAPH_ATTR,
    node_attr=NODE_ATTR,
    edge_attr=EDGE_ATTR,
):
    data_flow = DataflowApache("OCI Data Flow\nIngestion / ETL")

    with Cluster("Object Storage Lakehouse"):
        object_storage = ObjectStorage("Object Storage")

        raw = Buckets("Raw\nDados brutos")
        bronze = Buckets("Bronze\nPadronização inicial")
        silver = Buckets("Silver\nQualidade / Curadoria")
        gold = Buckets("Gold\nDados analíticos")

        object_storage >> raw >> bronze >> silver >> gold

    data_science = Science("OCI Data Science\nConsumo analítico")

    data_flow >> Edge(label="write") >> raw
    bronze >> Edge(label="tratamento") >> silver
    silver >> Edge(label="agregação / negócio") >> gold
    gold >> Edge(label="read") >> data_science
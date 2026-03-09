from diagrams import Diagram, Cluster, Edge
from diagrams.oci.database import DataflowApache, Science
from diagrams.oci.storage import ObjectStorage, Buckets
from diagrams.oci.governance import Compartments, Groups, Policies
from diagrams.oci.security import IDAccess

GRAPH_ATTR = {
    "fontsize": "22",
    "pad": "0.6",
    "nodesep": "0.8",
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
    "Hackathon OCI - Physical Architecture",
    filename="outputs/png/hackathon_physical",
    outformat="png",
    show=False,
    direction="LR",
    graph_attr=GRAPH_ATTR,
    node_attr=NODE_ATTR,
    edge_attr=EDGE_ATTR,
):
    with Cluster("OCI Region: sa-saopaulo-1"):
        with Cluster("Compartment: cmp-hackathon-data"):
            object_storage = ObjectStorage("Object Storage")

            bucket_raw = Buckets("bucket-raw")
            bucket_bronze = Buckets("bucket-bronze")
            bucket_silver = Buckets("bucket-silver")
            bucket_gold = Buckets("bucket-gold")

            data_flow = DataflowApache("OCI Data Flow")

        with Cluster("Compartment: cmp-hackathon-ml"):
            data_science = Science("OCI Data Science")
            feature_store = Buckets("abt-features")
            model_artifact = Buckets("model-artifacts")

        with Cluster("IAM Governance"):
            compartments = Compartments("Compartments")
            groups = Groups("User Groups")
            policies = Policies("Policies")
            iam = IDAccess("IAM")

    # Storage hierarchy
    object_storage >> bucket_raw >> bucket_bronze >> bucket_silver >> bucket_gold

    # Processing and analytics
    data_flow >> Edge(label="write") >> bucket_raw
    bucket_gold >> Edge(label="read") >> data_science
    data_science >> feature_store
    data_science >> model_artifact

    # Governance
    compartments >> groups >> policies >> iam
    iam >> Edge(style="dashed", label="access") >> data_flow
    iam >> Edge(style="dashed", label="access") >> bucket_gold
    iam >> Edge(style="dashed", label="access") >> data_science
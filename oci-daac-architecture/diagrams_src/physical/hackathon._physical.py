from diagrams import Diagram, Cluster, Edge
from diagrams.generic.storage import Storage
from diagrams.generic.compute import Rack

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
    "Hackathon OCI - Arquitetura Fisica",
    filename="outputs/png/hackathon_physical",
    outformat="png",
    show=False,
    graph_attr=GRAPH_ATTR,
    node_attr=NODE_ATTR,
    edge_attr=EDGE_ATTR,
):
    with Cluster("OCI Region: sa-saopaulo-1"):
        with Cluster("Compartment: hackathon-data"):
            with Cluster("Object Storage"):
                bucket_raw = Storage("bucket-raw")
                bucket_bronze = Storage("bucket-bronze")
                bucket_silver = Storage("bucket-silver")
                bucket_gold = Storage("bucket-gold")

            data_flow = Rack("OCI Data Flow")
            spark_jobs = Rack("Spark Serverless Jobs")

            data_flow >> spark_jobs
            spark_jobs >> Edge(label="write") >> bucket_raw
            bucket_raw >> bucket_bronze >> bucket_silver >> bucket_gold

        with Cluster("Compartment: hackathon-ml"):
            ds_notebook = Rack("OCI Data Science Notebook")
            abt_store = Rack("ABT / Feature Base")
            model_artifact = Rack("Model Artifact")

            bucket_gold >> Edge(label="read") >> ds_notebook
            ds_notebook >> abt_store >> model_artifact

        with Cluster("IAM Governance"):
            user_groups = Rack("User Groups")
            policies = Rack("Policies")
            access = Rack("IAM Access Control")

            user_groups >> policies >> access

        access >> Edge(style="dashed", label="access") >> data_flow
        access >> Edge(style="dashed", label="access") >> ds_notebook
        access >> Edge(style="dashed", label="access") >> bucket_gold
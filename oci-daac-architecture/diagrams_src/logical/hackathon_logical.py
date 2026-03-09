
#%% 

from diagrams import Diagram, Cluster, Edge
from diagrams.oci.connectivity import CustomerPremises

from diagrams.generic.storage import Storage
from diagrams.generic.compute import Rack


GRAPH_ATTR = {
    "fontsize": "20",
    "pad": "0.5",
    "splines": "ortho",
    "nodesep": "0.6",
    "ranksep": "0.9",
    "labelloc": "t",
}

with Diagram(
    "Hackathon OCI - Arquitetura Logica",
    filename="outputs/png/hackathon_logical",
    outformat="png",
    show=False,
    graph_attr=GRAPH_ATTR,
):
    with Cluster("Fontes de Dados"):
        telco_db = CustomerPremises("Base Telco")
        ext_data = Storage("Arquivos Externos")

    with Cluster("Processamento"):
        data_flow = Rack("OCI Data Flow")
        spark_jobs = Rack("Spark ETL Jobs")

    with Cluster("Lakehouse Medallion"):
        raw = Storage("Raw")
        bronze = Storage("Bronze")
        silver = Storage("Silver")
        gold = Storage("Gold")

    with Cluster("Analytics e ML"):
        ds = Rack("OCI Data Science")
        abt = Rack("ABT")
        model = Rack("Modelo ML")

    with Cluster("Governanca"):
        iam = Rack("IAM / Policies / Groups")
        compartments = Rack("Compartments")

    telco_db >> Edge(label="ingestao") >> data_flow
    ext_data >> Edge(label="carga") >> data_flow
    data_flow >> spark_jobs >> raw
    raw >> bronze >> silver >> gold
    gold >> ds >> abt >> model

    compartments >> iam
    iam >> Edge(style="dashed", label="acesso") >> data_flow
    iam >> Edge(style="dashed", label="acesso") >> ds
    iam >> Edge(style="dashed", label="acesso") >> gold
# %%

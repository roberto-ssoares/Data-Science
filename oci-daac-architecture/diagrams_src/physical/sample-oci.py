from diagrams import Diagram, Cluster, Edge
from diagrams.oci.compute import VM
from diagrams.oci.database import DatabaseService
from diagrams.oci.network import LoadBalancer
from diagrams.oci.connectivity import CustomerDatacenter
from diagrams.oci.connectivity import FastConnect
from diagrams.oci.network import Vcn
from diagrams.aws.storage import  S3Glacier

with Diagram("Sample-OCI", show=False):
    #graphdir = "LR";
    source = CustomerDatacenter("My DC")
    FC = FastConnect("FC-1Gbps")
    source >> FC

    with Cluster("VCN"):
        VCN = Vcn("OCI VCN", width="0.50")
        FC >> VCN
        with Cluster("DMZ Subnet"):
            LB = LoadBalancer("Public LBaaS")
        with Cluster("App Subnet"):
            WEB = VM("App1")
            WEB - Edge(color="red", style="dashed") - VM("App2")
            LB >> WEB
        with Cluster("DB Subnet"):
            DB = DatabaseService("DB")
            WEB >> DB
    BKP = S3Glacier("S3-Backup-Bucket")
    DB >> BKP
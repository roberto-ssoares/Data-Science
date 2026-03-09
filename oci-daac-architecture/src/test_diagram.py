from diagrams import Diagram
from diagrams.generic.compute import Rack

with Diagram("teste_diagram", show=False):
    Rack("node")
from diagrams import Cluster, Diagram, Edge
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS

with Diagram("AWS Architecture", show=False):
    with Cluster("DMZ"):
        app_server = EC2("App Server")
        lb = EC2("Load Balancer")

    with Cluster("DB"):
        db = RDS("Database")

    lb >> app_server
    app_server >> db
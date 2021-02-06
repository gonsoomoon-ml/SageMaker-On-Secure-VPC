from aws_cdk import (
    aws_ec2 as ec2,
    core,
)

class VpcPeeringConnection(ec2.CfnVPCPeeringConnection):
    def __init__(self,scope, id, **kwargs):
        super().__init__(scope, id, **kwargs)

class VpcPeering(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        vpc_id = core.CfnParameter(self, "vpcId", type="String",
            description="The ID of the VPC peering requester")

        peer_vpc_id = core.CfnParameter(self, "peerVpcId", type="String",
            description="The ID of the VPC peering accepter")

        peer_region = core.CfnParameter(self, "peerVpcRegion", type="String",
            description="The region of the VPC peering accepter")

        vpc_peer = VpcPeeringConnection(
            self, "vpc_peering_connection",
            vpc_id=vpc_id.value_as_string,
            peer_vpc_id=peer_vpc_id.value_as_string,
            peer_region=peer_region.value_as_string
        )
        vpc_peer_ref=vpc_peer.ref

        # cloudformation outputs
        core.CfnOutput(
            self, "VPCPEERINGID",
            description = "VPC PEERING ID",
            value = vpc_peer.ref
        )

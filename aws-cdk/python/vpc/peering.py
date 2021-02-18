from aws_cdk import (
    aws_ec2 as ec2,
    core,
)

class VpcPeeringConnection(ec2.CfnVPCPeeringConnection):
    def __init__(self, scope, id, **kwargs):
        super().__init__(scope, id, **kwargs)

class VpcPeering(core.Stack):
    def __init__(self, scope: core.Construct, id: str, props, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # vpc peering
        peering = VpcPeeringConnection(
            self, "vpc_peering_connection",
            vpc_id=props['vpc'].vpc_id,
            peer_vpc_id=props['peer_vpc'].vpc_id,
        )
        self.vpc_peer_ref=peering.ref

        self.output_props=props.copy()
        self.output_props['vpc_peer_ref']=peering.ref

        # peering route table
        ec2.CfnRoute(self, "route_to_peer_vpc",
            route_table_id=props['vpc'].isolated_subnets[0].route_table.route_table_id,
            destination_cidr_block=props['peer_vpc'].vpc_cidr_block,
            vpc_peering_connection_id=peering.ref
        )

        ec2.CfnRoute(self, "route_to_vpc",
            route_table_id=props['peer_vpc'].isolated_subnets[0].route_table.route_table_id,
            destination_cidr_block=props['vpc'].vpc_cidr_block,
            vpc_peering_connection_id=peering.ref
        )

    # pass objects to another stack
    @property
    def outputs(self):
        return self.output_props

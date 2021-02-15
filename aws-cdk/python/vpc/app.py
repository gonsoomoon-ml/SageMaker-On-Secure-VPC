import os

from aws_cdk import (
    core,
)
from vpc import Vpc
from peering import VpcPeering

props = {'namespace': 'default'}

env = core.Environment(account=os.environ['CDK_DEFAULT_ACCOUNT'],region="ap-northeast-2")

app = core.App()

# VPCs
vpc_aws = Vpc(app, f"{props['namespace']}-aws", props, cidr="10.11.0.0/16", env=env)
vpc_corp = Vpc(app, f"{props['namespace']}-corp", props, cidr="10.10.0.0/16", env=env)

props['vpc']=vpc_aws.outputs['vpc']
props['peer_vpc']=vpc_corp.outputs['vpc']

peering = VpcPeering(app, f"{props['namespace']}-peering", props, env=env)

app.synth()

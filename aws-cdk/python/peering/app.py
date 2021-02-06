import os

from aws_cdk import (
    core,
)
from peering import VpcPeering

props = {'namespace': 'default'}

env_kr = core.Environment(account=os.environ['CDK_DEFAULT_ACCOUNT'], region="ap-northeast-2")

app = core.App()

# VPCs
peering = VpcPeering(app, f"{props['namespace']}-peering", env=env_kr)

app.synth()

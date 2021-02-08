import os

from aws_cdk import (
    core,
)
from vpc import Vpc

props = {'namespace': 'default'}

env_kr = core.Environment(account=os.environ['CDK_DEFAULT_ACCOUNT'],region="ap-northeast-2")
env_us = core.Environment(account=os.environ['CDK_DEFAULT_ACCOUNT'],region="us-west-2")

app = core.App()

# VPCs
vpc_aws = Vpc(app, f"{props['namespace']}-aws", props, cidr="10.11.0.0/16", env=env_us)
vpc_corp = Vpc(app, f"{props['namespace']}-corp", props, cidr="10.10.0.0/16", env=env_kr)

app.synth()

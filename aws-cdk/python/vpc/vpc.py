from aws_cdk import (
    aws_ec2 as ec2,
    core,
)

class Vpc(core.Stack):
    def __init__(self, app: core.App, id: str, props, cidr: str, **kwargs) -> None:
        super().__init__(app, id, **kwargs)

        # vpc
        vpc = ec2.Vpc(self, "vpc",
            max_azs=1,
            cidr=cidr,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.ISOLATED,
                    name="SageMaker",
                    cidr_mask=24
                )
            ],
        )
        self.vpc_id = vpc.vpc_id
        #self.add_vpc_endpoints(self, vpc=vpc)

        # cloudformation outputs
        core.CfnOutput(
            self, "VPCID",
            description="VPC ID",
            value=vpc.vpc_id
        )

        self.output_props=props.copy()
        self.output_props['vpc']=vpc

        # security group for vpc endpoint
        sg = ec2.SecurityGroup(
            self, "vpce-sg",
            vpc=vpc,
            allow_all_outbound=True,
            description="allow tls for vpc endpoint"
        )

        # vpc endpoints
        vpc.add_gateway_endpoint(
            "s3-vpce",
            service=ec2.GatewayVpcEndpointAwsService.S3
        )

        vpc.add_interface_endpoint(
            "ecr.api-vpce",
            service=ec2.InterfaceVpcEndpointAwsService.ECR,
            private_dns_enabled=True,
            security_groups=[sg]
        )

        vpc.add_interface_endpoint(
            "ecr.dkr-vpce",
            service=ec2.InterfaceVpcEndpointAwsService.ECR_DOCKER,
            private_dns_enabled=True,
            security_groups=[sg]
        )

        vpc.add_interface_endpoint(
            "sagemaker.notebook-vpce",
            service=ec2.InterfaceVpcEndpointAwsService.SAGEMAKER_NOTEBOOK,
            private_dns_enabled=True,
            security_groups=[sg]
        )

        vpc.add_interface_endpoint(
            "sagemaker.api-vpce",
            service=ec2.InterfaceVpcEndpointAwsService.SAGEMAKER_API,
            private_dns_enabled=True,
            security_groups=[sg]
        )

        vpc.add_interface_endpoint(
            "sagemaker.runtime-vpce",
            service=ec2.InterfaceVpcEndpointAwsService.SAGEMAKER_RUNTIME,
            private_dns_enabled=True,
            security_groups=[sg]
        )

        vpc.add_interface_endpoint(
            "efs-vpce",
            service=ec2.InterfaceVpcEndpointAwsService.ELASTIC_FILESYSTEM,
            private_dns_enabled=True,
            security_groups=[sg]
        )

        vpc.add_interface_endpoint(
            "sts-vpce",
            service=ec2.InterfaceVpcEndpointAwsService.STS,
            private_dns_enabled=True,
            security_groups=[sg]
        )

    # pass objects to another stack
    @property
    def outputs(self):
        return self.output_props

#    def add_vpc_endpoints(self, vpc, **kwargs):

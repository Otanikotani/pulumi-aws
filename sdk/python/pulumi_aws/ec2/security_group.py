# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class SecurityGroup(pulumi.CustomResource):
    arn: pulumi.Output[str]
    """
    The ARN of the security group
    """
    description: pulumi.Output[str]
    """
    The security group description. Defaults to
    "Managed by Terraform". Cannot be "". __NOTE__: This field maps to the AWS
    `GroupDescription` attribute, for which there is no Update API. If you'd like
    to classify your security groups in a way that can be updated, use `tags`.
    """
    egress: pulumi.Output[list]
    """
    Can be specified multiple times for each
    egress rule. Each egress block supports fields documented below.
    This argument is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
    """
    ingress: pulumi.Output[list]
    """
    Can be specified multiple times for each
    ingress rule. Each ingress block supports fields documented below.
    This argument is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
    """
    name: pulumi.Output[str]
    """
    The name of the security group. If omitted, Terraform will
    assign a random, unique name
    """
    name_prefix: pulumi.Output[str]
    """
    Creates a unique name beginning with the specified
    prefix. Conflicts with `name`.
    """
    owner_id: pulumi.Output[str]
    """
    The owner ID.
    """
    revoke_rules_on_delete: pulumi.Output[bool]
    """
    Instruct Terraform to revoke all of the
    Security Groups attached ingress and egress rules before deleting the rule
    itself. This is normally not needed, however certain AWS services such as
    Elastic Map Reduce may automatically add required rules to security groups used
    with the service, and those rules may contain a cyclic dependency that prevent
    the security groups from being destroyed without removing the dependency first.
    Default `false`
    """
    tags: pulumi.Output[dict]
    """
    A mapping of tags to assign to the resource.
    """
    vpc_id: pulumi.Output[str]
    """
    The VPC ID.
    """
    def __init__(__self__, resource_name, opts=None, description=None, egress=None, ingress=None, name=None, name_prefix=None, revoke_rules_on_delete=None, tags=None, vpc_id=None, __name__=None, __opts__=None):
        """
        Provides a security group resource.
        
        > **NOTE on Security Groups and Security Group Rules:** Terraform currently
        provides both a standalone Security Group Rule resource (a single `ingress` or
        `egress` rule), and a Security Group resource with `ingress` and `egress` rules
        defined in-line. At this time you cannot use a Security Group with in-line rules
        in conjunction with any Security Group Rule resources. Doing so will cause
        a conflict of rule settings and will overwrite rules.
        
        > **NOTE:** Referencing Security Groups across VPC peering has certain restrictions. More information is available in the [VPC Peering User Guide](https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-security-groups.html).
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The security group description. Defaults to
               "Managed by Terraform". Cannot be "". __NOTE__: This field maps to the AWS
               `GroupDescription` attribute, for which there is no Update API. If you'd like
               to classify your security groups in a way that can be updated, use `tags`.
        :param pulumi.Input[list] egress: Can be specified multiple times for each
               egress rule. Each egress block supports fields documented below.
               This argument is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
        :param pulumi.Input[list] ingress: Can be specified multiple times for each
               ingress rule. Each ingress block supports fields documented below.
               This argument is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
        :param pulumi.Input[str] name: The name of the security group. If omitted, Terraform will
               assign a random, unique name
        :param pulumi.Input[str] name_prefix: Creates a unique name beginning with the specified
               prefix. Conflicts with `name`.
        :param pulumi.Input[bool] revoke_rules_on_delete: Instruct Terraform to revoke all of the
               Security Groups attached ingress and egress rules before deleting the rule
               itself. This is normally not needed, however certain AWS services such as
               Elastic Map Reduce may automatically add required rules to security groups used
               with the service, and those rules may contain a cyclic dependency that prevent
               the security groups from being destroyed without removing the dependency first.
               Default `false`
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] vpc_id: The VPC ID.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if not resource_name:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(resource_name, str):
            raise TypeError('Expected resource name to be a string')
        if opts and not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if description is None:
            description = 'Managed by Pulumi'
        __props__['description'] = description

        __props__['egress'] = egress

        __props__['ingress'] = ingress

        __props__['name'] = name

        __props__['name_prefix'] = name_prefix

        __props__['revoke_rules_on_delete'] = revoke_rules_on_delete

        __props__['tags'] = tags

        __props__['vpc_id'] = vpc_id

        __props__['arn'] = None
        __props__['owner_id'] = None

        super(SecurityGroup, __self__).__init__(
            'aws:ec2/securityGroup:SecurityGroup',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


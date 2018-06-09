# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class DefaultSecurityGroup(pulumi.CustomResource):
    """
    Provides a resource to manage the default AWS Security Group.
    
    For EC2 Classic accounts, each region comes with a Default Security Group.
    Additionally, each VPC created in AWS comes with a Default Security Group that can be managed, but not
    destroyed. **This is an advanced resource**, and has special caveats to be aware
    of when using it. Please read this document in its entirety before using this
    resource.
    
    The `aws_default_security_group` behaves differently from normal resources, in that
    Terraform does not _create_ this resource, but instead "adopts" it
    into management. We can do this because these default security groups cannot be
    destroyed, and are created with a known set of default ingress/egress rules.
    
    When Terraform first adopts the Default Security Group, it **immediately removes all
    ingress and egress rules in the Security Group**. It then proceeds to create any rules specified in the
    configuration. This step is required so that only the rules specified in the
    configuration are created.
    
    This resource treats its inline rules as absolute; only the rules defined
    inline are created, and any additions/removals external to this resource will
    result in diff shown. For these reasons, this resource is incompatible with the
    `aws_security_group_rule` resource.
    
    For more information about Default Security Groups, see the AWS Documentation on
    [Default Security Groups][aws-default-security-groups].
    """
    def __init__(__self__, __name__, __opts__=None, egress=None, ingress=None, revoke_rules_on_delete=None, tags=None, vpc_id=None):
        """Create a DefaultSecurityGroup resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if egress and not isinstance(egress, list):
            raise TypeError('Expected property egress to be a list')
        __self__.egress = egress
        """
        Can be specified multiple times for each
        egress rule. Each egress block supports fields documented below.
        """
        __props__['egress'] = egress

        if ingress and not isinstance(ingress, list):
            raise TypeError('Expected property ingress to be a list')
        __self__.ingress = ingress
        """
        Can be specified multiple times for each
        ingress rule. Each ingress block supports fields documented below.
        """
        __props__['ingress'] = ingress

        if revoke_rules_on_delete and not isinstance(revoke_rules_on_delete, bool):
            raise TypeError('Expected property revoke_rules_on_delete to be a bool')
        __self__.revoke_rules_on_delete = revoke_rules_on_delete
        __props__['revokeRulesOnDelete'] = revoke_rules_on_delete

        if tags and not isinstance(tags, dict):
            raise TypeError('Expected property tags to be a dict')
        __self__.tags = tags
        """
        A mapping of tags to assign to the resource.
        """
        __props__['tags'] = tags

        if vpc_id and not isinstance(vpc_id, basestring):
            raise TypeError('Expected property vpc_id to be a basestring')
        __self__.vpc_id = vpc_id
        """
        The VPC ID. **Note that changing
        the `vpc_id` will _not_ restore any default security group rules that were
        modified, added, or removed.** It will be left in its current state
        """
        __props__['vpcId'] = vpc_id

        __self__.arn = pulumi.runtime.UNKNOWN
        __self__.name = pulumi.runtime.UNKNOWN
        """
        The name of the security group
        """
        __self__.owner_id = pulumi.runtime.UNKNOWN
        """
        The owner ID.
        """

        super(DefaultSecurityGroup, __self__).__init__(
            'aws:ec2/defaultSecurityGroup:DefaultSecurityGroup',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'arn' in outs:
            self.arn = outs['arn']
        if 'egress' in outs:
            self.egress = outs['egress']
        if 'ingress' in outs:
            self.ingress = outs['ingress']
        if 'name' in outs:
            self.name = outs['name']
        if 'ownerId' in outs:
            self.owner_id = outs['ownerId']
        if 'revokeRulesOnDelete' in outs:
            self.revoke_rules_on_delete = outs['revokeRulesOnDelete']
        if 'tags' in outs:
            self.tags = outs['tags']
        if 'vpcId' in outs:
            self.vpc_id = outs['vpcId']
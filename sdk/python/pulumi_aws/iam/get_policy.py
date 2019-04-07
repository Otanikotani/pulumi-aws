# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class GetPolicyResult:
    """
    A collection of values returned by getPolicy.
    """
    def __init__(__self__, arn=None, description=None, name=None, path=None, policy=None, id=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        __self__.arn = arn
        """
        The Amazon Resource Name (ARN) specifying the policy.
        """
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        __self__.description = description
        """
        The description of the policy.
        """
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        """
        The name of the IAM policy.
        """
        if path and not isinstance(path, str):
            raise TypeError("Expected argument 'path' to be a str")
        __self__.path = path
        """
        The path to the policy.
        """
        if policy and not isinstance(policy, str):
            raise TypeError("Expected argument 'policy' to be a str")
        __self__.policy = policy
        """
        The policy document of the policy.
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

async def get_policy(arn=None,opts=None):
    """
    This data source can be used to fetch information about a specific
    IAM policy.
    """
    __args__ = dict()

    __args__['arn'] = arn
    __ret__ = await pulumi.runtime.invoke('aws:iam/getPolicy:getPolicy', __args__, opts=opts)

    return GetPolicyResult(
        arn=__ret__.get('arn'),
        description=__ret__.get('description'),
        name=__ret__.get('name'),
        path=__ret__.get('path'),
        policy=__ret__.get('policy'),
        id=__ret__.get('id'))

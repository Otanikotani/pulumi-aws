# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class Model(pulumi.CustomResource):
    content_type: pulumi.Output[str]
    """
    The content type of the model
    """
    description: pulumi.Output[str]
    """
    The description of the model
    """
    name: pulumi.Output[str]
    """
    The name of the model
    """
    rest_api: pulumi.Output[str]
    """
    The ID of the associated REST API
    """
    schema: pulumi.Output[str]
    """
    The schema of the model in a JSON form
    """
    def __init__(__self__, resource_name, opts=None, content_type=None, description=None, name=None, rest_api=None, schema=None, __name__=None, __opts__=None):
        """
        Provides a Model for a API Gateway.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] content_type: The content type of the model
        :param pulumi.Input[str] description: The description of the model
        :param pulumi.Input[str] name: The name of the model
        :param pulumi.Input[str] rest_api: The ID of the associated REST API
        :param pulumi.Input[str] schema: The schema of the model in a JSON form
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

        if content_type is None:
            raise TypeError("Missing required property 'content_type'")
        __props__['content_type'] = content_type

        __props__['description'] = description

        __props__['name'] = name

        if rest_api is None:
            raise TypeError("Missing required property 'rest_api'")
        __props__['rest_api'] = rest_api

        __props__['schema'] = schema

        super(Model, __self__).__init__(
            'aws:apigateway/model:Model',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


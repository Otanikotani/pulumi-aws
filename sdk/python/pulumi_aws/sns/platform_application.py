# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class PlatformApplication(pulumi.CustomResource):
    arn: pulumi.Output[str]
    """
    The ARN of the SNS platform application
    """
    event_delivery_failure_topic_arn: pulumi.Output[str]
    """
    SNS Topic triggered when a delivery to any of the platform endpoints associated with your platform application encounters a permanent failure.
    """
    event_endpoint_created_topic_arn: pulumi.Output[str]
    """
    SNS Topic triggered when a new platform endpoint is added to your platform application.
    """
    event_endpoint_deleted_topic_arn: pulumi.Output[str]
    """
    SNS Topic triggered when an existing platform endpoint is deleted from your platform application.
    """
    event_endpoint_updated_topic_arn: pulumi.Output[str]
    """
    SNS Topic triggered when an existing platform endpoint is changed from your platform application.
    """
    failure_feedback_role_arn: pulumi.Output[str]
    """
    The IAM role permitted to receive failure feedback for this application.
    """
    name: pulumi.Output[str]
    """
    The friendly name for the SNS platform application
    """
    platform: pulumi.Output[str]
    """
    The platform that the app is registered with. See [Platform][1] for supported platforms.
    """
    platform_credential: pulumi.Output[str]
    """
    Application Platform credential. See [Credential][1] for type of credential required for platform. The value of this attribute when stored into the Terraform state is only a hash of the real value, so therefore it is not practical to use this as an attribute for other resources.
    """
    platform_principal: pulumi.Output[str]
    """
    Application Platform principal. See [Principal][2] for type of principal required for platform. The value of this attribute when stored into the Terraform state is only a hash of the real value, so therefore it is not practical to use this as an attribute for other resources.
    """
    success_feedback_role_arn: pulumi.Output[str]
    """
    The IAM role permitted to receive success feedback for this application.
    """
    success_feedback_sample_rate: pulumi.Output[str]
    """
    The percentage of success to sample (0-100)
    """
    def __init__(__self__, resource_name, opts=None, event_delivery_failure_topic_arn=None, event_endpoint_created_topic_arn=None, event_endpoint_deleted_topic_arn=None, event_endpoint_updated_topic_arn=None, failure_feedback_role_arn=None, name=None, platform=None, platform_credential=None, platform_principal=None, success_feedback_role_arn=None, success_feedback_sample_rate=None, __name__=None, __opts__=None):
        """
        Provides an SNS platform application resource
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] event_delivery_failure_topic_arn: SNS Topic triggered when a delivery to any of the platform endpoints associated with your platform application encounters a permanent failure.
        :param pulumi.Input[str] event_endpoint_created_topic_arn: SNS Topic triggered when a new platform endpoint is added to your platform application.
        :param pulumi.Input[str] event_endpoint_deleted_topic_arn: SNS Topic triggered when an existing platform endpoint is deleted from your platform application.
        :param pulumi.Input[str] event_endpoint_updated_topic_arn: SNS Topic triggered when an existing platform endpoint is changed from your platform application.
        :param pulumi.Input[str] failure_feedback_role_arn: The IAM role permitted to receive failure feedback for this application.
        :param pulumi.Input[str] name: The friendly name for the SNS platform application
        :param pulumi.Input[str] platform: The platform that the app is registered with. See [Platform][1] for supported platforms.
        :param pulumi.Input[str] platform_credential: Application Platform credential. See [Credential][1] for type of credential required for platform. The value of this attribute when stored into the Terraform state is only a hash of the real value, so therefore it is not practical to use this as an attribute for other resources.
        :param pulumi.Input[str] platform_principal: Application Platform principal. See [Principal][2] for type of principal required for platform. The value of this attribute when stored into the Terraform state is only a hash of the real value, so therefore it is not practical to use this as an attribute for other resources.
        :param pulumi.Input[str] success_feedback_role_arn: The IAM role permitted to receive success feedback for this application.
        :param pulumi.Input[str] success_feedback_sample_rate: The percentage of success to sample (0-100)
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

        __props__['event_delivery_failure_topic_arn'] = event_delivery_failure_topic_arn

        __props__['event_endpoint_created_topic_arn'] = event_endpoint_created_topic_arn

        __props__['event_endpoint_deleted_topic_arn'] = event_endpoint_deleted_topic_arn

        __props__['event_endpoint_updated_topic_arn'] = event_endpoint_updated_topic_arn

        __props__['failure_feedback_role_arn'] = failure_feedback_role_arn

        __props__['name'] = name

        if platform is None:
            raise TypeError("Missing required property 'platform'")
        __props__['platform'] = platform

        if platform_credential is None:
            raise TypeError("Missing required property 'platform_credential'")
        __props__['platform_credential'] = platform_credential

        __props__['platform_principal'] = platform_principal

        __props__['success_feedback_role_arn'] = success_feedback_role_arn

        __props__['success_feedback_sample_rate'] = success_feedback_sample_rate

        __props__['arn'] = None

        super(PlatformApplication, __self__).__init__(
            'aws:sns/platformApplication:PlatformApplication',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


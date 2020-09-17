# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['Integration']


class Integration(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_id: Optional[pulumi.Input[str]] = None,
                 connection_id: Optional[pulumi.Input[str]] = None,
                 connection_type: Optional[pulumi.Input[str]] = None,
                 content_handling_strategy: Optional[pulumi.Input[str]] = None,
                 credentials_arn: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 integration_method: Optional[pulumi.Input[str]] = None,
                 integration_type: Optional[pulumi.Input[str]] = None,
                 integration_uri: Optional[pulumi.Input[str]] = None,
                 passthrough_behavior: Optional[pulumi.Input[str]] = None,
                 payload_format_version: Optional[pulumi.Input[str]] = None,
                 request_parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 request_templates: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 template_selection_expression: Optional[pulumi.Input[str]] = None,
                 timeout_milliseconds: Optional[pulumi.Input[int]] = None,
                 tls_config: Optional[pulumi.Input[pulumi.InputType['IntegrationTlsConfigArgs']]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages an Amazon API Gateway Version 2 integration.
        More information can be found in the [Amazon API Gateway Developer Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api.html).

        ## Example Usage
        ### Basic

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.apigatewayv2.Integration("example",
            api_id=aws_apigatewayv2_api["example"]["id"],
            integration_type="MOCK")
        ```
        ### Lambda Integration

        ```python
        import pulumi
        import pulumi_aws as aws

        example_function = aws.lambda_.Function("exampleFunction",
            code=pulumi.FileArchive("example.zip"),
            role=aws_iam_role["example"]["arn"],
            handler="index.handler",
            runtime="nodejs12.x")
        example_integration = aws.apigatewayv2.Integration("exampleIntegration",
            api_id=aws_apigatewayv2_api["example"]["id"],
            integration_type="AWS",
            connection_type="INTERNET",
            content_handling_strategy="CONVERT_TO_TEXT",
            description="Lambda example",
            integration_method="POST",
            integration_uri=example_function.invoke_arn,
            passthrough_behavior="WHEN_NO_MATCH")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_id: The API identifier.
        :param pulumi.Input[str] connection_id: The ID of the VPC link for a private integration. Supported only for HTTP APIs.
        :param pulumi.Input[str] connection_type: The type of the network connection to the integration endpoint. Valid values: `INTERNET`, `VPC_LINK`. Default is `INTERNET`.
        :param pulumi.Input[str] content_handling_strategy: How to handle response payload content type conversions. Valid values: `CONVERT_TO_BINARY`, `CONVERT_TO_TEXT`. Supported only for WebSocket APIs.
        :param pulumi.Input[str] credentials_arn: The credentials required for the integration, if any.
        :param pulumi.Input[str] description: The description of the integration.
        :param pulumi.Input[str] integration_method: The integration's HTTP method. Must be specified if `integration_type` is not `MOCK`.
        :param pulumi.Input[str] integration_type: The integration type of an integration.
               Valid values: `AWS`, `AWS_PROXY`, `HTTP`, `HTTP_PROXY`, `MOCK`.
        :param pulumi.Input[str] integration_uri: The URI of the Lambda function for a Lambda proxy integration, when `integration_type` is `AWS_PROXY`.
               For an `HTTP` integration, specify a fully-qualified URL. For an HTTP API private integration, specify the ARN of an Application Load Balancer listener, Network Load Balancer listener, or AWS Cloud Map service.
        :param pulumi.Input[str] passthrough_behavior: The pass-through behavior for incoming requests based on the Content-Type header in the request, and the available mapping templates specified as the `request_templates` attribute.
               Valid values: `WHEN_NO_MATCH`, `WHEN_NO_TEMPLATES`, `NEVER`. Default is `WHEN_NO_MATCH`. Supported only for WebSocket APIs.
        :param pulumi.Input[str] payload_format_version: The [format of the payload](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html#http-api-develop-integrations-lambda.proxy-format) sent to an integration. Valid values: `1.0`, `2.0`. Default is `1.0`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] request_parameters: A key-value map specifying request parameters that are passed from the method request to the backend.
               Supported only for WebSocket APIs.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] request_templates: A map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client. Supported only for WebSocket APIs.
        :param pulumi.Input[str] template_selection_expression: The [template selection expression](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-template-selection-expressions) for the integration.
        :param pulumi.Input[int] timeout_milliseconds: Custom timeout between 50 and 29,000 milliseconds. The default value is 29,000 milliseconds or 29 seconds.
        :param pulumi.Input[pulumi.InputType['IntegrationTlsConfigArgs']] tls_config: The TLS configuration for a private integration. Supported only for HTTP APIs.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            if api_id is None:
                raise TypeError("Missing required property 'api_id'")
            __props__['api_id'] = api_id
            __props__['connection_id'] = connection_id
            __props__['connection_type'] = connection_type
            __props__['content_handling_strategy'] = content_handling_strategy
            __props__['credentials_arn'] = credentials_arn
            __props__['description'] = description
            __props__['integration_method'] = integration_method
            if integration_type is None:
                raise TypeError("Missing required property 'integration_type'")
            __props__['integration_type'] = integration_type
            __props__['integration_uri'] = integration_uri
            __props__['passthrough_behavior'] = passthrough_behavior
            __props__['payload_format_version'] = payload_format_version
            __props__['request_parameters'] = request_parameters
            __props__['request_templates'] = request_templates
            __props__['template_selection_expression'] = template_selection_expression
            __props__['timeout_milliseconds'] = timeout_milliseconds
            __props__['tls_config'] = tls_config
            __props__['integration_response_selection_expression'] = None
        super(Integration, __self__).__init__(
            'aws:apigatewayv2/integration:Integration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            api_id: Optional[pulumi.Input[str]] = None,
            connection_id: Optional[pulumi.Input[str]] = None,
            connection_type: Optional[pulumi.Input[str]] = None,
            content_handling_strategy: Optional[pulumi.Input[str]] = None,
            credentials_arn: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            integration_method: Optional[pulumi.Input[str]] = None,
            integration_response_selection_expression: Optional[pulumi.Input[str]] = None,
            integration_type: Optional[pulumi.Input[str]] = None,
            integration_uri: Optional[pulumi.Input[str]] = None,
            passthrough_behavior: Optional[pulumi.Input[str]] = None,
            payload_format_version: Optional[pulumi.Input[str]] = None,
            request_parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            request_templates: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            template_selection_expression: Optional[pulumi.Input[str]] = None,
            timeout_milliseconds: Optional[pulumi.Input[int]] = None,
            tls_config: Optional[pulumi.Input[pulumi.InputType['IntegrationTlsConfigArgs']]] = None) -> 'Integration':
        """
        Get an existing Integration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_id: The API identifier.
        :param pulumi.Input[str] connection_id: The ID of the VPC link for a private integration. Supported only for HTTP APIs.
        :param pulumi.Input[str] connection_type: The type of the network connection to the integration endpoint. Valid values: `INTERNET`, `VPC_LINK`. Default is `INTERNET`.
        :param pulumi.Input[str] content_handling_strategy: How to handle response payload content type conversions. Valid values: `CONVERT_TO_BINARY`, `CONVERT_TO_TEXT`. Supported only for WebSocket APIs.
        :param pulumi.Input[str] credentials_arn: The credentials required for the integration, if any.
        :param pulumi.Input[str] description: The description of the integration.
        :param pulumi.Input[str] integration_method: The integration's HTTP method. Must be specified if `integration_type` is not `MOCK`.
        :param pulumi.Input[str] integration_response_selection_expression: The [integration response selection expression](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-integration-response-selection-expressions) for the integration.
        :param pulumi.Input[str] integration_type: The integration type of an integration.
               Valid values: `AWS`, `AWS_PROXY`, `HTTP`, `HTTP_PROXY`, `MOCK`.
        :param pulumi.Input[str] integration_uri: The URI of the Lambda function for a Lambda proxy integration, when `integration_type` is `AWS_PROXY`.
               For an `HTTP` integration, specify a fully-qualified URL. For an HTTP API private integration, specify the ARN of an Application Load Balancer listener, Network Load Balancer listener, or AWS Cloud Map service.
        :param pulumi.Input[str] passthrough_behavior: The pass-through behavior for incoming requests based on the Content-Type header in the request, and the available mapping templates specified as the `request_templates` attribute.
               Valid values: `WHEN_NO_MATCH`, `WHEN_NO_TEMPLATES`, `NEVER`. Default is `WHEN_NO_MATCH`. Supported only for WebSocket APIs.
        :param pulumi.Input[str] payload_format_version: The [format of the payload](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html#http-api-develop-integrations-lambda.proxy-format) sent to an integration. Valid values: `1.0`, `2.0`. Default is `1.0`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] request_parameters: A key-value map specifying request parameters that are passed from the method request to the backend.
               Supported only for WebSocket APIs.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] request_templates: A map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client. Supported only for WebSocket APIs.
        :param pulumi.Input[str] template_selection_expression: The [template selection expression](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-template-selection-expressions) for the integration.
        :param pulumi.Input[int] timeout_milliseconds: Custom timeout between 50 and 29,000 milliseconds. The default value is 29,000 milliseconds or 29 seconds.
        :param pulumi.Input[pulumi.InputType['IntegrationTlsConfigArgs']] tls_config: The TLS configuration for a private integration. Supported only for HTTP APIs.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["api_id"] = api_id
        __props__["connection_id"] = connection_id
        __props__["connection_type"] = connection_type
        __props__["content_handling_strategy"] = content_handling_strategy
        __props__["credentials_arn"] = credentials_arn
        __props__["description"] = description
        __props__["integration_method"] = integration_method
        __props__["integration_response_selection_expression"] = integration_response_selection_expression
        __props__["integration_type"] = integration_type
        __props__["integration_uri"] = integration_uri
        __props__["passthrough_behavior"] = passthrough_behavior
        __props__["payload_format_version"] = payload_format_version
        __props__["request_parameters"] = request_parameters
        __props__["request_templates"] = request_templates
        __props__["template_selection_expression"] = template_selection_expression
        __props__["timeout_milliseconds"] = timeout_milliseconds
        __props__["tls_config"] = tls_config
        return Integration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Output[str]:
        """
        The API identifier.
        """
        return pulumi.get(self, "api_id")

    @property
    @pulumi.getter(name="connectionId")
    def connection_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of the VPC link for a private integration. Supported only for HTTP APIs.
        """
        return pulumi.get(self, "connection_id")

    @property
    @pulumi.getter(name="connectionType")
    def connection_type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of the network connection to the integration endpoint. Valid values: `INTERNET`, `VPC_LINK`. Default is `INTERNET`.
        """
        return pulumi.get(self, "connection_type")

    @property
    @pulumi.getter(name="contentHandlingStrategy")
    def content_handling_strategy(self) -> pulumi.Output[Optional[str]]:
        """
        How to handle response payload content type conversions. Valid values: `CONVERT_TO_BINARY`, `CONVERT_TO_TEXT`. Supported only for WebSocket APIs.
        """
        return pulumi.get(self, "content_handling_strategy")

    @property
    @pulumi.getter(name="credentialsArn")
    def credentials_arn(self) -> pulumi.Output[Optional[str]]:
        """
        The credentials required for the integration, if any.
        """
        return pulumi.get(self, "credentials_arn")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the integration.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="integrationMethod")
    def integration_method(self) -> pulumi.Output[Optional[str]]:
        """
        The integration's HTTP method. Must be specified if `integration_type` is not `MOCK`.
        """
        return pulumi.get(self, "integration_method")

    @property
    @pulumi.getter(name="integrationResponseSelectionExpression")
    def integration_response_selection_expression(self) -> pulumi.Output[str]:
        """
        The [integration response selection expression](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-integration-response-selection-expressions) for the integration.
        """
        return pulumi.get(self, "integration_response_selection_expression")

    @property
    @pulumi.getter(name="integrationType")
    def integration_type(self) -> pulumi.Output[str]:
        """
        The integration type of an integration.
        Valid values: `AWS`, `AWS_PROXY`, `HTTP`, `HTTP_PROXY`, `MOCK`.
        """
        return pulumi.get(self, "integration_type")

    @property
    @pulumi.getter(name="integrationUri")
    def integration_uri(self) -> pulumi.Output[Optional[str]]:
        """
        The URI of the Lambda function for a Lambda proxy integration, when `integration_type` is `AWS_PROXY`.
        For an `HTTP` integration, specify a fully-qualified URL. For an HTTP API private integration, specify the ARN of an Application Load Balancer listener, Network Load Balancer listener, or AWS Cloud Map service.
        """
        return pulumi.get(self, "integration_uri")

    @property
    @pulumi.getter(name="passthroughBehavior")
    def passthrough_behavior(self) -> pulumi.Output[Optional[str]]:
        """
        The pass-through behavior for incoming requests based on the Content-Type header in the request, and the available mapping templates specified as the `request_templates` attribute.
        Valid values: `WHEN_NO_MATCH`, `WHEN_NO_TEMPLATES`, `NEVER`. Default is `WHEN_NO_MATCH`. Supported only for WebSocket APIs.
        """
        return pulumi.get(self, "passthrough_behavior")

    @property
    @pulumi.getter(name="payloadFormatVersion")
    def payload_format_version(self) -> pulumi.Output[Optional[str]]:
        """
        The [format of the payload](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html#http-api-develop-integrations-lambda.proxy-format) sent to an integration. Valid values: `1.0`, `2.0`. Default is `1.0`.
        """
        return pulumi.get(self, "payload_format_version")

    @property
    @pulumi.getter(name="requestParameters")
    def request_parameters(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A key-value map specifying request parameters that are passed from the method request to the backend.
        Supported only for WebSocket APIs.
        """
        return pulumi.get(self, "request_parameters")

    @property
    @pulumi.getter(name="requestTemplates")
    def request_templates(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client. Supported only for WebSocket APIs.
        """
        return pulumi.get(self, "request_templates")

    @property
    @pulumi.getter(name="templateSelectionExpression")
    def template_selection_expression(self) -> pulumi.Output[Optional[str]]:
        """
        The [template selection expression](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-template-selection-expressions) for the integration.
        """
        return pulumi.get(self, "template_selection_expression")

    @property
    @pulumi.getter(name="timeoutMilliseconds")
    def timeout_milliseconds(self) -> pulumi.Output[Optional[int]]:
        """
        Custom timeout between 50 and 29,000 milliseconds. The default value is 29,000 milliseconds or 29 seconds.
        """
        return pulumi.get(self, "timeout_milliseconds")

    @property
    @pulumi.getter(name="tlsConfig")
    def tls_config(self) -> pulumi.Output[Optional['outputs.IntegrationTlsConfig']]:
        """
        The TLS configuration for a private integration. Supported only for HTTP APIs.
        """
        return pulumi.get(self, "tls_config")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


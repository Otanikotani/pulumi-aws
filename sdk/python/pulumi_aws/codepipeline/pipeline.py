# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class Pipeline(pulumi.CustomResource):
    """
    Provides a CodePipeline.
    
    ~> **NOTE on `aws_codepipeline`:** - the `GITHUB_TOKEN` environment variable must be set if the GitHub provider is specified.
    """
    def __init__(__self__, __name__, __opts__=None, artifact_store=None, name=None, role_arn=None, stages=None):
        """Create a Pipeline resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not artifact_store:
            raise TypeError('Missing required property artifact_store')
        elif not isinstance(artifact_store, dict):
            raise TypeError('Expected property artifact_store to be a dict')
        __self__.artifact_store = artifact_store
        """
        An artifact_store block. Artifact stores are documented below.
        * `stage` (Minimum of at least two `stage` blocks is required) A stage block. Stages are documented below.
        """
        __props__['artifactStore'] = artifact_store

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        The action declaration's name.
        """
        __props__['name'] = name

        if not role_arn:
            raise TypeError('Missing required property role_arn')
        elif not isinstance(role_arn, basestring):
            raise TypeError('Expected property role_arn to be a basestring')
        __self__.role_arn = role_arn
        """
        The ARN of the IAM service role that will perform the declared action. This is assumed through the roleArn for the pipeline.
        """
        __props__['roleArn'] = role_arn

        if not stages:
            raise TypeError('Missing required property stages')
        elif not isinstance(stages, list):
            raise TypeError('Expected property stages to be a list')
        __self__.stages = stages
        __props__['stages'] = stages

        __self__.arn = pulumi.runtime.UNKNOWN
        """
        The codepipeline ARN.
        """

        super(Pipeline, __self__).__init__(
            'aws:codepipeline/pipeline:Pipeline',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'arn' in outs:
            self.arn = outs['arn']
        if 'artifactStore' in outs:
            self.artifact_store = outs['artifactStore']
        if 'name' in outs:
            self.name = outs['name']
        if 'roleArn' in outs:
            self.role_arn = outs['roleArn']
        if 'stages' in outs:
            self.stages = outs['stages']

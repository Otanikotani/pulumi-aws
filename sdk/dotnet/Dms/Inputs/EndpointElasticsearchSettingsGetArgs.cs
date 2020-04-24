// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Dms.Inputs
{

    public sealed class EndpointElasticsearchSettingsGetArgs : Pulumi.ResourceArgs
    {
        [Input("endpointUri", required: true)]
        public Input<string> EndpointUri { get; set; } = null!;

        [Input("errorRetryDuration")]
        public Input<int>? ErrorRetryDuration { get; set; }

        [Input("fullLoadErrorPercentage")]
        public Input<int>? FullLoadErrorPercentage { get; set; }

        [Input("serviceAccessRoleArn", required: true)]
        public Input<string> ServiceAccessRoleArn { get; set; } = null!;

        public EndpointElasticsearchSettingsGetArgs()
        {
        }
    }
}
// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.WafV2
{
    public static class GetRegexPatternSet
    {
        /// <summary>
        /// Retrieves the summary of a WAFv2 Regex Pattern Set.
        /// 
        /// {{% examples %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetRegexPatternSetResult> InvokeAsync(GetRegexPatternSetArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetRegexPatternSetResult>("aws:wafv2/getRegexPatternSet:getRegexPatternSet", args ?? new GetRegexPatternSetArgs(), options.WithVersion());
    }


    public sealed class GetRegexPatternSetArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of the WAFv2 Regex Pattern Set.
        /// </summary>
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        /// <summary>
        /// Specifies whether this is for an AWS CloudFront distribution or for a regional application. Valid values are `CLOUDFRONT` or `REGIONAL`. To work with CloudFront, you must also specify the region `us-east-1` (N. Virginia) on the AWS provider.
        /// </summary>
        [Input("scope", required: true)]
        public string Scope { get; set; } = null!;

        public GetRegexPatternSetArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetRegexPatternSetResult
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) of the entity.
        /// </summary>
        public readonly string Arn;
        /// <summary>
        /// The description of the set that helps with identification.
        /// </summary>
        public readonly string Description;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string Name;
        /// <summary>
        /// One or more blocks of regular expression patterns that AWS WAF is searching for. See Regular Expression below for details.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetRegexPatternSetRegularExpressionResult> RegularExpressions;
        public readonly string Scope;

        [OutputConstructor]
        private GetRegexPatternSetResult(
            string arn,

            string description,

            string id,

            string name,

            ImmutableArray<Outputs.GetRegexPatternSetRegularExpressionResult> regularExpressions,

            string scope)
        {
            Arn = arn;
            Description = description;
            Id = id;
            Name = name;
            RegularExpressions = regularExpressions;
            Scope = scope;
        }
    }
}

// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.CodeBuild.Outputs
{

    [OutputType]
    public sealed class ProjectSource
    {
        /// <summary>
        /// Information about the authorization settings for AWS CodeBuild to access the source code to be built. Auth blocks are documented below.
        /// </summary>
        public readonly ImmutableArray<Outputs.ProjectSourceAuth> Auths;
        /// <summary>
        /// The build spec declaration to use for this build project's related builds. This must be set when `type` is `NO_SOURCE`.
        /// </summary>
        public readonly string? Buildspec;
        /// <summary>
        /// Truncate git history to this many commits.
        /// </summary>
        public readonly int? GitCloneDepth;
        /// <summary>
        /// Information about the Git submodules configuration for an AWS CodeBuild build project. Git submodules config blocks are documented below. This option is only valid when the `type` is `CODECOMMIT`.
        /// </summary>
        public readonly Outputs.ProjectSourceGitSubmodulesConfig? GitSubmodulesConfig;
        /// <summary>
        /// Ignore SSL warnings when connecting to source control.
        /// </summary>
        public readonly bool? InsecureSsl;
        /// <summary>
        /// The location of the source code from git or s3.
        /// </summary>
        public readonly string? Location;
        /// <summary>
        /// Set to `true` to report the status of a build's start and finish to your source provider. This option is only valid when the `type` is `BITBUCKET` or `GITHUB`.
        /// </summary>
        public readonly bool? ReportBuildStatus;
        /// <summary>
        /// The type of repository that contains the source code to be built. Valid values for this parameter are: `CODECOMMIT`, `CODEPIPELINE`, `GITHUB`, `GITHUB_ENTERPRISE`, `BITBUCKET`, `S3` or `NO_SOURCE`.
        /// </summary>
        public readonly string Type;

        [OutputConstructor]
        private ProjectSource(
            ImmutableArray<Outputs.ProjectSourceAuth> auths,

            string? buildspec,

            int? gitCloneDepth,

            Outputs.ProjectSourceGitSubmodulesConfig? gitSubmodulesConfig,

            bool? insecureSsl,

            string? location,

            bool? reportBuildStatus,

            string type)
        {
            Auths = auths;
            Buildspec = buildspec;
            GitCloneDepth = gitCloneDepth;
            GitSubmodulesConfig = gitSubmodulesConfig;
            InsecureSsl = insecureSsl;
            Location = location;
            ReportBuildStatus = reportBuildStatus;
            Type = type;
        }
    }
}
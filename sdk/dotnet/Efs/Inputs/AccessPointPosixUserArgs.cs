// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Efs.Inputs
{

    public sealed class AccessPointPosixUserArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The POSIX group ID used for all file system operations using this access point.
        /// </summary>
        [Input("gid", required: true)]
        public Input<int> Gid { get; set; } = null!;

        [Input("secondaryGids")]
        private InputList<int>? _secondaryGids;

        /// <summary>
        /// Secondary POSIX group IDs used for all file system operations using this access point.
        /// </summary>
        public InputList<int> SecondaryGids
        {
            get => _secondaryGids ?? (_secondaryGids = new InputList<int>());
            set => _secondaryGids = value;
        }

        /// <summary>
        /// he POSIX user ID used for all file system operations using this access point.
        /// </summary>
        [Input("uid", required: true)]
        public Input<int> Uid { get; set; } = null!;

        public AccessPointPosixUserArgs()
        {
        }
    }
}

// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Efs.Outputs
{

    [OutputType]
    public sealed class AccessPointRootDirectoryCreationInfo
    {
        /// <summary>
        /// Specifies the POSIX group ID to apply to the `root_directory`.
        /// </summary>
        public readonly int OwnerGid;
        /// <summary>
        /// Specifies the POSIX user ID to apply to the `root_directory`.
        /// </summary>
        public readonly int OwnerUid;
        /// <summary>
        /// Specifies the POSIX permissions to apply to the RootDirectory, in the format of an octal number representing the file's mode bits.
        /// </summary>
        public readonly string Permissions;

        [OutputConstructor]
        private AccessPointRootDirectoryCreationInfo(
            int ownerGid,

            int ownerUid,

            string permissions)
        {
            OwnerGid = ownerGid;
            OwnerUid = ownerUid;
            Permissions = permissions;
        }
    }
}

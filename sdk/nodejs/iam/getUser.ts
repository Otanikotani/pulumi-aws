// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";

/**
 * This data source can be used to fetch information about a specific
 * IAM user. By using this data source, you can reference IAM user
 * properties without having to hard code ARNs or unique IDs as input.
 */
export function getUser(args: GetUserArgs): Promise<GetUserResult> {
    return pulumi.runtime.invoke("aws:iam/getUser:getUser", {
        "userName": args.userName,
    });
}

/**
 * A collection of arguments for invoking getUser.
 */
export interface GetUserArgs {
    /**
     * The friendly IAM user name to match.
     */
    readonly userName: string;
}

/**
 * A collection of values returned by getUser.
 */
export interface GetUserResult {
    /**
     * The Amazon Resource Name (ARN) assigned by AWS for this user.
     */
    readonly arn: string;
    /**
     * Path in which this user was created.
     */
    readonly path: string;
    /**
     * The ARN of the policy that is used to set the permissions boundary for the user.
     */
    readonly permissionsBoundary: string;
    /**
     * The unique ID assigned by AWS for this user.
     */
    readonly userId: string;
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}

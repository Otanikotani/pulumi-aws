// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * > **NOTE:** This resource interacts with [Amazon Macie Classic](https://docs.aws.amazon.com/macie/latest/userguide/what-is-macie.html). Macie Classic cannot be activated in new accounts. See the [FAQ](https://aws.amazon.com/macie/classic-faqs/) for more details.
 *
 * Associates an AWS account with Amazon Macie as a member account.
 *
 * > **NOTE:** Before using Amazon Macie for the first time it must be enabled manually. Instructions are [here](https://docs.aws.amazon.com/macie/latest/userguide/macie-setting-up.html#macie-setting-up-enable).
 *
 * ## Example Usage
 *
 *
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 *
 * const example = new aws.macie.MemberAccountAssociation("example", {
 *     memberAccountId: "123456789012",
 * });
 * ```
 */
export class MemberAccountAssociation extends pulumi.CustomResource {
    /**
     * Get an existing MemberAccountAssociation resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: MemberAccountAssociationState, opts?: pulumi.CustomResourceOptions): MemberAccountAssociation {
        return new MemberAccountAssociation(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:macie/memberAccountAssociation:MemberAccountAssociation';

    /**
     * Returns true if the given object is an instance of MemberAccountAssociation.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is MemberAccountAssociation {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === MemberAccountAssociation.__pulumiType;
    }

    /**
     * The ID of the AWS account that you want to associate with Amazon Macie as a member account.
     */
    public readonly memberAccountId!: pulumi.Output<string>;

    /**
     * Create a MemberAccountAssociation resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: MemberAccountAssociationArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: MemberAccountAssociationArgs | MemberAccountAssociationState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as MemberAccountAssociationState | undefined;
            inputs["memberAccountId"] = state ? state.memberAccountId : undefined;
        } else {
            const args = argsOrState as MemberAccountAssociationArgs | undefined;
            if (!args || args.memberAccountId === undefined) {
                throw new Error("Missing required property 'memberAccountId'");
            }
            inputs["memberAccountId"] = args ? args.memberAccountId : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(MemberAccountAssociation.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering MemberAccountAssociation resources.
 */
export interface MemberAccountAssociationState {
    /**
     * The ID of the AWS account that you want to associate with Amazon Macie as a member account.
     */
    readonly memberAccountId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a MemberAccountAssociation resource.
 */
export interface MemberAccountAssociationArgs {
    /**
     * The ID of the AWS account that you want to associate with Amazon Macie as a member account.
     */
    readonly memberAccountId: pulumi.Input<string>;
}

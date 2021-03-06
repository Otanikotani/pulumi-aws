// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Provides an RDS DB proxy target resource.
 */
export class ProxyTarget extends pulumi.CustomResource {
    /**
     * Get an existing ProxyTarget resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ProxyTargetState, opts?: pulumi.CustomResourceOptions): ProxyTarget {
        return new ProxyTarget(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:rds/proxyTarget:ProxyTarget';

    /**
     * Returns true if the given object is an instance of ProxyTarget.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ProxyTarget {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ProxyTarget.__pulumiType;
    }

    /**
     * DB cluster identifier.
     */
    public readonly dbClusterIdentifier!: pulumi.Output<string | undefined>;
    /**
     * DB instance identifier.
     */
    public readonly dbInstanceIdentifier!: pulumi.Output<string | undefined>;
    /**
     * The name of the DB proxy.
     */
    public readonly dbProxyName!: pulumi.Output<string>;
    /**
     * Hostname for the target RDS DB Instance. Only returned for `RDS_INSTANCE` type.
     */
    public /*out*/ readonly endpoint!: pulumi.Output<string>;
    /**
     * Port for the target RDS DB Instance or Aurora DB Cluster.
     */
    public /*out*/ readonly port!: pulumi.Output<number>;
    /**
     * Identifier representing the DB Instance or DB Cluster target.
     */
    public /*out*/ readonly rdsResourceId!: pulumi.Output<string>;
    /**
     * Amazon Resource Name (ARN) for the DB instance or DB cluster. Currently not returned by the RDS API.
     */
    public /*out*/ readonly targetArn!: pulumi.Output<string>;
    /**
     * The name of the target group.
     */
    public readonly targetGroupName!: pulumi.Output<string>;
    /**
     * DB Cluster identifier for the DB Instance target. Not returned unless manually importing an `RDS_INSTANCE` target that is part of a DB Cluster.
     */
    public /*out*/ readonly trackedClusterId!: pulumi.Output<string>;
    /**
     * Type of target. e.g. `RDS_INSTANCE` or `TRACKED_CLUSTER`
     */
    public /*out*/ readonly type!: pulumi.Output<string>;

    /**
     * Create a ProxyTarget resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ProxyTargetArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ProxyTargetArgs | ProxyTargetState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as ProxyTargetState | undefined;
            inputs["dbClusterIdentifier"] = state ? state.dbClusterIdentifier : undefined;
            inputs["dbInstanceIdentifier"] = state ? state.dbInstanceIdentifier : undefined;
            inputs["dbProxyName"] = state ? state.dbProxyName : undefined;
            inputs["endpoint"] = state ? state.endpoint : undefined;
            inputs["port"] = state ? state.port : undefined;
            inputs["rdsResourceId"] = state ? state.rdsResourceId : undefined;
            inputs["targetArn"] = state ? state.targetArn : undefined;
            inputs["targetGroupName"] = state ? state.targetGroupName : undefined;
            inputs["trackedClusterId"] = state ? state.trackedClusterId : undefined;
            inputs["type"] = state ? state.type : undefined;
        } else {
            const args = argsOrState as ProxyTargetArgs | undefined;
            if (!args || args.dbProxyName === undefined) {
                throw new Error("Missing required property 'dbProxyName'");
            }
            if (!args || args.targetGroupName === undefined) {
                throw new Error("Missing required property 'targetGroupName'");
            }
            inputs["dbClusterIdentifier"] = args ? args.dbClusterIdentifier : undefined;
            inputs["dbInstanceIdentifier"] = args ? args.dbInstanceIdentifier : undefined;
            inputs["dbProxyName"] = args ? args.dbProxyName : undefined;
            inputs["targetGroupName"] = args ? args.targetGroupName : undefined;
            inputs["endpoint"] = undefined /*out*/;
            inputs["port"] = undefined /*out*/;
            inputs["rdsResourceId"] = undefined /*out*/;
            inputs["targetArn"] = undefined /*out*/;
            inputs["trackedClusterId"] = undefined /*out*/;
            inputs["type"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(ProxyTarget.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ProxyTarget resources.
 */
export interface ProxyTargetState {
    /**
     * DB cluster identifier.
     */
    readonly dbClusterIdentifier?: pulumi.Input<string>;
    /**
     * DB instance identifier.
     */
    readonly dbInstanceIdentifier?: pulumi.Input<string>;
    /**
     * The name of the DB proxy.
     */
    readonly dbProxyName?: pulumi.Input<string>;
    /**
     * Hostname for the target RDS DB Instance. Only returned for `RDS_INSTANCE` type.
     */
    readonly endpoint?: pulumi.Input<string>;
    /**
     * Port for the target RDS DB Instance or Aurora DB Cluster.
     */
    readonly port?: pulumi.Input<number>;
    /**
     * Identifier representing the DB Instance or DB Cluster target.
     */
    readonly rdsResourceId?: pulumi.Input<string>;
    /**
     * Amazon Resource Name (ARN) for the DB instance or DB cluster. Currently not returned by the RDS API.
     */
    readonly targetArn?: pulumi.Input<string>;
    /**
     * The name of the target group.
     */
    readonly targetGroupName?: pulumi.Input<string>;
    /**
     * DB Cluster identifier for the DB Instance target. Not returned unless manually importing an `RDS_INSTANCE` target that is part of a DB Cluster.
     */
    readonly trackedClusterId?: pulumi.Input<string>;
    /**
     * Type of target. e.g. `RDS_INSTANCE` or `TRACKED_CLUSTER`
     */
    readonly type?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a ProxyTarget resource.
 */
export interface ProxyTargetArgs {
    /**
     * DB cluster identifier.
     */
    readonly dbClusterIdentifier?: pulumi.Input<string>;
    /**
     * DB instance identifier.
     */
    readonly dbInstanceIdentifier?: pulumi.Input<string>;
    /**
     * The name of the DB proxy.
     */
    readonly dbProxyName: pulumi.Input<string>;
    /**
     * The name of the target group.
     */
    readonly targetGroupName: pulumi.Input<string>;
}

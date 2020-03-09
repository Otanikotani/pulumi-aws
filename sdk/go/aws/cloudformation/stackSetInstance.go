// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package cloudformation

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Manages a CloudFormation StackSet Instance. Instances are managed in the account and region of the StackSet after the target account permissions have been configured. Additional information about StackSets can be found in the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html).
// 
// > **NOTE:** All target accounts must have an IAM Role created that matches the name of the execution role configured in the StackSet (the `executionRoleName` argument in the `cloudformation.StackSet` resource) in a trust relationship with the administrative account or administration IAM Role. The execution role must have appropriate permissions to manage resources defined in the template along with those required for StackSets to operate. See the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs.html) for more details.
// 
// > **NOTE:** To retain the Stack during resource destroy, ensure `retainStack` has been set to `true` in the state first. This must be completed _before_ a deployment that would destroy the resource.
// 
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cloudformation_stack_set_instance.html.markdown.
type StackSetInstance struct {
	pulumi.CustomResourceState

	// Target AWS Account ID to create a Stack based on the StackSet. Defaults to current account.
	AccountId pulumi.StringOutput `pulumi:"accountId"`
	// Key-value map of input parameters to override from the StackSet for this Instance.
	ParameterOverrides pulumi.StringMapOutput `pulumi:"parameterOverrides"`
	// Target AWS Region to create a Stack based on the StackSet. Defaults to current region.
	Region pulumi.StringOutput `pulumi:"region"`
	// During resource destroy, remove Instance from StackSet while keeping the Stack and its associated resources. Must be enabled in the state _before_ destroy operation to take effect. You cannot reassociate a retained Stack or add an existing, saved Stack to a new StackSet. Defaults to `false`.
	RetainStack pulumi.BoolPtrOutput `pulumi:"retainStack"`
	// Stack identifier
	StackId pulumi.StringOutput `pulumi:"stackId"`
	// Name of the StackSet.
	StackSetName pulumi.StringOutput `pulumi:"stackSetName"`
}

// NewStackSetInstance registers a new resource with the given unique name, arguments, and options.
func NewStackSetInstance(ctx *pulumi.Context,
	name string, args *StackSetInstanceArgs, opts ...pulumi.ResourceOption) (*StackSetInstance, error) {
	if args == nil || args.StackSetName == nil {
		return nil, errors.New("missing required argument 'StackSetName'")
	}
	if args == nil {
		args = &StackSetInstanceArgs{}
	}
	var resource StackSetInstance
	err := ctx.RegisterResource("aws:cloudformation/stackSetInstance:StackSetInstance", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetStackSetInstance gets an existing StackSetInstance resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetStackSetInstance(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *StackSetInstanceState, opts ...pulumi.ResourceOption) (*StackSetInstance, error) {
	var resource StackSetInstance
	err := ctx.ReadResource("aws:cloudformation/stackSetInstance:StackSetInstance", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering StackSetInstance resources.
type stackSetInstanceState struct {
	// Target AWS Account ID to create a Stack based on the StackSet. Defaults to current account.
	AccountId *string `pulumi:"accountId"`
	// Key-value map of input parameters to override from the StackSet for this Instance.
	ParameterOverrides map[string]string `pulumi:"parameterOverrides"`
	// Target AWS Region to create a Stack based on the StackSet. Defaults to current region.
	Region *string `pulumi:"region"`
	// During resource destroy, remove Instance from StackSet while keeping the Stack and its associated resources. Must be enabled in the state _before_ destroy operation to take effect. You cannot reassociate a retained Stack or add an existing, saved Stack to a new StackSet. Defaults to `false`.
	RetainStack *bool `pulumi:"retainStack"`
	// Stack identifier
	StackId *string `pulumi:"stackId"`
	// Name of the StackSet.
	StackSetName *string `pulumi:"stackSetName"`
}

type StackSetInstanceState struct {
	// Target AWS Account ID to create a Stack based on the StackSet. Defaults to current account.
	AccountId pulumi.StringPtrInput
	// Key-value map of input parameters to override from the StackSet for this Instance.
	ParameterOverrides pulumi.StringMapInput
	// Target AWS Region to create a Stack based on the StackSet. Defaults to current region.
	Region pulumi.StringPtrInput
	// During resource destroy, remove Instance from StackSet while keeping the Stack and its associated resources. Must be enabled in the state _before_ destroy operation to take effect. You cannot reassociate a retained Stack or add an existing, saved Stack to a new StackSet. Defaults to `false`.
	RetainStack pulumi.BoolPtrInput
	// Stack identifier
	StackId pulumi.StringPtrInput
	// Name of the StackSet.
	StackSetName pulumi.StringPtrInput
}

func (StackSetInstanceState) ElementType() reflect.Type {
	return reflect.TypeOf((*stackSetInstanceState)(nil)).Elem()
}

type stackSetInstanceArgs struct {
	// Target AWS Account ID to create a Stack based on the StackSet. Defaults to current account.
	AccountId *string `pulumi:"accountId"`
	// Key-value map of input parameters to override from the StackSet for this Instance.
	ParameterOverrides map[string]string `pulumi:"parameterOverrides"`
	// Target AWS Region to create a Stack based on the StackSet. Defaults to current region.
	Region *string `pulumi:"region"`
	// During resource destroy, remove Instance from StackSet while keeping the Stack and its associated resources. Must be enabled in the state _before_ destroy operation to take effect. You cannot reassociate a retained Stack or add an existing, saved Stack to a new StackSet. Defaults to `false`.
	RetainStack *bool `pulumi:"retainStack"`
	// Name of the StackSet.
	StackSetName string `pulumi:"stackSetName"`
}

// The set of arguments for constructing a StackSetInstance resource.
type StackSetInstanceArgs struct {
	// Target AWS Account ID to create a Stack based on the StackSet. Defaults to current account.
	AccountId pulumi.StringPtrInput
	// Key-value map of input parameters to override from the StackSet for this Instance.
	ParameterOverrides pulumi.StringMapInput
	// Target AWS Region to create a Stack based on the StackSet. Defaults to current region.
	Region pulumi.StringPtrInput
	// During resource destroy, remove Instance from StackSet while keeping the Stack and its associated resources. Must be enabled in the state _before_ destroy operation to take effect. You cannot reassociate a retained Stack or add an existing, saved Stack to a new StackSet. Defaults to `false`.
	RetainStack pulumi.BoolPtrInput
	// Name of the StackSet.
	StackSetName pulumi.StringInput
}

func (StackSetInstanceArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*stackSetInstanceArgs)(nil)).Elem()
}


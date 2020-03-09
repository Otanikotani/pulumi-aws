// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package cloudformation

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Manages a CloudFormation StackSet. StackSets allow CloudFormation templates to be easily deployed across multiple accounts and regions via StackSet Instances ([`cloudformation.StackSetInstance` resource](https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set_instance.html)). Additional information about StackSets can be found in the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html).
// 
// > **NOTE:** All template parameters, including those with a `Default`, must be configured or ignored with the `lifecycle` configuration block `ignoreChanges` argument.
// 
// > **NOTE:** All `NoEcho` template parameters must be ignored with the `lifecycle` configuration block `ignoreChanges` argument.
// 
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cloudformation_stack_set.html.markdown.
type StackSet struct {
	pulumi.CustomResourceState

	// Amazon Resource Number (ARN) of the IAM Role in the administrator account.
	AdministrationRoleArn pulumi.StringOutput `pulumi:"administrationRoleArn"`
	// Amazon Resource Name (ARN) of the StackSet.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// A list of capabilities. Valid values: `CAPABILITY_IAM`, `CAPABILITY_NAMED_IAM`, `CAPABILITY_AUTO_EXPAND`.
	Capabilities pulumi.StringArrayOutput `pulumi:"capabilities"`
	// Description of the StackSet.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// Name of the IAM Role in all target accounts for StackSet operations. Defaults to `AWSCloudFormationStackSetExecutionRole`.
	ExecutionRoleName pulumi.StringPtrOutput `pulumi:"executionRoleName"`
	// Name of the StackSet. The name must be unique in the region where you create your StackSet. The name can contain only alphanumeric characters (case-sensitive) and hyphens. It must start with an alphabetic character and cannot be longer than 128 characters.
	Name pulumi.StringOutput `pulumi:"name"`
	// Key-value map of input parameters for the StackSet template. All template parameters, including those with a `Default`, must be configured or ignored with `lifecycle` configuration block `ignoreChanges` argument. All `NoEcho` template parameters must be ignored with the `lifecycle` configuration block `ignoreChanges` argument.
	Parameters pulumi.StringMapOutput `pulumi:"parameters"`
	// Unique identifier of the StackSet.
	StackSetId pulumi.StringOutput `pulumi:"stackSetId"`
	// Key-value map of tags to associate with this StackSet and the Stacks created from it. AWS CloudFormation also propagates these tags to supported resources that are created in the Stacks. A maximum number of 50 tags can be specified.
	Tags pulumi.MapOutput `pulumi:"tags"`
	// String containing the CloudFormation template body. Maximum size: 51,200 bytes. Conflicts with `templateUrl`.
	TemplateBody pulumi.StringOutput `pulumi:"templateBody"`
	// String containing the location of a file containing the CloudFormation template body. The URL must point to a template that is located in an Amazon S3 bucket. Maximum location file size: 460,800 bytes. Conflicts with `templateBody`.
	TemplateUrl pulumi.StringPtrOutput `pulumi:"templateUrl"`
}

// NewStackSet registers a new resource with the given unique name, arguments, and options.
func NewStackSet(ctx *pulumi.Context,
	name string, args *StackSetArgs, opts ...pulumi.ResourceOption) (*StackSet, error) {
	if args == nil || args.AdministrationRoleArn == nil {
		return nil, errors.New("missing required argument 'AdministrationRoleArn'")
	}
	if args == nil {
		args = &StackSetArgs{}
	}
	var resource StackSet
	err := ctx.RegisterResource("aws:cloudformation/stackSet:StackSet", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetStackSet gets an existing StackSet resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetStackSet(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *StackSetState, opts ...pulumi.ResourceOption) (*StackSet, error) {
	var resource StackSet
	err := ctx.ReadResource("aws:cloudformation/stackSet:StackSet", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering StackSet resources.
type stackSetState struct {
	// Amazon Resource Number (ARN) of the IAM Role in the administrator account.
	AdministrationRoleArn *string `pulumi:"administrationRoleArn"`
	// Amazon Resource Name (ARN) of the StackSet.
	Arn *string `pulumi:"arn"`
	// A list of capabilities. Valid values: `CAPABILITY_IAM`, `CAPABILITY_NAMED_IAM`, `CAPABILITY_AUTO_EXPAND`.
	Capabilities []string `pulumi:"capabilities"`
	// Description of the StackSet.
	Description *string `pulumi:"description"`
	// Name of the IAM Role in all target accounts for StackSet operations. Defaults to `AWSCloudFormationStackSetExecutionRole`.
	ExecutionRoleName *string `pulumi:"executionRoleName"`
	// Name of the StackSet. The name must be unique in the region where you create your StackSet. The name can contain only alphanumeric characters (case-sensitive) and hyphens. It must start with an alphabetic character and cannot be longer than 128 characters.
	Name *string `pulumi:"name"`
	// Key-value map of input parameters for the StackSet template. All template parameters, including those with a `Default`, must be configured or ignored with `lifecycle` configuration block `ignoreChanges` argument. All `NoEcho` template parameters must be ignored with the `lifecycle` configuration block `ignoreChanges` argument.
	Parameters map[string]string `pulumi:"parameters"`
	// Unique identifier of the StackSet.
	StackSetId *string `pulumi:"stackSetId"`
	// Key-value map of tags to associate with this StackSet and the Stacks created from it. AWS CloudFormation also propagates these tags to supported resources that are created in the Stacks. A maximum number of 50 tags can be specified.
	Tags map[string]interface{} `pulumi:"tags"`
	// String containing the CloudFormation template body. Maximum size: 51,200 bytes. Conflicts with `templateUrl`.
	TemplateBody *string `pulumi:"templateBody"`
	// String containing the location of a file containing the CloudFormation template body. The URL must point to a template that is located in an Amazon S3 bucket. Maximum location file size: 460,800 bytes. Conflicts with `templateBody`.
	TemplateUrl *string `pulumi:"templateUrl"`
}

type StackSetState struct {
	// Amazon Resource Number (ARN) of the IAM Role in the administrator account.
	AdministrationRoleArn pulumi.StringPtrInput
	// Amazon Resource Name (ARN) of the StackSet.
	Arn pulumi.StringPtrInput
	// A list of capabilities. Valid values: `CAPABILITY_IAM`, `CAPABILITY_NAMED_IAM`, `CAPABILITY_AUTO_EXPAND`.
	Capabilities pulumi.StringArrayInput
	// Description of the StackSet.
	Description pulumi.StringPtrInput
	// Name of the IAM Role in all target accounts for StackSet operations. Defaults to `AWSCloudFormationStackSetExecutionRole`.
	ExecutionRoleName pulumi.StringPtrInput
	// Name of the StackSet. The name must be unique in the region where you create your StackSet. The name can contain only alphanumeric characters (case-sensitive) and hyphens. It must start with an alphabetic character and cannot be longer than 128 characters.
	Name pulumi.StringPtrInput
	// Key-value map of input parameters for the StackSet template. All template parameters, including those with a `Default`, must be configured or ignored with `lifecycle` configuration block `ignoreChanges` argument. All `NoEcho` template parameters must be ignored with the `lifecycle` configuration block `ignoreChanges` argument.
	Parameters pulumi.StringMapInput
	// Unique identifier of the StackSet.
	StackSetId pulumi.StringPtrInput
	// Key-value map of tags to associate with this StackSet and the Stacks created from it. AWS CloudFormation also propagates these tags to supported resources that are created in the Stacks. A maximum number of 50 tags can be specified.
	Tags pulumi.MapInput
	// String containing the CloudFormation template body. Maximum size: 51,200 bytes. Conflicts with `templateUrl`.
	TemplateBody pulumi.StringPtrInput
	// String containing the location of a file containing the CloudFormation template body. The URL must point to a template that is located in an Amazon S3 bucket. Maximum location file size: 460,800 bytes. Conflicts with `templateBody`.
	TemplateUrl pulumi.StringPtrInput
}

func (StackSetState) ElementType() reflect.Type {
	return reflect.TypeOf((*stackSetState)(nil)).Elem()
}

type stackSetArgs struct {
	// Amazon Resource Number (ARN) of the IAM Role in the administrator account.
	AdministrationRoleArn string `pulumi:"administrationRoleArn"`
	// A list of capabilities. Valid values: `CAPABILITY_IAM`, `CAPABILITY_NAMED_IAM`, `CAPABILITY_AUTO_EXPAND`.
	Capabilities []string `pulumi:"capabilities"`
	// Description of the StackSet.
	Description *string `pulumi:"description"`
	// Name of the IAM Role in all target accounts for StackSet operations. Defaults to `AWSCloudFormationStackSetExecutionRole`.
	ExecutionRoleName *string `pulumi:"executionRoleName"`
	// Name of the StackSet. The name must be unique in the region where you create your StackSet. The name can contain only alphanumeric characters (case-sensitive) and hyphens. It must start with an alphabetic character and cannot be longer than 128 characters.
	Name *string `pulumi:"name"`
	// Key-value map of input parameters for the StackSet template. All template parameters, including those with a `Default`, must be configured or ignored with `lifecycle` configuration block `ignoreChanges` argument. All `NoEcho` template parameters must be ignored with the `lifecycle` configuration block `ignoreChanges` argument.
	Parameters map[string]string `pulumi:"parameters"`
	// Key-value map of tags to associate with this StackSet and the Stacks created from it. AWS CloudFormation also propagates these tags to supported resources that are created in the Stacks. A maximum number of 50 tags can be specified.
	Tags map[string]interface{} `pulumi:"tags"`
	// String containing the CloudFormation template body. Maximum size: 51,200 bytes. Conflicts with `templateUrl`.
	TemplateBody *string `pulumi:"templateBody"`
	// String containing the location of a file containing the CloudFormation template body. The URL must point to a template that is located in an Amazon S3 bucket. Maximum location file size: 460,800 bytes. Conflicts with `templateBody`.
	TemplateUrl *string `pulumi:"templateUrl"`
}

// The set of arguments for constructing a StackSet resource.
type StackSetArgs struct {
	// Amazon Resource Number (ARN) of the IAM Role in the administrator account.
	AdministrationRoleArn pulumi.StringInput
	// A list of capabilities. Valid values: `CAPABILITY_IAM`, `CAPABILITY_NAMED_IAM`, `CAPABILITY_AUTO_EXPAND`.
	Capabilities pulumi.StringArrayInput
	// Description of the StackSet.
	Description pulumi.StringPtrInput
	// Name of the IAM Role in all target accounts for StackSet operations. Defaults to `AWSCloudFormationStackSetExecutionRole`.
	ExecutionRoleName pulumi.StringPtrInput
	// Name of the StackSet. The name must be unique in the region where you create your StackSet. The name can contain only alphanumeric characters (case-sensitive) and hyphens. It must start with an alphabetic character and cannot be longer than 128 characters.
	Name pulumi.StringPtrInput
	// Key-value map of input parameters for the StackSet template. All template parameters, including those with a `Default`, must be configured or ignored with `lifecycle` configuration block `ignoreChanges` argument. All `NoEcho` template parameters must be ignored with the `lifecycle` configuration block `ignoreChanges` argument.
	Parameters pulumi.StringMapInput
	// Key-value map of tags to associate with this StackSet and the Stacks created from it. AWS CloudFormation also propagates these tags to supported resources that are created in the Stacks. A maximum number of 50 tags can be specified.
	Tags pulumi.MapInput
	// String containing the CloudFormation template body. Maximum size: 51,200 bytes. Conflicts with `templateUrl`.
	TemplateBody pulumi.StringPtrInput
	// String containing the location of a file containing the CloudFormation template body. The URL must point to a template that is located in an Amazon S3 bucket. Maximum location file size: 460,800 bytes. Conflicts with `templateBody`.
	TemplateUrl pulumi.StringPtrInput
}

func (StackSetArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*stackSetArgs)(nil)).Elem()
}


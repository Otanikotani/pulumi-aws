// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package lambda

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Creates a Lambda permission to allow external sources invoking the Lambda function
// (e.g. CloudWatch Event Rule, SNS or S3).
type Permission struct {
	s *pulumi.ResourceState
}

// NewPermission registers a new resource with the given unique name, arguments, and options.
func NewPermission(ctx *pulumi.Context,
	name string, args *PermissionArgs, opts ...pulumi.ResourceOpt) (*Permission, error) {
	if args == nil || args.Action == nil {
		return nil, errors.New("missing required argument 'Action'")
	}
	if args == nil || args.Function == nil {
		return nil, errors.New("missing required argument 'Function'")
	}
	if args == nil || args.Principal == nil {
		return nil, errors.New("missing required argument 'Principal'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["action"] = nil
		inputs["eventSourceToken"] = nil
		inputs["function"] = nil
		inputs["principal"] = nil
		inputs["qualifier"] = nil
		inputs["sourceAccount"] = nil
		inputs["sourceArn"] = nil
		inputs["statementId"] = nil
		inputs["statementIdPrefix"] = nil
	} else {
		inputs["action"] = args.Action
		inputs["eventSourceToken"] = args.EventSourceToken
		inputs["function"] = args.Function
		inputs["principal"] = args.Principal
		inputs["qualifier"] = args.Qualifier
		inputs["sourceAccount"] = args.SourceAccount
		inputs["sourceArn"] = args.SourceArn
		inputs["statementId"] = args.StatementId
		inputs["statementIdPrefix"] = args.StatementIdPrefix
	}
	s, err := ctx.RegisterResource("aws:lambda/permission:Permission", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Permission{s: s}, nil
}

// GetPermission gets an existing Permission resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetPermission(ctx *pulumi.Context,
	name string, id pulumi.ID, state *PermissionState, opts ...pulumi.ResourceOpt) (*Permission, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["action"] = state.Action
		inputs["eventSourceToken"] = state.EventSourceToken
		inputs["function"] = state.Function
		inputs["principal"] = state.Principal
		inputs["qualifier"] = state.Qualifier
		inputs["sourceAccount"] = state.SourceAccount
		inputs["sourceArn"] = state.SourceArn
		inputs["statementId"] = state.StatementId
		inputs["statementIdPrefix"] = state.StatementIdPrefix
	}
	s, err := ctx.ReadResource("aws:lambda/permission:Permission", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Permission{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *Permission) URN() *pulumi.URNOutput {
	return r.s.URN
}

// ID is this resource's unique identifier assigned by its provider.
func (r *Permission) ID() *pulumi.IDOutput {
	return r.s.ID
}

// The AWS Lambda action you want to allow in this statement. (e.g. `lambda:InvokeFunction`)
func (r *Permission) Action() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["action"])
}

// The Event Source Token to validate.  Used with [Alexa Skills][1].
func (r *Permission) EventSourceToken() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["eventSourceToken"])
}

// Name of the Lambda function whose resource policy you are updating
func (r *Permission) Function() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["function"])
}

// The principal who is getting this permission.
// e.g. `s3.amazonaws.com`, an AWS account ID, or any valid AWS service principal
// such as `events.amazonaws.com` or `sns.amazonaws.com`.
func (r *Permission) Principal() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["principal"])
}

// Query parameter to specify function version or alias name.
// The permission will then apply to the specific qualified ARN.
// e.g. `arn:aws:lambda:aws-region:acct-id:function:function-name:2`
func (r *Permission) Qualifier() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["qualifier"])
}

// This parameter is used for S3 and SES. The AWS account ID (without a hyphen) of the source owner.
func (r *Permission) SourceAccount() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["sourceAccount"])
}

// When granting Amazon S3 or CloudWatch Events permission to
// invoke your function, you should specify this field with the Amazon Resource Name (ARN)
// for the S3 Bucket or CloudWatch Events Rule as its value.  This ensures that only events
// generated from the specified bucket or rule can invoke the function.
// API Gateway ARNs have a unique structure described
// [here](http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-control-access-using-iam-policies-to-invoke-api.html).
func (r *Permission) SourceArn() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["sourceArn"])
}

// A unique statement identifier. By default generated by Terraform.
func (r *Permission) StatementId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["statementId"])
}

// A statement identifier prefix. Terraform will generate a unique suffix. Conflicts with `statement_id`.
func (r *Permission) StatementIdPrefix() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["statementIdPrefix"])
}

// Input properties used for looking up and filtering Permission resources.
type PermissionState struct {
	// The AWS Lambda action you want to allow in this statement. (e.g. `lambda:InvokeFunction`)
	Action interface{}
	// The Event Source Token to validate.  Used with [Alexa Skills][1].
	EventSourceToken interface{}
	// Name of the Lambda function whose resource policy you are updating
	Function interface{}
	// The principal who is getting this permission.
	// e.g. `s3.amazonaws.com`, an AWS account ID, or any valid AWS service principal
	// such as `events.amazonaws.com` or `sns.amazonaws.com`.
	Principal interface{}
	// Query parameter to specify function version or alias name.
	// The permission will then apply to the specific qualified ARN.
	// e.g. `arn:aws:lambda:aws-region:acct-id:function:function-name:2`
	Qualifier interface{}
	// This parameter is used for S3 and SES. The AWS account ID (without a hyphen) of the source owner.
	SourceAccount interface{}
	// When granting Amazon S3 or CloudWatch Events permission to
	// invoke your function, you should specify this field with the Amazon Resource Name (ARN)
	// for the S3 Bucket or CloudWatch Events Rule as its value.  This ensures that only events
	// generated from the specified bucket or rule can invoke the function.
	// API Gateway ARNs have a unique structure described
	// [here](http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-control-access-using-iam-policies-to-invoke-api.html).
	SourceArn interface{}
	// A unique statement identifier. By default generated by Terraform.
	StatementId interface{}
	// A statement identifier prefix. Terraform will generate a unique suffix. Conflicts with `statement_id`.
	StatementIdPrefix interface{}
}

// The set of arguments for constructing a Permission resource.
type PermissionArgs struct {
	// The AWS Lambda action you want to allow in this statement. (e.g. `lambda:InvokeFunction`)
	Action interface{}
	// The Event Source Token to validate.  Used with [Alexa Skills][1].
	EventSourceToken interface{}
	// Name of the Lambda function whose resource policy you are updating
	Function interface{}
	// The principal who is getting this permission.
	// e.g. `s3.amazonaws.com`, an AWS account ID, or any valid AWS service principal
	// such as `events.amazonaws.com` or `sns.amazonaws.com`.
	Principal interface{}
	// Query parameter to specify function version or alias name.
	// The permission will then apply to the specific qualified ARN.
	// e.g. `arn:aws:lambda:aws-region:acct-id:function:function-name:2`
	Qualifier interface{}
	// This parameter is used for S3 and SES. The AWS account ID (without a hyphen) of the source owner.
	SourceAccount interface{}
	// When granting Amazon S3 or CloudWatch Events permission to
	// invoke your function, you should specify this field with the Amazon Resource Name (ARN)
	// for the S3 Bucket or CloudWatch Events Rule as its value.  This ensures that only events
	// generated from the specified bucket or rule can invoke the function.
	// API Gateway ARNs have a unique structure described
	// [here](http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-control-access-using-iam-policies-to-invoke-api.html).
	SourceArn interface{}
	// A unique statement identifier. By default generated by Terraform.
	StatementId interface{}
	// A statement identifier prefix. Terraform will generate a unique suffix. Conflicts with `statement_id`.
	StatementIdPrefix interface{}
}

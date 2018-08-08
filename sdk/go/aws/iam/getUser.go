// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package iam

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// This data source can be used to fetch information about a specific
// IAM user. By using this data source, you can reference IAM user
// properties without having to hard code ARNs or unique IDs as input.
func LookupUser(ctx *pulumi.Context, args *GetUserArgs) (*GetUserResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["userName"] = args.UserName
	}
	outputs, err := ctx.Invoke("aws:iam/getUser:getUser", inputs)
	if err != nil {
		return nil, err
	}
	return &GetUserResult{
		Arn: outputs["arn"],
		Path: outputs["path"],
		PermissionsBoundary: outputs["permissionsBoundary"],
		UserId: outputs["userId"],
		Id: outputs["id"],
	}, nil
}

// A collection of arguments for invoking getUser.
type GetUserArgs struct {
	// The friendly IAM user name to match.
	UserName interface{}
}

// A collection of values returned by getUser.
type GetUserResult struct {
	// The Amazon Resource Name (ARN) assigned by AWS for this user.
	Arn interface{}
	// Path in which this user was created.
	Path interface{}
	// The ARN of the policy that is used to set the permissions boundary for the user.
	PermissionsBoundary interface{}
	// The unique ID assigned by AWS for this user.
	UserId interface{}
	// id is the provider-assigned unique ID for this managed resource.
	Id interface{}
}

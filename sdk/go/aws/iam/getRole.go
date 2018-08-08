// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package iam

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// This data source can be used to fetch information about a specific
// IAM role. By using this data source, you can reference IAM role
// properties without having to hard code ARNs as input.
func LookupRole(ctx *pulumi.Context, args *GetRoleArgs) (*GetRoleResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["name"] = args.Name
		inputs["roleName"] = args.RoleName
	}
	outputs, err := ctx.Invoke("aws:iam/getRole:getRole", inputs)
	if err != nil {
		return nil, err
	}
	return &GetRoleResult{
		Arn: outputs["arn"],
		AssumeRolePolicy: outputs["assumeRolePolicy"],
		AssumeRolePolicyDocument: outputs["assumeRolePolicyDocument"],
		CreateDate: outputs["createDate"],
		Description: outputs["description"],
		MaxSessionDuration: outputs["maxSessionDuration"],
		Path: outputs["path"],
		PermissionsBoundary: outputs["permissionsBoundary"],
		RoleId: outputs["roleId"],
		UniqueId: outputs["uniqueId"],
		Id: outputs["id"],
	}, nil
}

// A collection of arguments for invoking getRole.
type GetRoleArgs struct {
	// The friendly IAM role name to match.
	Name interface{}
	RoleName interface{}
}

// A collection of values returned by getRole.
type GetRoleResult struct {
	// The Amazon Resource Name (ARN) specifying the role.
	Arn interface{}
	// The policy document associated with the role.
	AssumeRolePolicy interface{}
	AssumeRolePolicyDocument interface{}
	CreateDate interface{}
	Description interface{}
	MaxSessionDuration interface{}
	// The path to the role.
	Path interface{}
	// The ARN of the policy that is used to set the permissions boundary for the role.
	PermissionsBoundary interface{}
	RoleId interface{}
	// The stable and unique string identifying the role.
	UniqueId interface{}
	// id is the provider-assigned unique ID for this managed resource.
	Id interface{}
}

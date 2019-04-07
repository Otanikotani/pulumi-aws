// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package apigateway

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Use this data source to get the id of a VPC Link in
// API Gateway. To fetch the VPC Link you must provide a name to match against. 
// As there is no unique name constraint on API Gateway VPC Links this data source will 
// error if there is more than one match.
func LookupVpcLink(ctx *pulumi.Context, args *GetVpcLinkArgs) (*GetVpcLinkResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["name"] = args.Name
	}
	outputs, err := ctx.Invoke("aws:apigateway/getVpcLink:getVpcLink", inputs)
	if err != nil {
		return nil, err
	}
	return &GetVpcLinkResult{
		Id: outputs["id"],
		Name: outputs["name"],
	}, nil
}

// A collection of arguments for invoking getVpcLink.
type GetVpcLinkArgs struct {
	// The name of the API Gateway VPC Link to look up. If no API Gateway VPC Link is found with this name, an error will be returned. 
	// If multiple API Gateway VPC Links are found with this name, an error will be returned.
	Name interface{}
}

// A collection of values returned by getVpcLink.
type GetVpcLinkResult struct {
	// Set to the ID of the found API Gateway VPC Link.
	Id interface{}
	Name interface{}
}

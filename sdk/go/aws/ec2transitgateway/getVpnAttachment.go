// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ec2transitgateway

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Get information on an EC2 Transit Gateway VPN Attachment.
func LookupVpnAttachment(ctx *pulumi.Context, args *GetVpnAttachmentArgs) (*GetVpnAttachmentResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["tags"] = args.Tags
		inputs["transitGatewayId"] = args.TransitGatewayId
		inputs["vpnConnectionId"] = args.VpnConnectionId
	}
	outputs, err := ctx.Invoke("aws:ec2transitgateway/getVpnAttachment:getVpnAttachment", inputs)
	if err != nil {
		return nil, err
	}
	return &GetVpnAttachmentResult{
		Tags: outputs["tags"],
		TransitGatewayId: outputs["transitGatewayId"],
		VpnConnectionId: outputs["vpnConnectionId"],
		Id: outputs["id"],
	}, nil
}

// A collection of arguments for invoking getVpnAttachment.
type GetVpnAttachmentArgs struct {
	Tags interface{}
	// Identifier of the EC2 Transit Gateway.
	TransitGatewayId interface{}
	// Identifier of the EC2 VPN Connection.
	VpnConnectionId interface{}
}

// A collection of values returned by getVpnAttachment.
type GetVpnAttachmentResult struct {
	// Key-value tags for the EC2 Transit Gateway VPN Attachment
	Tags interface{}
	TransitGatewayId interface{}
	VpnConnectionId interface{}
	// id is the provider-assigned unique ID for this managed resource.
	Id interface{}
}

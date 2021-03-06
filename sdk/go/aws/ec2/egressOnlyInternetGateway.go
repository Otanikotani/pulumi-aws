// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ec2

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// [IPv6 only] Creates an egress-only Internet gateway for your VPC.
// An egress-only Internet gateway is used to enable outbound communication
// over IPv6 from instances in your VPC to the Internet, and prevents hosts
// outside of your VPC from initiating an IPv6 connection with your instance.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/ec2"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		exampleVpc, err := ec2.NewVpc(ctx, "exampleVpc", &ec2.VpcArgs{
// 			CidrBlock:                    pulumi.String("10.1.0.0/16"),
// 			AssignGeneratedIpv6CidrBlock: pulumi.Bool(true),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = ec2.NewEgressOnlyInternetGateway(ctx, "exampleEgressOnlyInternetGateway", &ec2.EgressOnlyInternetGatewayArgs{
// 			VpcId: exampleVpc.ID(),
// 			Tags: pulumi.StringMap{
// 				"Name": pulumi.String("main"),
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type EgressOnlyInternetGateway struct {
	pulumi.CustomResourceState

	// A map of tags to assign to the resource.
	Tags pulumi.StringMapOutput `pulumi:"tags"`
	// The VPC ID to create in.
	VpcId pulumi.StringOutput `pulumi:"vpcId"`
}

// NewEgressOnlyInternetGateway registers a new resource with the given unique name, arguments, and options.
func NewEgressOnlyInternetGateway(ctx *pulumi.Context,
	name string, args *EgressOnlyInternetGatewayArgs, opts ...pulumi.ResourceOption) (*EgressOnlyInternetGateway, error) {
	if args == nil || args.VpcId == nil {
		return nil, errors.New("missing required argument 'VpcId'")
	}
	if args == nil {
		args = &EgressOnlyInternetGatewayArgs{}
	}
	var resource EgressOnlyInternetGateway
	err := ctx.RegisterResource("aws:ec2/egressOnlyInternetGateway:EgressOnlyInternetGateway", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetEgressOnlyInternetGateway gets an existing EgressOnlyInternetGateway resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetEgressOnlyInternetGateway(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *EgressOnlyInternetGatewayState, opts ...pulumi.ResourceOption) (*EgressOnlyInternetGateway, error) {
	var resource EgressOnlyInternetGateway
	err := ctx.ReadResource("aws:ec2/egressOnlyInternetGateway:EgressOnlyInternetGateway", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering EgressOnlyInternetGateway resources.
type egressOnlyInternetGatewayState struct {
	// A map of tags to assign to the resource.
	Tags map[string]string `pulumi:"tags"`
	// The VPC ID to create in.
	VpcId *string `pulumi:"vpcId"`
}

type EgressOnlyInternetGatewayState struct {
	// A map of tags to assign to the resource.
	Tags pulumi.StringMapInput
	// The VPC ID to create in.
	VpcId pulumi.StringPtrInput
}

func (EgressOnlyInternetGatewayState) ElementType() reflect.Type {
	return reflect.TypeOf((*egressOnlyInternetGatewayState)(nil)).Elem()
}

type egressOnlyInternetGatewayArgs struct {
	// A map of tags to assign to the resource.
	Tags map[string]string `pulumi:"tags"`
	// The VPC ID to create in.
	VpcId string `pulumi:"vpcId"`
}

// The set of arguments for constructing a EgressOnlyInternetGateway resource.
type EgressOnlyInternetGatewayArgs struct {
	// A map of tags to assign to the resource.
	Tags pulumi.StringMapInput
	// The VPC ID to create in.
	VpcId pulumi.StringInput
}

func (EgressOnlyInternetGatewayArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*egressOnlyInternetGatewayArgs)(nil)).Elem()
}

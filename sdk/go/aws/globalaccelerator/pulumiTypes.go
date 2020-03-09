// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package globalaccelerator

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

type AcceleratorAttributes struct {
	// Indicates whether flow logs are enabled.
	FlowLogsEnabled *bool `pulumi:"flowLogsEnabled"`
	// The name of the Amazon S3 bucket for the flow logs.
	FlowLogsS3Bucket *string `pulumi:"flowLogsS3Bucket"`
	// The prefix for the location in the Amazon S3 bucket for the flow logs.
	FlowLogsS3Prefix *string `pulumi:"flowLogsS3Prefix"`
}

type AcceleratorAttributesInput interface {
	pulumi.Input

	ToAcceleratorAttributesOutput() AcceleratorAttributesOutput
	ToAcceleratorAttributesOutputWithContext(context.Context) AcceleratorAttributesOutput
}

type AcceleratorAttributesArgs struct {
	// Indicates whether flow logs are enabled.
	FlowLogsEnabled pulumi.BoolPtrInput `pulumi:"flowLogsEnabled"`
	// The name of the Amazon S3 bucket for the flow logs.
	FlowLogsS3Bucket pulumi.StringPtrInput `pulumi:"flowLogsS3Bucket"`
	// The prefix for the location in the Amazon S3 bucket for the flow logs.
	FlowLogsS3Prefix pulumi.StringPtrInput `pulumi:"flowLogsS3Prefix"`
}

func (AcceleratorAttributesArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*AcceleratorAttributes)(nil)).Elem()
}

func (i AcceleratorAttributesArgs) ToAcceleratorAttributesOutput() AcceleratorAttributesOutput {
	return i.ToAcceleratorAttributesOutputWithContext(context.Background())
}

func (i AcceleratorAttributesArgs) ToAcceleratorAttributesOutputWithContext(ctx context.Context) AcceleratorAttributesOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AcceleratorAttributesOutput)
}

func (i AcceleratorAttributesArgs) ToAcceleratorAttributesPtrOutput() AcceleratorAttributesPtrOutput {
	return i.ToAcceleratorAttributesPtrOutputWithContext(context.Background())
}

func (i AcceleratorAttributesArgs) ToAcceleratorAttributesPtrOutputWithContext(ctx context.Context) AcceleratorAttributesPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AcceleratorAttributesOutput).ToAcceleratorAttributesPtrOutputWithContext(ctx)
}

type AcceleratorAttributesPtrInput interface {
	pulumi.Input

	ToAcceleratorAttributesPtrOutput() AcceleratorAttributesPtrOutput
	ToAcceleratorAttributesPtrOutputWithContext(context.Context) AcceleratorAttributesPtrOutput
}

type acceleratorAttributesPtrType AcceleratorAttributesArgs

func AcceleratorAttributesPtr(v *AcceleratorAttributesArgs) AcceleratorAttributesPtrInput {	return (*acceleratorAttributesPtrType)(v)
}

func (*acceleratorAttributesPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**AcceleratorAttributes)(nil)).Elem()
}

func (i *acceleratorAttributesPtrType) ToAcceleratorAttributesPtrOutput() AcceleratorAttributesPtrOutput {
	return i.ToAcceleratorAttributesPtrOutputWithContext(context.Background())
}

func (i *acceleratorAttributesPtrType) ToAcceleratorAttributesPtrOutputWithContext(ctx context.Context) AcceleratorAttributesPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AcceleratorAttributesPtrOutput)
}

type AcceleratorAttributesOutput struct { *pulumi.OutputState }

func (AcceleratorAttributesOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*AcceleratorAttributes)(nil)).Elem()
}

func (o AcceleratorAttributesOutput) ToAcceleratorAttributesOutput() AcceleratorAttributesOutput {
	return o
}

func (o AcceleratorAttributesOutput) ToAcceleratorAttributesOutputWithContext(ctx context.Context) AcceleratorAttributesOutput {
	return o
}

func (o AcceleratorAttributesOutput) ToAcceleratorAttributesPtrOutput() AcceleratorAttributesPtrOutput {
	return o.ToAcceleratorAttributesPtrOutputWithContext(context.Background())
}

func (o AcceleratorAttributesOutput) ToAcceleratorAttributesPtrOutputWithContext(ctx context.Context) AcceleratorAttributesPtrOutput {
	return o.ApplyT(func(v AcceleratorAttributes) *AcceleratorAttributes {
		return &v
	}).(AcceleratorAttributesPtrOutput)
}
// Indicates whether flow logs are enabled.
func (o AcceleratorAttributesOutput) FlowLogsEnabled() pulumi.BoolPtrOutput {
	return o.ApplyT(func (v AcceleratorAttributes) *bool { return v.FlowLogsEnabled }).(pulumi.BoolPtrOutput)
}

// The name of the Amazon S3 bucket for the flow logs.
func (o AcceleratorAttributesOutput) FlowLogsS3Bucket() pulumi.StringPtrOutput {
	return o.ApplyT(func (v AcceleratorAttributes) *string { return v.FlowLogsS3Bucket }).(pulumi.StringPtrOutput)
}

// The prefix for the location in the Amazon S3 bucket for the flow logs.
func (o AcceleratorAttributesOutput) FlowLogsS3Prefix() pulumi.StringPtrOutput {
	return o.ApplyT(func (v AcceleratorAttributes) *string { return v.FlowLogsS3Prefix }).(pulumi.StringPtrOutput)
}

type AcceleratorAttributesPtrOutput struct { *pulumi.OutputState}

func (AcceleratorAttributesPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**AcceleratorAttributes)(nil)).Elem()
}

func (o AcceleratorAttributesPtrOutput) ToAcceleratorAttributesPtrOutput() AcceleratorAttributesPtrOutput {
	return o
}

func (o AcceleratorAttributesPtrOutput) ToAcceleratorAttributesPtrOutputWithContext(ctx context.Context) AcceleratorAttributesPtrOutput {
	return o
}

func (o AcceleratorAttributesPtrOutput) Elem() AcceleratorAttributesOutput {
	return o.ApplyT(func (v *AcceleratorAttributes) AcceleratorAttributes { return *v }).(AcceleratorAttributesOutput)
}

// Indicates whether flow logs are enabled.
func (o AcceleratorAttributesPtrOutput) FlowLogsEnabled() pulumi.BoolPtrOutput {
	return o.ApplyT(func (v AcceleratorAttributes) *bool { return v.FlowLogsEnabled }).(pulumi.BoolPtrOutput)
}

// The name of the Amazon S3 bucket for the flow logs.
func (o AcceleratorAttributesPtrOutput) FlowLogsS3Bucket() pulumi.StringPtrOutput {
	return o.ApplyT(func (v AcceleratorAttributes) *string { return v.FlowLogsS3Bucket }).(pulumi.StringPtrOutput)
}

// The prefix for the location in the Amazon S3 bucket for the flow logs.
func (o AcceleratorAttributesPtrOutput) FlowLogsS3Prefix() pulumi.StringPtrOutput {
	return o.ApplyT(func (v AcceleratorAttributes) *string { return v.FlowLogsS3Prefix }).(pulumi.StringPtrOutput)
}

type AcceleratorIpSet struct {
	// A list of IP addresses in the IP address set.
	IpAddresses []string `pulumi:"ipAddresses"`
	// The types of IP addresses included in this IP set.
	IpFamily *string `pulumi:"ipFamily"`
}

type AcceleratorIpSetInput interface {
	pulumi.Input

	ToAcceleratorIpSetOutput() AcceleratorIpSetOutput
	ToAcceleratorIpSetOutputWithContext(context.Context) AcceleratorIpSetOutput
}

type AcceleratorIpSetArgs struct {
	// A list of IP addresses in the IP address set.
	IpAddresses pulumi.StringArrayInput `pulumi:"ipAddresses"`
	// The types of IP addresses included in this IP set.
	IpFamily pulumi.StringPtrInput `pulumi:"ipFamily"`
}

func (AcceleratorIpSetArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*AcceleratorIpSet)(nil)).Elem()
}

func (i AcceleratorIpSetArgs) ToAcceleratorIpSetOutput() AcceleratorIpSetOutput {
	return i.ToAcceleratorIpSetOutputWithContext(context.Background())
}

func (i AcceleratorIpSetArgs) ToAcceleratorIpSetOutputWithContext(ctx context.Context) AcceleratorIpSetOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AcceleratorIpSetOutput)
}

type AcceleratorIpSetArrayInput interface {
	pulumi.Input

	ToAcceleratorIpSetArrayOutput() AcceleratorIpSetArrayOutput
	ToAcceleratorIpSetArrayOutputWithContext(context.Context) AcceleratorIpSetArrayOutput
}

type AcceleratorIpSetArray []AcceleratorIpSetInput

func (AcceleratorIpSetArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]AcceleratorIpSet)(nil)).Elem()
}

func (i AcceleratorIpSetArray) ToAcceleratorIpSetArrayOutput() AcceleratorIpSetArrayOutput {
	return i.ToAcceleratorIpSetArrayOutputWithContext(context.Background())
}

func (i AcceleratorIpSetArray) ToAcceleratorIpSetArrayOutputWithContext(ctx context.Context) AcceleratorIpSetArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AcceleratorIpSetArrayOutput)
}

type AcceleratorIpSetOutput struct { *pulumi.OutputState }

func (AcceleratorIpSetOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*AcceleratorIpSet)(nil)).Elem()
}

func (o AcceleratorIpSetOutput) ToAcceleratorIpSetOutput() AcceleratorIpSetOutput {
	return o
}

func (o AcceleratorIpSetOutput) ToAcceleratorIpSetOutputWithContext(ctx context.Context) AcceleratorIpSetOutput {
	return o
}

// A list of IP addresses in the IP address set.
func (o AcceleratorIpSetOutput) IpAddresses() pulumi.StringArrayOutput {
	return o.ApplyT(func (v AcceleratorIpSet) []string { return v.IpAddresses }).(pulumi.StringArrayOutput)
}

// The types of IP addresses included in this IP set.
func (o AcceleratorIpSetOutput) IpFamily() pulumi.StringPtrOutput {
	return o.ApplyT(func (v AcceleratorIpSet) *string { return v.IpFamily }).(pulumi.StringPtrOutput)
}

type AcceleratorIpSetArrayOutput struct { *pulumi.OutputState}

func (AcceleratorIpSetArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]AcceleratorIpSet)(nil)).Elem()
}

func (o AcceleratorIpSetArrayOutput) ToAcceleratorIpSetArrayOutput() AcceleratorIpSetArrayOutput {
	return o
}

func (o AcceleratorIpSetArrayOutput) ToAcceleratorIpSetArrayOutputWithContext(ctx context.Context) AcceleratorIpSetArrayOutput {
	return o
}

func (o AcceleratorIpSetArrayOutput) Index(i pulumi.IntInput) AcceleratorIpSetOutput {
	return pulumi.All(o, i).ApplyT(func (vs []interface{}) AcceleratorIpSet {
		return vs[0].([]AcceleratorIpSet)[vs[1].(int)]
	}).(AcceleratorIpSetOutput)
}

type EndpointGroupEndpointConfiguration struct {
	// An ID for the endpoint. If the endpoint is a Network Load Balancer or Application Load Balancer, this is the Amazon Resource Name (ARN) of the resource. If the endpoint is an Elastic IP address, this is the Elastic IP address allocation ID.
	EndpointId *string `pulumi:"endpointId"`
	// The weight associated with the endpoint. When you add weights to endpoints, you configure AWS Global Accelerator to route traffic based on proportions that you specify. 
	Weight *int `pulumi:"weight"`
}

type EndpointGroupEndpointConfigurationInput interface {
	pulumi.Input

	ToEndpointGroupEndpointConfigurationOutput() EndpointGroupEndpointConfigurationOutput
	ToEndpointGroupEndpointConfigurationOutputWithContext(context.Context) EndpointGroupEndpointConfigurationOutput
}

type EndpointGroupEndpointConfigurationArgs struct {
	// An ID for the endpoint. If the endpoint is a Network Load Balancer or Application Load Balancer, this is the Amazon Resource Name (ARN) of the resource. If the endpoint is an Elastic IP address, this is the Elastic IP address allocation ID.
	EndpointId pulumi.StringPtrInput `pulumi:"endpointId"`
	// The weight associated with the endpoint. When you add weights to endpoints, you configure AWS Global Accelerator to route traffic based on proportions that you specify. 
	Weight pulumi.IntPtrInput `pulumi:"weight"`
}

func (EndpointGroupEndpointConfigurationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*EndpointGroupEndpointConfiguration)(nil)).Elem()
}

func (i EndpointGroupEndpointConfigurationArgs) ToEndpointGroupEndpointConfigurationOutput() EndpointGroupEndpointConfigurationOutput {
	return i.ToEndpointGroupEndpointConfigurationOutputWithContext(context.Background())
}

func (i EndpointGroupEndpointConfigurationArgs) ToEndpointGroupEndpointConfigurationOutputWithContext(ctx context.Context) EndpointGroupEndpointConfigurationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EndpointGroupEndpointConfigurationOutput)
}

type EndpointGroupEndpointConfigurationArrayInput interface {
	pulumi.Input

	ToEndpointGroupEndpointConfigurationArrayOutput() EndpointGroupEndpointConfigurationArrayOutput
	ToEndpointGroupEndpointConfigurationArrayOutputWithContext(context.Context) EndpointGroupEndpointConfigurationArrayOutput
}

type EndpointGroupEndpointConfigurationArray []EndpointGroupEndpointConfigurationInput

func (EndpointGroupEndpointConfigurationArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]EndpointGroupEndpointConfiguration)(nil)).Elem()
}

func (i EndpointGroupEndpointConfigurationArray) ToEndpointGroupEndpointConfigurationArrayOutput() EndpointGroupEndpointConfigurationArrayOutput {
	return i.ToEndpointGroupEndpointConfigurationArrayOutputWithContext(context.Background())
}

func (i EndpointGroupEndpointConfigurationArray) ToEndpointGroupEndpointConfigurationArrayOutputWithContext(ctx context.Context) EndpointGroupEndpointConfigurationArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EndpointGroupEndpointConfigurationArrayOutput)
}

type EndpointGroupEndpointConfigurationOutput struct { *pulumi.OutputState }

func (EndpointGroupEndpointConfigurationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*EndpointGroupEndpointConfiguration)(nil)).Elem()
}

func (o EndpointGroupEndpointConfigurationOutput) ToEndpointGroupEndpointConfigurationOutput() EndpointGroupEndpointConfigurationOutput {
	return o
}

func (o EndpointGroupEndpointConfigurationOutput) ToEndpointGroupEndpointConfigurationOutputWithContext(ctx context.Context) EndpointGroupEndpointConfigurationOutput {
	return o
}

// An ID for the endpoint. If the endpoint is a Network Load Balancer or Application Load Balancer, this is the Amazon Resource Name (ARN) of the resource. If the endpoint is an Elastic IP address, this is the Elastic IP address allocation ID.
func (o EndpointGroupEndpointConfigurationOutput) EndpointId() pulumi.StringPtrOutput {
	return o.ApplyT(func (v EndpointGroupEndpointConfiguration) *string { return v.EndpointId }).(pulumi.StringPtrOutput)
}

// The weight associated with the endpoint. When you add weights to endpoints, you configure AWS Global Accelerator to route traffic based on proportions that you specify. 
func (o EndpointGroupEndpointConfigurationOutput) Weight() pulumi.IntPtrOutput {
	return o.ApplyT(func (v EndpointGroupEndpointConfiguration) *int { return v.Weight }).(pulumi.IntPtrOutput)
}

type EndpointGroupEndpointConfigurationArrayOutput struct { *pulumi.OutputState}

func (EndpointGroupEndpointConfigurationArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]EndpointGroupEndpointConfiguration)(nil)).Elem()
}

func (o EndpointGroupEndpointConfigurationArrayOutput) ToEndpointGroupEndpointConfigurationArrayOutput() EndpointGroupEndpointConfigurationArrayOutput {
	return o
}

func (o EndpointGroupEndpointConfigurationArrayOutput) ToEndpointGroupEndpointConfigurationArrayOutputWithContext(ctx context.Context) EndpointGroupEndpointConfigurationArrayOutput {
	return o
}

func (o EndpointGroupEndpointConfigurationArrayOutput) Index(i pulumi.IntInput) EndpointGroupEndpointConfigurationOutput {
	return pulumi.All(o, i).ApplyT(func (vs []interface{}) EndpointGroupEndpointConfiguration {
		return vs[0].([]EndpointGroupEndpointConfiguration)[vs[1].(int)]
	}).(EndpointGroupEndpointConfigurationOutput)
}

type ListenerPortRange struct {
	// The first port in the range of ports, inclusive.
	FromPort *int `pulumi:"fromPort"`
	// The last port in the range of ports, inclusive.
	ToPort *int `pulumi:"toPort"`
}

type ListenerPortRangeInput interface {
	pulumi.Input

	ToListenerPortRangeOutput() ListenerPortRangeOutput
	ToListenerPortRangeOutputWithContext(context.Context) ListenerPortRangeOutput
}

type ListenerPortRangeArgs struct {
	// The first port in the range of ports, inclusive.
	FromPort pulumi.IntPtrInput `pulumi:"fromPort"`
	// The last port in the range of ports, inclusive.
	ToPort pulumi.IntPtrInput `pulumi:"toPort"`
}

func (ListenerPortRangeArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ListenerPortRange)(nil)).Elem()
}

func (i ListenerPortRangeArgs) ToListenerPortRangeOutput() ListenerPortRangeOutput {
	return i.ToListenerPortRangeOutputWithContext(context.Background())
}

func (i ListenerPortRangeArgs) ToListenerPortRangeOutputWithContext(ctx context.Context) ListenerPortRangeOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ListenerPortRangeOutput)
}

type ListenerPortRangeArrayInput interface {
	pulumi.Input

	ToListenerPortRangeArrayOutput() ListenerPortRangeArrayOutput
	ToListenerPortRangeArrayOutputWithContext(context.Context) ListenerPortRangeArrayOutput
}

type ListenerPortRangeArray []ListenerPortRangeInput

func (ListenerPortRangeArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]ListenerPortRange)(nil)).Elem()
}

func (i ListenerPortRangeArray) ToListenerPortRangeArrayOutput() ListenerPortRangeArrayOutput {
	return i.ToListenerPortRangeArrayOutputWithContext(context.Background())
}

func (i ListenerPortRangeArray) ToListenerPortRangeArrayOutputWithContext(ctx context.Context) ListenerPortRangeArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ListenerPortRangeArrayOutput)
}

type ListenerPortRangeOutput struct { *pulumi.OutputState }

func (ListenerPortRangeOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ListenerPortRange)(nil)).Elem()
}

func (o ListenerPortRangeOutput) ToListenerPortRangeOutput() ListenerPortRangeOutput {
	return o
}

func (o ListenerPortRangeOutput) ToListenerPortRangeOutputWithContext(ctx context.Context) ListenerPortRangeOutput {
	return o
}

// The first port in the range of ports, inclusive.
func (o ListenerPortRangeOutput) FromPort() pulumi.IntPtrOutput {
	return o.ApplyT(func (v ListenerPortRange) *int { return v.FromPort }).(pulumi.IntPtrOutput)
}

// The last port in the range of ports, inclusive.
func (o ListenerPortRangeOutput) ToPort() pulumi.IntPtrOutput {
	return o.ApplyT(func (v ListenerPortRange) *int { return v.ToPort }).(pulumi.IntPtrOutput)
}

type ListenerPortRangeArrayOutput struct { *pulumi.OutputState}

func (ListenerPortRangeArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]ListenerPortRange)(nil)).Elem()
}

func (o ListenerPortRangeArrayOutput) ToListenerPortRangeArrayOutput() ListenerPortRangeArrayOutput {
	return o
}

func (o ListenerPortRangeArrayOutput) ToListenerPortRangeArrayOutputWithContext(ctx context.Context) ListenerPortRangeArrayOutput {
	return o
}

func (o ListenerPortRangeArrayOutput) Index(i pulumi.IntInput) ListenerPortRangeOutput {
	return pulumi.All(o, i).ApplyT(func (vs []interface{}) ListenerPortRange {
		return vs[0].([]ListenerPortRange)[vs[1].(int)]
	}).(ListenerPortRangeOutput)
}

func init() {
	pulumi.RegisterOutputType(AcceleratorAttributesOutput{})
	pulumi.RegisterOutputType(AcceleratorAttributesPtrOutput{})
	pulumi.RegisterOutputType(AcceleratorIpSetOutput{})
	pulumi.RegisterOutputType(AcceleratorIpSetArrayOutput{})
	pulumi.RegisterOutputType(EndpointGroupEndpointConfigurationOutput{})
	pulumi.RegisterOutputType(EndpointGroupEndpointConfigurationArrayOutput{})
	pulumi.RegisterOutputType(ListenerPortRangeOutput{})
	pulumi.RegisterOutputType(ListenerPortRangeArrayOutput{})
}

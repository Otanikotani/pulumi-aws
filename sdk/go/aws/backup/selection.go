// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package backup

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Manages selection conditions for AWS Backup plan resources.
type Selection struct {
	s *pulumi.ResourceState
}

// NewSelection registers a new resource with the given unique name, arguments, and options.
func NewSelection(ctx *pulumi.Context,
	name string, args *SelectionArgs, opts ...pulumi.ResourceOpt) (*Selection, error) {
	if args == nil || args.IamRoleArn == nil {
		return nil, errors.New("missing required argument 'IamRoleArn'")
	}
	if args == nil || args.PlanId == nil {
		return nil, errors.New("missing required argument 'PlanId'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["iamRoleArn"] = nil
		inputs["name"] = nil
		inputs["planId"] = nil
		inputs["resources"] = nil
		inputs["selectionTags"] = nil
	} else {
		inputs["iamRoleArn"] = args.IamRoleArn
		inputs["name"] = args.Name
		inputs["planId"] = args.PlanId
		inputs["resources"] = args.Resources
		inputs["selectionTags"] = args.SelectionTags
	}
	s, err := ctx.RegisterResource("aws:backup/selection:Selection", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Selection{s: s}, nil
}

// GetSelection gets an existing Selection resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSelection(ctx *pulumi.Context,
	name string, id pulumi.ID, state *SelectionState, opts ...pulumi.ResourceOpt) (*Selection, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["iamRoleArn"] = state.IamRoleArn
		inputs["name"] = state.Name
		inputs["planId"] = state.PlanId
		inputs["resources"] = state.Resources
		inputs["selectionTags"] = state.SelectionTags
	}
	s, err := ctx.ReadResource("aws:backup/selection:Selection", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Selection{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *Selection) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *Selection) ID() *pulumi.IDOutput {
	return r.s.ID()
}

func (r *Selection) IamRoleArn() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["iamRoleArn"])
}

// The display name of a resource selection document.
func (r *Selection) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// The backup plan ID to be associated with the selection of resources.
func (r *Selection) PlanId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["planId"])
}

// An array of strings that either contain Amazon Resource Names (ARNs) or match patterns of resources to assign to a backup plan..
func (r *Selection) Resources() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["resources"])
}

// Tag-based conditions used to specify a set of resources to assign to a backup plan.
func (r *Selection) SelectionTags() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["selectionTags"])
}

// Input properties used for looking up and filtering Selection resources.
type SelectionState struct {
	IamRoleArn interface{}
	// The display name of a resource selection document.
	Name interface{}
	// The backup plan ID to be associated with the selection of resources.
	PlanId interface{}
	// An array of strings that either contain Amazon Resource Names (ARNs) or match patterns of resources to assign to a backup plan..
	Resources interface{}
	// Tag-based conditions used to specify a set of resources to assign to a backup plan.
	SelectionTags interface{}
}

// The set of arguments for constructing a Selection resource.
type SelectionArgs struct {
	IamRoleArn interface{}
	// The display name of a resource selection document.
	Name interface{}
	// The backup plan ID to be associated with the selection of resources.
	PlanId interface{}
	// An array of strings that either contain Amazon Resource Names (ARNs) or match patterns of resources to assign to a backup plan..
	Resources interface{}
	// Tag-based conditions used to specify a set of resources to assign to a backup plan.
	SelectionTags interface{}
}

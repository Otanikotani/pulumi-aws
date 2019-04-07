# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class Group(pulumi.CustomResource):
    arn: pulumi.Output[str]
    """
    The ARN for this AutoScaling Group
    """
    availability_zones: pulumi.Output[list]
    """
    A list of one or more availability zones for the group. This parameter should not be specified when using `vpc_zone_identifier`.
    """
    default_cooldown: pulumi.Output[float]
    """
    The amount of time, in seconds, after a scaling activity completes before another scaling activity can start.
    """
    desired_capacity: pulumi.Output[float]
    """
    The number of Amazon EC2 instances that
    should be running in the group. (See also Waiting for
    Capacity below.)
    """
    enabled_metrics: pulumi.Output[list]
    """
    A list of metrics to collect. The allowed values are `GroupMinSize`, `GroupMaxSize`, `GroupDesiredCapacity`, `GroupInServiceInstances`, `GroupPendingInstances`, `GroupStandbyInstances`, `GroupTerminatingInstances`, `GroupTotalInstances`.
    * `wait_for_capacity_timeout` (Default: "10m") A maximum
    [duration](https://golang.org/pkg/time/#ParseDuration) that Terraform should
    wait for ASG instances to be healthy before timing out.  (See also Waiting
    for Capacity below.) Setting this to "0" causes
    Terraform to skip all Capacity Waiting behavior.
    """
    force_delete: pulumi.Output[bool]
    """
    Allows deleting the autoscaling group without waiting
    for all instances in the pool to terminate.  You can force an autoscaling group to delete
    even if it's in the process of scaling a resource. Normally, Terraform
    drains all the instances before deleting the group.  This bypasses that
    behavior and potentially leaves resources dangling.
    """
    health_check_grace_period: pulumi.Output[float]
    """
    Time (in seconds) after instance comes into service before checking health.
    """
    health_check_type: pulumi.Output[str]
    """
    "EC2" or "ELB". Controls how health checking is done.
    """
    initial_lifecycle_hooks: pulumi.Output[list]
    """
    One or more
    [Lifecycle Hooks](http://docs.aws.amazon.com/autoscaling/latest/userguide/lifecycle-hooks.html)
    to attach to the autoscaling group **before** instances are launched. The
    syntax is exactly the same as the separate
    [`aws_autoscaling_lifecycle_hook`](https://www.terraform.io/docs/providers/aws/r/autoscaling_lifecycle_hooks.html)
    resource, without the `autoscaling_group_name` attribute. Please note that this will only work when creating
    a new autoscaling group. For all other use-cases, please use `aws_autoscaling_lifecycle_hook` resource.
    """
    launch_configuration: pulumi.Output[str]
    """
    The name of the launch configuration to use.
    """
    launch_template: pulumi.Output[dict]
    """
    Nested argument containing launch template settings along with the overrides to specify multiple instance types. Defined below.
    """
    load_balancers: pulumi.Output[list]
    """
    A list of elastic load balancer names to add to the autoscaling
    group names. Only valid for classic load balancers. For ALBs, use `target_group_arns` instead.
    """
    max_size: pulumi.Output[float]
    """
    The maximum size of the auto scale group.
    """
    metrics_granularity: pulumi.Output[str]
    """
    The granularity to associate with the metrics to collect. The only valid value is `1Minute`. Default is `1Minute`.
    """
    min_elb_capacity: pulumi.Output[float]
    """
    Setting this causes Terraform to wait for
    this number of instances from this autoscaling group to show up healthy in the
    ELB only on creation. Updates will not wait on ELB instance number changes.
    (See also Waiting for Capacity below.)
    """
    min_size: pulumi.Output[float]
    """
    The minimum size of the auto scale group.
    (See also Waiting for Capacity below.)
    """
    mixed_instances_policy: pulumi.Output[dict]
    """
    Configuration block containing settings to define launch targets for Auto Scaling groups. Defined below.
    """
    name: pulumi.Output[str]
    """
    The name of the auto scaling group. By default generated by Terraform.
    """
    name_prefix: pulumi.Output[str]
    """
    Creates a unique name beginning with the specified
    prefix. Conflicts with `name`.
    """
    placement_group: pulumi.Output[str]
    """
    The name of the placement group into which you'll launch your instances, if any.
    """
    protect_from_scale_in: pulumi.Output[bool]
    """
    Allows setting instance protection. The
    autoscaling group will not select instances with this setting for terminination
    during scale in events.
    """
    service_linked_role_arn: pulumi.Output[str]
    """
    The ARN of the service-linked role that the ASG will use to call other AWS services
    """
    suspended_processes: pulumi.Output[list]
    """
    A list of processes to suspend for the AutoScaling Group. The allowed values are `Launch`, `Terminate`, `HealthCheck`, `ReplaceUnhealthy`, `AZRebalance`, `AlarmNotification`, `ScheduledActions`, `AddToLoadBalancer`.
    Note that if you suspend either the `Launch` or `Terminate` process types, it can prevent your autoscaling group from functioning properly.
    """
    tags: pulumi.Output[list]
    """
    A list of tag blocks. Tags documented below.
    """
    tags_collection: pulumi.Output[list]
    """
    A list of tag blocks (maps). Tags documented below.
    """
    target_group_arns: pulumi.Output[list]
    """
    A list of `aws_alb_target_group` ARNs, for use with Application Load Balancing.
    """
    termination_policies: pulumi.Output[list]
    """
    A list of policies to decide how the instances in the auto scale group should be terminated. The allowed values are `OldestInstance`, `NewestInstance`, `OldestLaunchConfiguration`, `ClosestToNextInstanceHour`, `OldestLaunchTemplate`, `AllocationStrategy`, `Default`.
    """
    vpc_zone_identifiers: pulumi.Output[list]
    """
    A list of subnet IDs to launch resources in.
    """
    wait_for_capacity_timeout: pulumi.Output[str]
    wait_for_elb_capacity: pulumi.Output[float]
    """
    Setting this will cause Terraform to wait
    for exactly this number of healthy instances from this autoscaling group in
    all attached load balancers on both create and update operations. (Takes
    precedence over `min_elb_capacity` behavior.)
    (See also Waiting for Capacity below.)
    """
    def __init__(__self__, resource_name, opts=None, availability_zones=None, default_cooldown=None, desired_capacity=None, enabled_metrics=None, force_delete=None, health_check_grace_period=None, health_check_type=None, initial_lifecycle_hooks=None, launch_configuration=None, launch_template=None, load_balancers=None, max_size=None, metrics_granularity=None, min_elb_capacity=None, min_size=None, mixed_instances_policy=None, name=None, name_prefix=None, placement_group=None, protect_from_scale_in=None, service_linked_role_arn=None, suspended_processes=None, tags=None, tags_collection=None, target_group_arns=None, termination_policies=None, vpc_zone_identifiers=None, wait_for_capacity_timeout=None, wait_for_elb_capacity=None, __name__=None, __opts__=None):
        """
        Provides an AutoScaling Group resource.
        
        > **Note:** You must specify either `launch_configuration`, `launch_template`, or `mixed_instances_policy`.
        
        ## Waiting for Capacity
        
        A newly-created ASG is initially empty and begins to scale to `min_size` (or
        `desired_capacity`, if specified) by launching instances using the provided
        Launch Configuration. These instances take time to launch and boot.
        
        On ASG Update, changes to these values also take time to result in the target
        number of instances providing service.
        
        Terraform provides two mechanisms to help consistently manage ASG scale up
        time across dependent resources.
        
        #### Waiting for ASG Capacity
        
        The first is default behavior. Terraform waits after ASG creation for
        `min_size` (or `desired_capacity`, if specified) healthy instances to show up
        in the ASG before continuing.
        
        If `min_size` or `desired_capacity` are changed in a subsequent update,
        Terraform will also wait for the correct number of healthy instances before
        continuing.
        
        Terraform considers an instance "healthy" when the ASG reports `HealthStatus:
        "Healthy"` and `LifecycleState: "InService"`. See the [AWS AutoScaling
        Docs](https://docs.aws.amazon.com/AutoScaling/latest/DeveloperGuide/AutoScalingGroupLifecycle.html)
        for more information on an ASG's lifecycle.
        
        Terraform will wait for healthy instances for up to
        `wait_for_capacity_timeout`. If ASG creation is taking more than a few minutes,
        it's worth investigating for scaling activity errors, which can be caused by
        problems with the selected Launch Configuration.
        
        Setting `wait_for_capacity_timeout` to `"0"` disables ASG Capacity waiting.
        
        #### Waiting for ELB Capacity
        
        The second mechanism is optional, and affects ASGs with attached ELBs specified
        via the `load_balancers` attribute or with ALBs specified with `target_group_arns`.
        
        The `min_elb_capacity` parameter causes Terraform to wait for at least the
        requested number of instances to show up `"InService"` in all attached ELBs
        during ASG creation.  It has no effect on ASG updates.
        
        If `wait_for_elb_capacity` is set, Terraform will wait for exactly that number
        of Instances to be `"InService"` in all attached ELBs on both creation and
        updates.
        
        These parameters can be used to ensure that service is being provided before
        Terraform moves on. If new instances don't pass the ELB's health checks for any
        reason, the Terraform apply will time out, and the ASG will be marked as
        tainted (i.e. marked to be destroyed in a follow up run).
        
        As with ASG Capacity, Terraform will wait for up to `wait_for_capacity_timeout`
        for the proper number of instances to be healthy.
        
        #### Troubleshooting Capacity Waiting Timeouts
        
        If ASG creation takes more than a few minutes, this could indicate one of a
        number of configuration problems. See the [AWS Docs on Load Balancer
        Troubleshooting](https://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/elb-troubleshooting.html)
        for more information.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[list] availability_zones: A list of one or more availability zones for the group. This parameter should not be specified when using `vpc_zone_identifier`.
        :param pulumi.Input[float] default_cooldown: The amount of time, in seconds, after a scaling activity completes before another scaling activity can start.
        :param pulumi.Input[float] desired_capacity: The number of Amazon EC2 instances that
               should be running in the group. (See also Waiting for
               Capacity below.)
        :param pulumi.Input[list] enabled_metrics: A list of metrics to collect. The allowed values are `GroupMinSize`, `GroupMaxSize`, `GroupDesiredCapacity`, `GroupInServiceInstances`, `GroupPendingInstances`, `GroupStandbyInstances`, `GroupTerminatingInstances`, `GroupTotalInstances`.
               * `wait_for_capacity_timeout` (Default: "10m") A maximum
               [duration](https://golang.org/pkg/time/#ParseDuration) that Terraform should
               wait for ASG instances to be healthy before timing out.  (See also Waiting
               for Capacity below.) Setting this to "0" causes
               Terraform to skip all Capacity Waiting behavior.
        :param pulumi.Input[bool] force_delete: Allows deleting the autoscaling group without waiting
               for all instances in the pool to terminate.  You can force an autoscaling group to delete
               even if it's in the process of scaling a resource. Normally, Terraform
               drains all the instances before deleting the group.  This bypasses that
               behavior and potentially leaves resources dangling.
        :param pulumi.Input[float] health_check_grace_period: Time (in seconds) after instance comes into service before checking health.
        :param pulumi.Input[str] health_check_type: "EC2" or "ELB". Controls how health checking is done.
        :param pulumi.Input[list] initial_lifecycle_hooks: One or more
               [Lifecycle Hooks](http://docs.aws.amazon.com/autoscaling/latest/userguide/lifecycle-hooks.html)
               to attach to the autoscaling group **before** instances are launched. The
               syntax is exactly the same as the separate
               [`aws_autoscaling_lifecycle_hook`](https://www.terraform.io/docs/providers/aws/r/autoscaling_lifecycle_hooks.html)
               resource, without the `autoscaling_group_name` attribute. Please note that this will only work when creating
               a new autoscaling group. For all other use-cases, please use `aws_autoscaling_lifecycle_hook` resource.
        :param pulumi.Input[str] launch_configuration: The name of the launch configuration to use.
        :param pulumi.Input[dict] launch_template: Nested argument containing launch template settings along with the overrides to specify multiple instance types. Defined below.
        :param pulumi.Input[list] load_balancers: A list of elastic load balancer names to add to the autoscaling
               group names. Only valid for classic load balancers. For ALBs, use `target_group_arns` instead.
        :param pulumi.Input[float] max_size: The maximum size of the auto scale group.
        :param pulumi.Input[str] metrics_granularity: The granularity to associate with the metrics to collect. The only valid value is `1Minute`. Default is `1Minute`.
        :param pulumi.Input[float] min_elb_capacity: Setting this causes Terraform to wait for
               this number of instances from this autoscaling group to show up healthy in the
               ELB only on creation. Updates will not wait on ELB instance number changes.
               (See also Waiting for Capacity below.)
        :param pulumi.Input[float] min_size: The minimum size of the auto scale group.
               (See also Waiting for Capacity below.)
        :param pulumi.Input[dict] mixed_instances_policy: Configuration block containing settings to define launch targets for Auto Scaling groups. Defined below.
        :param pulumi.Input[str] name: The name of the auto scaling group. By default generated by Terraform.
        :param pulumi.Input[str] name_prefix: Creates a unique name beginning with the specified
               prefix. Conflicts with `name`.
        :param pulumi.Input[str] placement_group: The name of the placement group into which you'll launch your instances, if any.
        :param pulumi.Input[bool] protect_from_scale_in: Allows setting instance protection. The
               autoscaling group will not select instances with this setting for terminination
               during scale in events.
        :param pulumi.Input[str] service_linked_role_arn: The ARN of the service-linked role that the ASG will use to call other AWS services
        :param pulumi.Input[list] suspended_processes: A list of processes to suspend for the AutoScaling Group. The allowed values are `Launch`, `Terminate`, `HealthCheck`, `ReplaceUnhealthy`, `AZRebalance`, `AlarmNotification`, `ScheduledActions`, `AddToLoadBalancer`.
               Note that if you suspend either the `Launch` or `Terminate` process types, it can prevent your autoscaling group from functioning properly.
        :param pulumi.Input[list] tags: A list of tag blocks. Tags documented below.
        :param pulumi.Input[list] tags_collection: A list of tag blocks (maps). Tags documented below.
        :param pulumi.Input[list] target_group_arns: A list of `aws_alb_target_group` ARNs, for use with Application Load Balancing.
        :param pulumi.Input[list] termination_policies: A list of policies to decide how the instances in the auto scale group should be terminated. The allowed values are `OldestInstance`, `NewestInstance`, `OldestLaunchConfiguration`, `ClosestToNextInstanceHour`, `OldestLaunchTemplate`, `AllocationStrategy`, `Default`.
        :param pulumi.Input[list] vpc_zone_identifiers: A list of subnet IDs to launch resources in.
        :param pulumi.Input[float] wait_for_elb_capacity: Setting this will cause Terraform to wait
               for exactly this number of healthy instances from this autoscaling group in
               all attached load balancers on both create and update operations. (Takes
               precedence over `min_elb_capacity` behavior.)
               (See also Waiting for Capacity below.)
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if not resource_name:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(resource_name, str):
            raise TypeError('Expected resource name to be a string')
        if opts and not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['availability_zones'] = availability_zones

        __props__['default_cooldown'] = default_cooldown

        __props__['desired_capacity'] = desired_capacity

        __props__['enabled_metrics'] = enabled_metrics

        __props__['force_delete'] = force_delete

        __props__['health_check_grace_period'] = health_check_grace_period

        __props__['health_check_type'] = health_check_type

        __props__['initial_lifecycle_hooks'] = initial_lifecycle_hooks

        __props__['launch_configuration'] = launch_configuration

        __props__['launch_template'] = launch_template

        __props__['load_balancers'] = load_balancers

        if max_size is None:
            raise TypeError("Missing required property 'max_size'")
        __props__['max_size'] = max_size

        __props__['metrics_granularity'] = metrics_granularity

        __props__['min_elb_capacity'] = min_elb_capacity

        if min_size is None:
            raise TypeError("Missing required property 'min_size'")
        __props__['min_size'] = min_size

        __props__['mixed_instances_policy'] = mixed_instances_policy

        __props__['name'] = name

        __props__['name_prefix'] = name_prefix

        __props__['placement_group'] = placement_group

        __props__['protect_from_scale_in'] = protect_from_scale_in

        __props__['service_linked_role_arn'] = service_linked_role_arn

        __props__['suspended_processes'] = suspended_processes

        __props__['tags'] = tags

        __props__['tags_collection'] = tags_collection

        __props__['target_group_arns'] = target_group_arns

        __props__['termination_policies'] = termination_policies

        __props__['vpc_zone_identifiers'] = vpc_zone_identifiers

        __props__['wait_for_capacity_timeout'] = wait_for_capacity_timeout

        __props__['wait_for_elb_capacity'] = wait_for_elb_capacity

        __props__['arn'] = None

        super(Group, __self__).__init__(
            'aws:autoscaling/group:Group',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


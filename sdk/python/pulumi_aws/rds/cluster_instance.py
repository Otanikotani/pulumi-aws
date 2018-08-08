# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class ClusterInstance(pulumi.CustomResource):
    """
    Provides an RDS Cluster Resource Instance. A Cluster Instance Resource defines
    attributes that are specific to a single instance in a [RDS Cluster][3],
    specifically running Amazon Aurora.
    
    Unlike other RDS resources that support replication, with Amazon Aurora you do
    not designate a primary and subsequent replicas. Instead, you simply add RDS
    Instances and Aurora manages the replication. You can use the [count][5]
    meta-parameter to make multiple instances and join them all to the same RDS
    Cluster, or you may specify different Cluster Instance resources with various
    `instance_class` sizes.
    
    For more information on Amazon Aurora, see [Aurora on Amazon RDS][2] in the Amazon RDS User Guide.
    """
    def __init__(__self__, __name__, __opts__=None, apply_immediately=None, auto_minor_version_upgrade=None, availability_zone=None, cluster_identifier=None, db_parameter_group_name=None, db_subnet_group_name=None, engine=None, engine_version=None, identifier=None, identifier_prefix=None, instance_class=None, monitoring_interval=None, monitoring_role_arn=None, performance_insights_enabled=None, performance_insights_kms_key_id=None, preferred_backup_window=None, preferred_maintenance_window=None, promotion_tier=None, publicly_accessible=None, tags=None):
        """Create a ClusterInstance resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if apply_immediately and not isinstance(apply_immediately, bool):
            raise TypeError('Expected property apply_immediately to be a bool')
        __self__.apply_immediately = apply_immediately
        """
        Specifies whether any database modifications
        are applied immediately, or during the next maintenance window. Default is`false`.
        """
        __props__['applyImmediately'] = apply_immediately

        if auto_minor_version_upgrade and not isinstance(auto_minor_version_upgrade, bool):
            raise TypeError('Expected property auto_minor_version_upgrade to be a bool')
        __self__.auto_minor_version_upgrade = auto_minor_version_upgrade
        """
        Indicates that minor engine upgrades will be applied automatically to the DB instance during the maintenance window. Default `true`.
        """
        __props__['autoMinorVersionUpgrade'] = auto_minor_version_upgrade

        if availability_zone and not isinstance(availability_zone, basestring):
            raise TypeError('Expected property availability_zone to be a basestring')
        __self__.availability_zone = availability_zone
        """
        The EC2 Availability Zone that the DB instance is created in. See [docs](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html) about the details.
        """
        __props__['availabilityZone'] = availability_zone

        if not cluster_identifier:
            raise TypeError('Missing required property cluster_identifier')
        elif not isinstance(cluster_identifier, basestring):
            raise TypeError('Expected property cluster_identifier to be a basestring')
        __self__.cluster_identifier = cluster_identifier
        """
        The identifier of the [`aws_rds_cluster`](/docs/providers/aws/r/rds_cluster.html) in which to launch this instance.
        """
        __props__['clusterIdentifier'] = cluster_identifier

        if db_parameter_group_name and not isinstance(db_parameter_group_name, basestring):
            raise TypeError('Expected property db_parameter_group_name to be a basestring')
        __self__.db_parameter_group_name = db_parameter_group_name
        """
        The name of the DB parameter group to associate with this instance.
        """
        __props__['dbParameterGroupName'] = db_parameter_group_name

        if db_subnet_group_name and not isinstance(db_subnet_group_name, basestring):
            raise TypeError('Expected property db_subnet_group_name to be a basestring')
        __self__.db_subnet_group_name = db_subnet_group_name
        """
        A DB subnet group to associate with this DB instance. **NOTE:** This must match the `db_subnet_group_name` of the attached [`aws_rds_cluster`](/docs/providers/aws/r/rds_cluster.html).
        """
        __props__['dbSubnetGroupName'] = db_subnet_group_name

        if engine and not isinstance(engine, basestring):
            raise TypeError('Expected property engine to be a basestring')
        __self__.engine = engine
        """
        The name of the database engine to be used for the RDS instance. Defaults to `aurora`. Valid Values: `aurora`, `aurora-mysql`, `aurora-postgresql`.
        For information on the difference between the available Aurora MySQL engines
        see [Comparison between Aurora MySQL 1 and Aurora MySQL 2](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AuroraMySQL.Updates.20180206.html)
        in the Amazon RDS User Guide.
        """
        __props__['engine'] = engine

        if engine_version and not isinstance(engine_version, basestring):
            raise TypeError('Expected property engine_version to be a basestring')
        __self__.engine_version = engine_version
        """
        The database engine version.
        """
        __props__['engineVersion'] = engine_version

        if identifier and not isinstance(identifier, basestring):
            raise TypeError('Expected property identifier to be a basestring')
        __self__.identifier = identifier
        """
        The indentifier for the RDS instance, if omitted, Terraform will assign a random, unique identifier.
        """
        __props__['identifier'] = identifier

        if identifier_prefix and not isinstance(identifier_prefix, basestring):
            raise TypeError('Expected property identifier_prefix to be a basestring')
        __self__.identifier_prefix = identifier_prefix
        """
        Creates a unique identifier beginning with the specified prefix. Conflicts with `identifer`.
        """
        __props__['identifierPrefix'] = identifier_prefix

        if not instance_class:
            raise TypeError('Missing required property instance_class')
        elif not isinstance(instance_class, basestring):
            raise TypeError('Expected property instance_class to be a basestring')
        __self__.instance_class = instance_class
        """
        The instance class to use. For details on CPU
        and memory, see [Scaling Aurora DB Instances][4]. Aurora currently
        supports the below instance classes.
        - db.t2.small
        - db.t2.medium
        - db.r3.large
        - db.r3.xlarge
        - db.r3.2xlarge
        - db.r3.4xlarge
        - db.r3.8xlarge
        - db.r4.large
        - db.r4.xlarge
        - db.r4.2xlarge
        - db.r4.4xlarge
        - db.r4.8xlarge
        - db.r4.16xlarge
        """
        __props__['instanceClass'] = instance_class

        if monitoring_interval and not isinstance(monitoring_interval, int):
            raise TypeError('Expected property monitoring_interval to be a int')
        __self__.monitoring_interval = monitoring_interval
        """
        The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance. To disable collecting Enhanced Monitoring metrics, specify 0. The default is 0. Valid Values: 0, 1, 5, 10, 15, 30, 60.
        """
        __props__['monitoringInterval'] = monitoring_interval

        if monitoring_role_arn and not isinstance(monitoring_role_arn, basestring):
            raise TypeError('Expected property monitoring_role_arn to be a basestring')
        __self__.monitoring_role_arn = monitoring_role_arn
        """
        The ARN for the IAM role that permits RDS to send
        enhanced monitoring metrics to CloudWatch Logs. You can find more information on the [AWS Documentation](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.html)
        what IAM permissions are needed to allow Enhanced Monitoring for RDS Instances.
        """
        __props__['monitoringRoleArn'] = monitoring_role_arn

        if performance_insights_enabled and not isinstance(performance_insights_enabled, bool):
            raise TypeError('Expected property performance_insights_enabled to be a bool')
        __self__.performance_insights_enabled = performance_insights_enabled
        """
        Specifies whether Performance Insights is enabled or not.
        """
        __props__['performanceInsightsEnabled'] = performance_insights_enabled

        if performance_insights_kms_key_id and not isinstance(performance_insights_kms_key_id, basestring):
            raise TypeError('Expected property performance_insights_kms_key_id to be a basestring')
        __self__.performance_insights_kms_key_id = performance_insights_kms_key_id
        """
        The ARN for the KMS key to encrypt Performance Insights data. When specifying `performance_insights_kms_key_id`, `performance_insights_enabled` needs to be set to true.
        """
        __props__['performanceInsightsKmsKeyId'] = performance_insights_kms_key_id

        if preferred_backup_window and not isinstance(preferred_backup_window, basestring):
            raise TypeError('Expected property preferred_backup_window to be a basestring')
        __self__.preferred_backup_window = preferred_backup_window
        """
        The daily time range during which automated backups are created if automated backups are enabled.
        Eg: "04:00-09:00"
        """
        __props__['preferredBackupWindow'] = preferred_backup_window

        if preferred_maintenance_window and not isinstance(preferred_maintenance_window, basestring):
            raise TypeError('Expected property preferred_maintenance_window to be a basestring')
        __self__.preferred_maintenance_window = preferred_maintenance_window
        """
        The window to perform maintenance in.
        Syntax: "ddd:hh24:mi-ddd:hh24:mi". Eg: "Mon:00:00-Mon:03:00".
        """
        __props__['preferredMaintenanceWindow'] = preferred_maintenance_window

        if promotion_tier and not isinstance(promotion_tier, int):
            raise TypeError('Expected property promotion_tier to be a int')
        __self__.promotion_tier = promotion_tier
        """
        Default 0. Failover Priority setting on instance level. The reader who has lower tier has higher priority to get promoter to writer.
        """
        __props__['promotionTier'] = promotion_tier

        if publicly_accessible and not isinstance(publicly_accessible, bool):
            raise TypeError('Expected property publicly_accessible to be a bool')
        __self__.publicly_accessible = publicly_accessible
        """
        Bool to control if instance is publicly accessible.
        Default `false`. See the documentation on [Creating DB Instances][6] for more
        details on controlling this property.
        """
        __props__['publiclyAccessible'] = publicly_accessible

        if tags and not isinstance(tags, dict):
            raise TypeError('Expected property tags to be a dict')
        __self__.tags = tags
        """
        A mapping of tags to assign to the instance.
        """
        __props__['tags'] = tags

        __self__.arn = pulumi.runtime.UNKNOWN
        """
        Amazon Resource Name (ARN) of cluster instance
        """
        __self__.dbi_resource_id = pulumi.runtime.UNKNOWN
        """
        The region-unique, immutable identifier for the DB instance.
        """
        __self__.endpoint = pulumi.runtime.UNKNOWN
        """
        The DNS address for this instance. May not be writable
        """
        __self__.kms_key_id = pulumi.runtime.UNKNOWN
        """
        The ARN for the KMS encryption key if one is set to the cluster.
        """
        __self__.port = pulumi.runtime.UNKNOWN
        """
        The database port
        """
        __self__.storage_encrypted = pulumi.runtime.UNKNOWN
        """
        Specifies whether the DB cluster is encrypted.
        """
        __self__.writer = pulumi.runtime.UNKNOWN
        """
        Boolean indicating if this instance is writable. `False` indicates this instance is a read replica.
        """

        super(ClusterInstance, __self__).__init__(
            'aws:rds/clusterInstance:ClusterInstance',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'applyImmediately' in outs:
            self.apply_immediately = outs['applyImmediately']
        if 'arn' in outs:
            self.arn = outs['arn']
        if 'autoMinorVersionUpgrade' in outs:
            self.auto_minor_version_upgrade = outs['autoMinorVersionUpgrade']
        if 'availabilityZone' in outs:
            self.availability_zone = outs['availabilityZone']
        if 'clusterIdentifier' in outs:
            self.cluster_identifier = outs['clusterIdentifier']
        if 'dbParameterGroupName' in outs:
            self.db_parameter_group_name = outs['dbParameterGroupName']
        if 'dbSubnetGroupName' in outs:
            self.db_subnet_group_name = outs['dbSubnetGroupName']
        if 'dbiResourceId' in outs:
            self.dbi_resource_id = outs['dbiResourceId']
        if 'endpoint' in outs:
            self.endpoint = outs['endpoint']
        if 'engine' in outs:
            self.engine = outs['engine']
        if 'engineVersion' in outs:
            self.engine_version = outs['engineVersion']
        if 'identifier' in outs:
            self.identifier = outs['identifier']
        if 'identifierPrefix' in outs:
            self.identifier_prefix = outs['identifierPrefix']
        if 'instanceClass' in outs:
            self.instance_class = outs['instanceClass']
        if 'kmsKeyId' in outs:
            self.kms_key_id = outs['kmsKeyId']
        if 'monitoringInterval' in outs:
            self.monitoring_interval = outs['monitoringInterval']
        if 'monitoringRoleArn' in outs:
            self.monitoring_role_arn = outs['monitoringRoleArn']
        if 'performanceInsightsEnabled' in outs:
            self.performance_insights_enabled = outs['performanceInsightsEnabled']
        if 'performanceInsightsKmsKeyId' in outs:
            self.performance_insights_kms_key_id = outs['performanceInsightsKmsKeyId']
        if 'port' in outs:
            self.port = outs['port']
        if 'preferredBackupWindow' in outs:
            self.preferred_backup_window = outs['preferredBackupWindow']
        if 'preferredMaintenanceWindow' in outs:
            self.preferred_maintenance_window = outs['preferredMaintenanceWindow']
        if 'promotionTier' in outs:
            self.promotion_tier = outs['promotionTier']
        if 'publiclyAccessible' in outs:
            self.publicly_accessible = outs['publiclyAccessible']
        if 'storageEncrypted' in outs:
            self.storage_encrypted = outs['storageEncrypted']
        if 'tags' in outs:
            self.tags = outs['tags']
        if 'writer' in outs:
            self.writer = outs['writer']

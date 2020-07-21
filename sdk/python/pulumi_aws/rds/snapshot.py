# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import _utilities, _tables


class Snapshot(pulumi.CustomResource):
    allocated_storage: pulumi.Output[float]
    """
    Specifies the allocated storage size in gigabytes (GB).
    """
    availability_zone: pulumi.Output[str]
    """
    Specifies the name of the Availability Zone the DB instance was located in at the time of the DB snapshot.
    """
    db_instance_identifier: pulumi.Output[str]
    """
    The DB Instance Identifier from which to take the snapshot.
    """
    db_snapshot_arn: pulumi.Output[str]
    """
    The Amazon Resource Name (ARN) for the DB snapshot.
    """
    db_snapshot_identifier: pulumi.Output[str]
    """
    The Identifier for the snapshot.
    """
    encrypted: pulumi.Output[bool]
    """
    Specifies whether the DB snapshot is encrypted.
    """
    engine: pulumi.Output[str]
    """
    Specifies the name of the database engine.
    """
    engine_version: pulumi.Output[str]
    """
    Specifies the version of the database engine.
    """
    iops: pulumi.Output[float]
    """
    Specifies the Provisioned IOPS (I/O operations per second) value of the DB instance at the time of the snapshot.
    """
    kms_key_id: pulumi.Output[str]
    """
    The ARN for the KMS encryption key.
    """
    license_model: pulumi.Output[str]
    """
    License model information for the restored DB instance.
    """
    option_group_name: pulumi.Output[str]
    """
    Provides the option group name for the DB snapshot.
    """
    port: pulumi.Output[float]
    snapshot_type: pulumi.Output[str]
    source_db_snapshot_identifier: pulumi.Output[str]
    """
    The DB snapshot Arn that the DB snapshot was copied from. It only has value in case of cross customer or cross region copy.
    """
    source_region: pulumi.Output[str]
    """
    The region that the DB snapshot was created in or copied from.
    """
    status: pulumi.Output[str]
    """
    Specifies the status of this DB snapshot.
    """
    storage_type: pulumi.Output[str]
    """
    Specifies the storage type associated with DB snapshot.
    """
    tags: pulumi.Output[dict]
    """
    Key-value map of resource tags
    """
    vpc_id: pulumi.Output[str]
    """
    Specifies the storage type associated with DB snapshot.
    """
    def __init__(__self__, resource_name, opts=None, db_instance_identifier=None, db_snapshot_identifier=None, tags=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages an RDS database instance snapshot. For managing RDS database cluster snapshots, see the `rds.ClusterSnapshot` resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        bar = aws.rds.Instance("bar",
            allocated_storage=10,
            backup_retention_period=0,
            engine="MySQL",
            engine_version="5.6.21",
            instance_class="db.t2.micro",
            maintenance_window="Fri:09:00-Fri:09:30",
            name="baz",
            parameter_group_name="default.mysql5.6",
            password="barbarbarbar",
            username="foo")
        test = aws.rds.Snapshot("test",
            db_instance_identifier=bar.id,
            db_snapshot_identifier="testsnapshot1234")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] db_instance_identifier: The DB Instance Identifier from which to take the snapshot.
        :param pulumi.Input[str] db_snapshot_identifier: The Identifier for the snapshot.
        :param pulumi.Input[dict] tags: Key-value map of resource tags
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            if db_instance_identifier is None:
                raise TypeError("Missing required property 'db_instance_identifier'")
            __props__['db_instance_identifier'] = db_instance_identifier
            if db_snapshot_identifier is None:
                raise TypeError("Missing required property 'db_snapshot_identifier'")
            __props__['db_snapshot_identifier'] = db_snapshot_identifier
            __props__['tags'] = tags
            __props__['allocated_storage'] = None
            __props__['availability_zone'] = None
            __props__['db_snapshot_arn'] = None
            __props__['encrypted'] = None
            __props__['engine'] = None
            __props__['engine_version'] = None
            __props__['iops'] = None
            __props__['kms_key_id'] = None
            __props__['license_model'] = None
            __props__['option_group_name'] = None
            __props__['port'] = None
            __props__['snapshot_type'] = None
            __props__['source_db_snapshot_identifier'] = None
            __props__['source_region'] = None
            __props__['status'] = None
            __props__['storage_type'] = None
            __props__['vpc_id'] = None
        super(Snapshot, __self__).__init__(
            'aws:rds/snapshot:Snapshot',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, allocated_storage=None, availability_zone=None, db_instance_identifier=None, db_snapshot_arn=None, db_snapshot_identifier=None, encrypted=None, engine=None, engine_version=None, iops=None, kms_key_id=None, license_model=None, option_group_name=None, port=None, snapshot_type=None, source_db_snapshot_identifier=None, source_region=None, status=None, storage_type=None, tags=None, vpc_id=None):
        """
        Get an existing Snapshot resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[float] allocated_storage: Specifies the allocated storage size in gigabytes (GB).
        :param pulumi.Input[str] availability_zone: Specifies the name of the Availability Zone the DB instance was located in at the time of the DB snapshot.
        :param pulumi.Input[str] db_instance_identifier: The DB Instance Identifier from which to take the snapshot.
        :param pulumi.Input[str] db_snapshot_arn: The Amazon Resource Name (ARN) for the DB snapshot.
        :param pulumi.Input[str] db_snapshot_identifier: The Identifier for the snapshot.
        :param pulumi.Input[bool] encrypted: Specifies whether the DB snapshot is encrypted.
        :param pulumi.Input[str] engine: Specifies the name of the database engine.
        :param pulumi.Input[str] engine_version: Specifies the version of the database engine.
        :param pulumi.Input[float] iops: Specifies the Provisioned IOPS (I/O operations per second) value of the DB instance at the time of the snapshot.
        :param pulumi.Input[str] kms_key_id: The ARN for the KMS encryption key.
        :param pulumi.Input[str] license_model: License model information for the restored DB instance.
        :param pulumi.Input[str] option_group_name: Provides the option group name for the DB snapshot.
        :param pulumi.Input[str] source_db_snapshot_identifier: The DB snapshot Arn that the DB snapshot was copied from. It only has value in case of cross customer or cross region copy.
        :param pulumi.Input[str] source_region: The region that the DB snapshot was created in or copied from.
        :param pulumi.Input[str] status: Specifies the status of this DB snapshot.
        :param pulumi.Input[str] storage_type: Specifies the storage type associated with DB snapshot.
        :param pulumi.Input[dict] tags: Key-value map of resource tags
        :param pulumi.Input[str] vpc_id: Specifies the storage type associated with DB snapshot.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["allocated_storage"] = allocated_storage
        __props__["availability_zone"] = availability_zone
        __props__["db_instance_identifier"] = db_instance_identifier
        __props__["db_snapshot_arn"] = db_snapshot_arn
        __props__["db_snapshot_identifier"] = db_snapshot_identifier
        __props__["encrypted"] = encrypted
        __props__["engine"] = engine
        __props__["engine_version"] = engine_version
        __props__["iops"] = iops
        __props__["kms_key_id"] = kms_key_id
        __props__["license_model"] = license_model
        __props__["option_group_name"] = option_group_name
        __props__["port"] = port
        __props__["snapshot_type"] = snapshot_type
        __props__["source_db_snapshot_identifier"] = source_db_snapshot_identifier
        __props__["source_region"] = source_region
        __props__["status"] = status
        __props__["storage_type"] = storage_type
        __props__["tags"] = tags
        __props__["vpc_id"] = vpc_id
        return Snapshot(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

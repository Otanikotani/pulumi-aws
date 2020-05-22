// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Outputs
{

    [OutputType]
    public sealed class ProviderEndpoint
    {
        public readonly string? Accessanalyzer;
        public readonly string? Acm;
        public readonly string? Acmpca;
        public readonly string? Amplify;
        public readonly string? Apigateway;
        public readonly string? Applicationautoscaling;
        public readonly string? Applicationinsights;
        public readonly string? Appmesh;
        public readonly string? Appstream;
        public readonly string? Appsync;
        public readonly string? Athena;
        public readonly string? Autoscaling;
        public readonly string? Autoscalingplans;
        public readonly string? Backup;
        public readonly string? Batch;
        public readonly string? Budgets;
        public readonly string? Cloud9;
        public readonly string? Cloudformation;
        public readonly string? Cloudfront;
        public readonly string? Cloudhsm;
        public readonly string? Cloudsearch;
        public readonly string? Cloudtrail;
        public readonly string? Cloudwatch;
        public readonly string? Cloudwatchevents;
        public readonly string? Cloudwatchlogs;
        public readonly string? Codebuild;
        public readonly string? Codecommit;
        public readonly string? Codedeploy;
        public readonly string? Codepipeline;
        public readonly string? Cognitoidentity;
        public readonly string? Cognitoidp;
        public readonly string? Configservice;
        public readonly string? Cur;
        public readonly string? Dataexchange;
        public readonly string? Datapipeline;
        public readonly string? Datasync;
        public readonly string? Dax;
        public readonly string? Devicefarm;
        public readonly string? Directconnect;
        public readonly string? Dlm;
        public readonly string? Dms;
        public readonly string? Docdb;
        public readonly string? Ds;
        public readonly string? Dynamodb;
        public readonly string? Ec2;
        public readonly string? Ecr;
        public readonly string? Ecs;
        public readonly string? Efs;
        public readonly string? Eks;
        public readonly string? Elasticache;
        public readonly string? Elasticbeanstalk;
        public readonly string? Elastictranscoder;
        public readonly string? Elb;
        public readonly string? Emr;
        public readonly string? Es;
        public readonly string? Firehose;
        public readonly string? Fms;
        public readonly string? Forecast;
        public readonly string? Fsx;
        public readonly string? Gamelift;
        public readonly string? Glacier;
        public readonly string? Globalaccelerator;
        public readonly string? Glue;
        public readonly string? Greengrass;
        public readonly string? Guardduty;
        public readonly string? Iam;
        public readonly string? Imagebuilder;
        public readonly string? Inspector;
        public readonly string? Iot;
        public readonly string? Iotanalytics;
        public readonly string? Iotevents;
        public readonly string? Kafka;
        public readonly string? Kinesis;
        public readonly string? KinesisAnalytics;
        public readonly string? Kinesisanalytics;
        public readonly string? Kinesisanalyticsv2;
        public readonly string? Kinesisvideo;
        public readonly string? Kms;
        public readonly string? Lakeformation;
        public readonly string? Lambda;
        public readonly string? Lexmodels;
        public readonly string? Licensemanager;
        public readonly string? Lightsail;
        public readonly string? Macie;
        public readonly string? Managedblockchain;
        public readonly string? Marketplacecatalog;
        public readonly string? Mediaconnect;
        public readonly string? Mediaconvert;
        public readonly string? Medialive;
        public readonly string? Mediapackage;
        public readonly string? Mediastore;
        public readonly string? Mediastoredata;
        public readonly string? Mq;
        public readonly string? Neptune;
        public readonly string? Networkmanager;
        public readonly string? Opsworks;
        public readonly string? Organizations;
        public readonly string? Personalize;
        public readonly string? Pinpoint;
        public readonly string? Pricing;
        public readonly string? Qldb;
        public readonly string? Quicksight;
        public readonly string? R53;
        public readonly string? Ram;
        public readonly string? Rds;
        public readonly string? Redshift;
        public readonly string? Resourcegroups;
        public readonly string? Route53;
        public readonly string? Route53domains;
        public readonly string? Route53resolver;
        public readonly string? S3;
        public readonly string? S3control;
        public readonly string? Sagemaker;
        public readonly string? Sdb;
        public readonly string? Secretsmanager;
        public readonly string? Securityhub;
        public readonly string? Serverlessrepo;
        public readonly string? Servicecatalog;
        public readonly string? Servicediscovery;
        public readonly string? Servicequotas;
        public readonly string? Ses;
        public readonly string? Shield;
        public readonly string? Sns;
        public readonly string? Sqs;
        public readonly string? Ssm;
        public readonly string? Stepfunctions;
        public readonly string? Storagegateway;
        public readonly string? Sts;
        public readonly string? Swf;
        public readonly string? Synthetics;
        public readonly string? Transfer;
        public readonly string? Waf;
        public readonly string? Wafregional;
        public readonly string? Wafv2;
        public readonly string? Worklink;
        public readonly string? Workmail;
        public readonly string? Workspaces;
        public readonly string? Xray;

        [OutputConstructor]
        private ProviderEndpoint(
            string? accessanalyzer,

            string? acm,

            string? acmpca,

            string? amplify,

            string? apigateway,

            string? applicationautoscaling,

            string? applicationinsights,

            string? appmesh,

            string? appstream,

            string? appsync,

            string? athena,

            string? autoscaling,

            string? autoscalingplans,

            string? backup,

            string? batch,

            string? budgets,

            string? cloud9,

            string? cloudformation,

            string? cloudfront,

            string? cloudhsm,

            string? cloudsearch,

            string? cloudtrail,

            string? cloudwatch,

            string? cloudwatchevents,

            string? cloudwatchlogs,

            string? codebuild,

            string? codecommit,

            string? codedeploy,

            string? codepipeline,

            string? cognitoidentity,

            string? cognitoidp,

            string? configservice,

            string? cur,

            string? dataexchange,

            string? datapipeline,

            string? datasync,

            string? dax,

            string? devicefarm,

            string? directconnect,

            string? dlm,

            string? dms,

            string? docdb,

            string? ds,

            string? dynamodb,

            string? ec2,

            string? ecr,

            string? ecs,

            string? efs,

            string? eks,

            string? elasticache,

            string? elasticbeanstalk,

            string? elastictranscoder,

            string? elb,

            string? emr,

            string? es,

            string? firehose,

            string? fms,

            string? forecast,

            string? fsx,

            string? gamelift,

            string? glacier,

            string? globalaccelerator,

            string? glue,

            string? greengrass,

            string? guardduty,

            string? iam,

            string? imagebuilder,

            string? inspector,

            string? iot,

            string? iotanalytics,

            string? iotevents,

            string? kafka,

            string? kinesis,

            string? kinesisAnalytics,

            string? kinesisanalytics,

            string? kinesisanalyticsv2,

            string? kinesisvideo,

            string? kms,

            string? lakeformation,

            string? lambda,

            string? lexmodels,

            string? licensemanager,

            string? lightsail,

            string? macie,

            string? managedblockchain,

            string? marketplacecatalog,

            string? mediaconnect,

            string? mediaconvert,

            string? medialive,

            string? mediapackage,

            string? mediastore,

            string? mediastoredata,

            string? mq,

            string? neptune,

            string? networkmanager,

            string? opsworks,

            string? organizations,

            string? personalize,

            string? pinpoint,

            string? pricing,

            string? qldb,

            string? quicksight,

            string? r53,

            string? ram,

            string? rds,

            string? redshift,

            string? resourcegroups,

            string? route53,

            string? route53domains,

            string? route53resolver,

            string? s3,

            string? s3control,

            string? sagemaker,

            string? sdb,

            string? secretsmanager,

            string? securityhub,

            string? serverlessrepo,

            string? servicecatalog,

            string? servicediscovery,

            string? servicequotas,

            string? ses,

            string? shield,

            string? sns,

            string? sqs,

            string? ssm,

            string? stepfunctions,

            string? storagegateway,

            string? sts,

            string? swf,

            string? synthetics,

            string? transfer,

            string? waf,

            string? wafregional,

            string? wafv2,

            string? worklink,

            string? workmail,

            string? workspaces,

            string? xray)
        {
            Accessanalyzer = accessanalyzer;
            Acm = acm;
            Acmpca = acmpca;
            Amplify = amplify;
            Apigateway = apigateway;
            Applicationautoscaling = applicationautoscaling;
            Applicationinsights = applicationinsights;
            Appmesh = appmesh;
            Appstream = appstream;
            Appsync = appsync;
            Athena = athena;
            Autoscaling = autoscaling;
            Autoscalingplans = autoscalingplans;
            Backup = backup;
            Batch = batch;
            Budgets = budgets;
            Cloud9 = cloud9;
            Cloudformation = cloudformation;
            Cloudfront = cloudfront;
            Cloudhsm = cloudhsm;
            Cloudsearch = cloudsearch;
            Cloudtrail = cloudtrail;
            Cloudwatch = cloudwatch;
            Cloudwatchevents = cloudwatchevents;
            Cloudwatchlogs = cloudwatchlogs;
            Codebuild = codebuild;
            Codecommit = codecommit;
            Codedeploy = codedeploy;
            Codepipeline = codepipeline;
            Cognitoidentity = cognitoidentity;
            Cognitoidp = cognitoidp;
            Configservice = configservice;
            Cur = cur;
            Dataexchange = dataexchange;
            Datapipeline = datapipeline;
            Datasync = datasync;
            Dax = dax;
            Devicefarm = devicefarm;
            Directconnect = directconnect;
            Dlm = dlm;
            Dms = dms;
            Docdb = docdb;
            Ds = ds;
            Dynamodb = dynamodb;
            Ec2 = ec2;
            Ecr = ecr;
            Ecs = ecs;
            Efs = efs;
            Eks = eks;
            Elasticache = elasticache;
            Elasticbeanstalk = elasticbeanstalk;
            Elastictranscoder = elastictranscoder;
            Elb = elb;
            Emr = emr;
            Es = es;
            Firehose = firehose;
            Fms = fms;
            Forecast = forecast;
            Fsx = fsx;
            Gamelift = gamelift;
            Glacier = glacier;
            Globalaccelerator = globalaccelerator;
            Glue = glue;
            Greengrass = greengrass;
            Guardduty = guardduty;
            Iam = iam;
            Imagebuilder = imagebuilder;
            Inspector = inspector;
            Iot = iot;
            Iotanalytics = iotanalytics;
            Iotevents = iotevents;
            Kafka = kafka;
            Kinesis = kinesis;
            KinesisAnalytics = kinesisAnalytics;
            Kinesisanalytics = kinesisanalytics;
            Kinesisanalyticsv2 = kinesisanalyticsv2;
            Kinesisvideo = kinesisvideo;
            Kms = kms;
            Lakeformation = lakeformation;
            Lambda = lambda;
            Lexmodels = lexmodels;
            Licensemanager = licensemanager;
            Lightsail = lightsail;
            Macie = macie;
            Managedblockchain = managedblockchain;
            Marketplacecatalog = marketplacecatalog;
            Mediaconnect = mediaconnect;
            Mediaconvert = mediaconvert;
            Medialive = medialive;
            Mediapackage = mediapackage;
            Mediastore = mediastore;
            Mediastoredata = mediastoredata;
            Mq = mq;
            Neptune = neptune;
            Networkmanager = networkmanager;
            Opsworks = opsworks;
            Organizations = organizations;
            Personalize = personalize;
            Pinpoint = pinpoint;
            Pricing = pricing;
            Qldb = qldb;
            Quicksight = quicksight;
            R53 = r53;
            Ram = ram;
            Rds = rds;
            Redshift = redshift;
            Resourcegroups = resourcegroups;
            Route53 = route53;
            Route53domains = route53domains;
            Route53resolver = route53resolver;
            S3 = s3;
            S3control = s3control;
            Sagemaker = sagemaker;
            Sdb = sdb;
            Secretsmanager = secretsmanager;
            Securityhub = securityhub;
            Serverlessrepo = serverlessrepo;
            Servicecatalog = servicecatalog;
            Servicediscovery = servicediscovery;
            Servicequotas = servicequotas;
            Ses = ses;
            Shield = shield;
            Sns = sns;
            Sqs = sqs;
            Ssm = ssm;
            Stepfunctions = stepfunctions;
            Storagegateway = storagegateway;
            Sts = sts;
            Swf = swf;
            Synthetics = synthetics;
            Transfer = transfer;
            Waf = waf;
            Wafregional = wafregional;
            Wafv2 = wafv2;
            Worklink = worklink;
            Workmail = workmail;
            Workspaces = workspaces;
            Xray = xray;
        }
    }
}

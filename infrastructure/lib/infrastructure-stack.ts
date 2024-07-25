import * as cdk from 'aws-cdk-lib';
import * as s3 from 'aws-cdk-lib/aws-s3';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as iam from "aws-cdk-lib/aws-iam";
import * as path from "path";
import { PythonLayerVersion } from "@aws-cdk/aws-lambda-python-alpha";
import { Construct } from 'constructs';
// import * as sqs from 'aws-cdk-lib/aws-sqs';

interface StackProps extends cdk.StackProps {
  environment: {
    databse_host: string;
    database_name: string;
    database_user: string;
    database_password: string;
  };
}

export class PipelineStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props: StackProps) {
    super(scope, id, props);

    // s3 bucket
    const bucket = new s3.Bucket(this, "ColdStorageBucket", {
      blockPublicAccess: s3.BlockPublicAccess.BLOCK_ALL,
      bucketName: "ColdStorage",
    });

    // lambda function
    const pipelineCode = lambda.Code.fromAsset(path.join(__dirname, "..", "..", "pipeline"));

    const pipelineDependencyLayer = new PythonLayerVersion(this, "PipelineDependencies", {
      entry: path.join(__dirname, "..", "..", "pipeline"),
      compatibleRuntimes: [lambda.Runtime.PYTHON_3_12],
    });
  
    const role = new iam.Role(this, "PipelineLambdaRole", {
      roleName: "PipelineLambdaRole",
      assumedBy: new iam.ServicePrincipal("lambda.amazonaws.com"),
      managedPolicies: [
        iam.ManagedPolicy.fromAwsManagedPolicyName("service-role/AWSLambdaBasicExecutionRole"),
      ],
    });

    bucket.grantWrite(role);

    const lambdaFunction = new lambda.Function(this, "PipelineLambda", {
      functionName: "PipelineLambda",
      runtime: lambda.Runtime.PYTHON_3_12,
      handler: "lambda_handler.handler",
      code: pipelineCode,
      role: role,
      layers: [pipelineDependencyLayer],
      memorySize: 512,
      timeout: cdk.Duration.seconds(120),
      environment: props.environment,
    });
  }
}

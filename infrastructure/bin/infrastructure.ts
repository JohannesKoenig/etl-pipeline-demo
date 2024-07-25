#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { PipelineStack } from '../lib/pipeline_stack';

// Environment variables are passed to the stack. This could either be done locally with environment variables
// or secrets could also be stored in AWS Secrets Manager.


const app = new cdk.App();
new PipelineStack(app, 'PipelineStack', {
  env: {
    region: process.env.CDK_DEFAULT_REGION,
    account: process.env.CDK_DEFAULT_ACCOUNT,
  },
  environment: {
    database_host: process.env.DATABASE_HOST ? process.env.DATABASE_HOST : "database.local",
    database_name: process.env.DATABASE_NAME ? process.env.DATABASE_NAME : "database",
    database_user: process.env.DATABASE_USER ? process.env.DATABASE_USER : "user", // dummy value - no user names need to be stored in plaintext
    database_password: process.env.DATABASE_PASSWORD ? process.env.DATABASE_PASSWORD : "dummy_password", // dummy value - no passwords should be stored in plaintext
  },
});
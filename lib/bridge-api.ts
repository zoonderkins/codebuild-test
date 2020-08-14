import * as cdk from '@aws-cdk/core'
import * as lambda from '@aws-cdk/aws-lambda'

export class BridgeApiStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props)

    new lambda.Function(this, 'api', {
      runtime: lambda.Runtime.NODEJS_12_X,
      code: lambda.AssetCode.fromAsset('lambda'),
      handler: 'index.handler',
      memorySize: 256,
      timeout: cdk.Duration.seconds(40),
    })
  }
}

#!/usr/bin/env node
import 'source-map-support/register'
import * as cdk from '@aws-cdk/core'
import { BridgeApiStack } from '../lib/bridge-api'

// App initailize
const app = new cdk.App()

// Bridge Api
const bridgeApi = new BridgeApiStack(app, 'sygna-bridge-api-lambda-ping-cdn-POC-dev')


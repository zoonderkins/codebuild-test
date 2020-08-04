import json
import os
import boto3
import sys
from pprint import pprint
from botocore.exceptions import ClientError
from base64 import b64decode
from urllib.parse import parse_qs
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from datetime import datetime, timezone
import pytz

tz = pytz.timezone('Asia/Taipei')

# utc_dt = datetime.now(timezone.utc)  # UTC time
# dt = utc_dt.astimezone()  # local time

SLACK_CHANNEL = os.environ['SLACK_CHANNEL']
SLACK_API_URL = "https://slack.com/api"
SLACK_BOT_TOKEN = os.environ['SLACK_BOT_TOKEN']
AWS_REGION = os.environ["AWS_REGION"]
CODE_BUILD_ID = os.environ["CODEBUILD_BUILD_ID"]
CODEBUILD_BUILD_SUCCEEDING = os.environ["CODEBUILD_BUILD_SUCCEEDING"]
BUILD_FINISH_TIME = taipei_now = datetime.now(tz)

print(f"Time: {BUILD_FINISH_TIME}, Build staus: {CODEBUILD_BUILD_SUCCEEDING}")

if (CODEBUILD_BUILD_SUCCEEDING == "1"):
    CODEBUILD_BUILD_SUCCEEDING = "Succesful ❇️"
else:
    CODEBUILD_BUILD_SUCCEEDING = "Failed ❌"

resend = {
    "channel": SLACK_CHANNEL,
    "blocks": [{
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": f" {CODE_BUILD_ID} \n Region: {AWS_REGION} \n Build status:{CODEBUILD_BUILD_SUCCEEDING} \n Time: {BUILD_FINISH_TIME} (Taipei)"
        }
    }]
}
req = Request(f'{SLACK_API_URL}/chat.postMessage', json.dumps(resend).encode('utf-8'),
              headers={'content-type': 'application/json', "Authorization": SLACK_BOT_TOKEN})
response = urlopen(req)
html = response.read()
json_obj = json.loads(html)
print(json.dumps(json_obj))

from uuid import uuid4

import boto3

from .secrets import AWS_ACCESS_KEY_ID, AWS_DEFAULT_REGION, AWS_SECRET_ACCESS_KEY

dynamodb = boto3.resource(
    "dynamodb",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_DEFAULT_REGION,
).Table("ac_state")


item = {
    "state_id": str(uuid4()),
    "name": "temp",
    "temperature": 23,
    "status": "ON",
}

# Insert the item
response = dynamodb.put_item(Item=item)

# Print response
print("Insert response:", response)

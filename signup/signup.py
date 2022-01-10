import boto3
import json
import os

def lambda_handler(event, context):

    loaded_body = json.loads(event["body"])
    username = loaded_body["username"]
    password = loaded_body["password"]

    client = boto3.client("cognito-idp", region_name="us-west-1")

    # The below code, will do the sign-up
    response = client.sign_up(
        ClientId=os.environ['USER_POOL_CLIENT_ID'],
        Username=username,
        Password=password,
        UserAttributes=[{"Name": "email", "Value": username}],
    )


    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": response,
        }),
    }

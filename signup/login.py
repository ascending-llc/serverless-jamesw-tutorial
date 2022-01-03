import boto3
import json
import os

def lambda_handler(event, context):
    
    loaded_body = json.loads(event["body"])
    username = loaded_body["username"]
    password = loaded_body["password"]

    client = boto3.client("cognito-idp", region_name="us-west-1")

    # this handles the authorization of user
    resp = client.admin_initiate_auth(
        UserPoolId=os.environ['USER_POOL_ID'],
        ClientId=os.environ['USER_POOL_CLIENT_ID'],
        AuthFlow='ADMIN_NO_SRP_AUTH',
        AuthParameters={
            "USERNAME": username,
            "PASSWORD": password
        }
    )
    
    # generating id token
    id_token = resp["AuthenticationResult"]["IdToken"]

    # returning id token to caller
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": id_token,
        }),
    }
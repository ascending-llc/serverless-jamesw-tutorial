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

    # add username and password to dynamodb
    # encode with username and password, jwt function
    # inside the jwtAuthoizer funvtion, decode it and retrive udername nad password
    # go in dynmodb to chevk if ther id user with swame udername andnpassword
    # embred jwt to the user, jwt will be intercepted w\by authorizer
    # authorizer is the interception

    # generating id token
    # this should be a JWT token!
    id_token = resp["AuthenticationResult"]["IdToken"]

    # returning id token to caller
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": id_token,
        }),
    }
import boto3
import json

def lambda_handler(event, context):

    loaded_body = json.loads(event["body"])
    username = loaded_body["username"]
    password = loaded_body["password"]

    client = boto3.client("cognito-idp", region_name="us-west-1")

    # this handles the authorization of user
    resp = client.admin_initiate_auth(
        UserPoolId="us-west-1_6vx2GPTnF",
        ClientId="61po7rn17jr6kngjfmpq3d2r6b",
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
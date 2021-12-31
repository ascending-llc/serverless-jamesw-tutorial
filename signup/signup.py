import boto3
import json

def lambda_handler(event, context):

    loaded_body = json.loads(event["body"])
    username = loaded_body["username"]
    password = loaded_body["password"]

    client = boto3.client("cognito-idp", region_name="us-west-1")

    # The below code, will do the sign-up
    response = client.sign_up(
        ClientId="61po7rn17jr6kngjfmpq3d2r6b",
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
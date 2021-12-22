import json
import boto3

def lambda_handler(event, context):

    client = boto3.resource('dynamodb')
    table = client.Table('myFoodTable')
    response = table.scan()
    data = response['Items']

    if event['httpMethod'] == 'GET':

        return {"statusCode": 200,
        "body": json.dumps({"message": data})
        }
        
    elif event['httpMethod'] == 'POST':
        
        body = event['body']
        loaded_body = json.loads(body)
        season = loaded_body['season']
        country = loaded_body['country']
        name = loaded_body['name']
        FoodId = name + country

        for i in data:
            if i['FoodID'] == FoodId:
                return {"StatusCode": 400,
                        "body": json.dumps({"message": "FoodId already in the db"})
                }

        item = {"FoodID": FoodId,
                "county": country,
                "season": season,
                "name": name}

        table.put_item(Item=item)
        
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "added to db"})
        }


import json
import base64


def lambda_handler(event, context):
    # TODO implement
    
    for record in event["Records"]:
        print(base64.b64decode(record["kinesis"]["data"]).decode("utf8"))
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!'),
        "event":event
    }

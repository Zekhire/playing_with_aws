# https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.01.html
# https://aws.amazon.com/getting-started/hands-on/create-manage-nonrelational-database-dynamodb/3/

import boto3
import time

def create_movie_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.create_table(
        TableName='Movies',
        KeySchema=[
            {
                'AttributeName': 'year',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'title',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'year',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'title',
                'AttributeType': 'S'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    return table


if __name__ == '__main__':
    # movie_table = create_movie_table()

    dynamodb = boto3.resource('dynamodb')
    movie_table = dynamodb.Table('Movies')
    item = {
        "year": 1985,
        "title": "Schreck",
        "info":
        {
            "plot": "xD",
            "details": "fool"
        }
    }
    movie_table.put_item(Item=item)
    # item = {
    #     "year": 1987,
    #     "title": "Schreck34",
    #     "info":
    #     {
    #         "plot": "xD",
    #         "details": "foo"
    #     }
    # }
    # movie_table.put_item(Item=item)
    # item = {
    #     "year": 1987,
    #     "title": "Schreck2"
    # }
    # movie_table.put_item(Item=item)
    # item = {
    #     "year": 1987,
    #     "title": "Schreck3154"
    # }
    # movie_table.put_item(Item=item)


    print("Table status:", movie_table.table_status)
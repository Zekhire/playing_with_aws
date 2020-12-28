# https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.04.html?fbclid=IwAR2KLI5otHKVvjDiRGIxVjLwgpSJSySgFoEUl2vEqKwak3Ao8OHmgOcAI3M

import boto3
from boto3.dynamodb.conditions import Key


def query_movies(year, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('Movies')
    print(table.scan())
    quit()
    response = table.query(
        KeyConditionExpression=Key('year').eq(year),
        ScanIndexForward=False,
        Limit=1
    )
    return response['Items']


if __name__ == '__main__':
    query_year = 1987
    print(f"Movies from {query_year}")
    movies = query_movies(query_year)
    for movie in movies:
        # print(movie)
        # print(movie["info:"]["plot"])
        print(movie['year'], ":", movie['title'])
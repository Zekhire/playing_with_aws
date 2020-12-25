# Example from:
# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-example-creating-buckets.html

import logging
import boto3
from botocore.exceptions import ClientError
import json


def create_bucket(bucket_name, region=None):
    """Create an S3 bucket in a specified region

    If a region is not specified, the bucket is created in the S3 default
    region (us-east-1).

    :param bucket_name: Bucket to create
    :param region: String region to create bucket in, e.g., 'us-west-2'
    :return: True if bucket created, else False
    """

    # Create bucket
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True



def create_file(data, bucket_name, file_name):
    s3_client = boto3.resource('s3')
    s3object = s3_client.Object(bucket_name, file_name)

    s3object.put(
        Body=(bytes(json.dumps(data).encode('UTF-8')))
    )



if __name__ == "__main__":
    bucket_name = "testbucketto3"
    file_name = "testdir/testfile.json"

    data = {
        "key0": "value0",
        "key1": "value1",
        "key2": "value2",
        "key3": "value3"
    }

    if create_bucket(bucket_name):
        create_file(data, bucket_name, file_name)

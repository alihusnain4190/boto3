import boto3
import logging
import boto3
from botocore.exceptions import ClientError

def list_all_bucket():
    try:
        s3_client=boto3.client('s3')
        resp=s3_client.list_buckets()
        print("Total Bucket in region")
        for bucket in resp['Buckets']:
            print(bucket)

    except ClientError as e :
        print(e)
        logging.error(e)
        return False
    return True

list_all_bucket()
import boto3
import os
from dotenv import load_dotenv

load_dotenv()


def create_bucket():
    
    s3 = boto3.resource(
        's3',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
        region_name=os.getenv('AWS_DEFUALT_REGION')
    )
    bucket_name = 'sales-transactions-bucket'
    s3.create_bucket(
        Bucket  = bucket_name,
    )

create_bucket()
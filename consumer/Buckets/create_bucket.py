import boto3
import os
from dotenv import load_dotenv

load_dotenv()


def create_bucket():
    
    s3 = boto3.client(
        's3'
    )
    bucket_name = 'sales-transactions-bucket'
    s3.create_bucket(
        Bucket  = bucket_name,
    )

create_bucket()

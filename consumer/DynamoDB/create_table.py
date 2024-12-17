import boto3
from dotenv import load_dotenv
import os
import logging
load_dotenv()

def create_dynamodb_table():
    dynamodb  = boto3.resource(
        'dynamodb',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
        region_name=os.getenv('AWS_DEFAULT_REGION')
    )

    table_name = 'Sales-Transactions'
    response = dynamodb.create_table(
    TableName= table_name,
    KeySchema=[
        {'AttributeName': 'transaction_id', 'KeyType': 'HASH'}
    ],
    AttributeDefinitions=[
        {'AttributeName': 'transaction_id', 'AttributeType': 'S'}
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    },
    
    )
    logging.info(response)

create_dynamodb_table()
    

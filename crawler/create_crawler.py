import boto3
import os
from dotenv import load_dotenv
import logging
load_dotenv()

def create_crawler():

    client = boto3.client(
        'glue',
        )
    
    response  = client.create_crawler(
        Name = 'Sales-Transactions-Crawler',
        Role = 'ServiceRole',
        DatabaseName = 'Sales-Transactions-Database-Glue',
       Targets={
            'S3Targets': [
                {
                    'Path': 's3://sales-transactions-bucket/transactions/2024/',  # Replace with your S3 bucket path
                },
            ],
        },
        TablePrefix = 'sales_',
        SchemaChangePolicy = {
            'UpdateBehavior': 'UPDATE_IN_DATABASE',
            'DeleteBehavior': 'DEPRECATE_IN_DATABASE'
        }
    )
    logging.info(response)
create_crawler()
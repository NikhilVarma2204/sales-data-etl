import boto3
import logging
import os
from dotenv import load_dotenv

load_dotenv()
# Set up logging
logging.basicConfig(level=logging.INFO)

def create_dynamodb_table():
    dynamodb = boto3.client('dynamodb')

    table_name = 'Sales-Transactions'
    try:
        # Create the DynamoDB table
        response = dynamodb.create_table(
            TableName=table_name,
            KeySchema=[
                {'AttributeName': 'transaction_id', 'KeyType': 'HASH'}
            ],
            AttributeDefinitions=[
                {'AttributeName': 'transaction_id', 'AttributeType': 'S'}
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        logging.info(f"Table creation initiated: {response['TableDescription']}")
        
        # Wait for the table to exist
        waiter = dynamodb.get_waiter('table_exists')
        waiter.wait(TableName=table_name)
        logging.info(f"Table '{table_name}' created successfully.")
    
    except dynamodb.exceptions.ResourceInUseException:
        logging.error(f"Table '{table_name}' already exists.")
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")

# Call the function
create_dynamodb_table()

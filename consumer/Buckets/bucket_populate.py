import boto3
from kafka import KafkaConsumer
import json
import os
from dotenv import load_dotenv

load_dotenv('/Users/nikhilvarma/vsc/sales-data-anlysis/.env')

def write_to_bucket(data):
    s3 = boto3.client(
        's3',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
    )
    bucket_name = 'sales-transactions-bucket'
    object_key = f"transactions/2024/{data['transaction_id']}.json"
    
    s3.put_object(
        Body=json.dumps(data),
        Bucket=bucket_name,
        Key=object_key
    )

message = KafkaConsumer(
    'incoming-data-replication',
    bootstrap_servers=['localhost:9092'],
    group_id='incoming-data-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

for msg in message:
    data = msg.value
    write_to_bucket(data=data)

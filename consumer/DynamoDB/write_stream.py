import boto3
import os
from dotenv import load_dotenv
import json
from kafka import KafkaConsumer, KafkaProducer
from decimal import Decimal

load_dotenv()

# Custom JSON Encoder to handle Decimal types
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)  # Convert Decimal to float
        return super(DecimalEncoder, self).default(obj)

def write_stream_to_table(
      transaction_id,
      transaction_type,
      gender,
      city,
      state,
      coast,
      sale_amount
):
   # Convert sale_amount to Decimal if it's a float
   sale_amount = Decimal(str(sale_amount))  # Convert float to Decimal

   dynamodb  = boto3.resource(
        'dynamodb',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
        region_name=os.getenv('AWS_DEFUALT_REGION')
    )
   
   Item = {
            'transaction_id': transaction_id,
            'transaction_type': transaction_type,
            'gender': gender,
            'city': city,
            'state': state,
            'coast': coast,
            'sale_amount': sale_amount
        }
   
   table = dynamodb.Table('Sales-Transactions')
   table.put_item(Item = Item)
   trigger_replication(Item)

def trigger_replication(value):
   replication_producer = KafkaProducer(
      bootstrap_servers='localhost:9092',
      value_serializer=lambda v: json.dumps(v, cls=DecimalEncoder).encode('utf-8')  # Use custom encoder
   )
   replication_producer.send('incoming-data-replication', value=value)

message = KafkaConsumer(
   'incoming-data',
   bootstrap_servers=['localhost:9092'],
   group_id='incoming-data-group',
   value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

for msg in message:
   data = msg.value
   write_stream_to_table(
       transaction_id=data['transaction_id'],
       transaction_type=data['transaction_type'],
       gender=data['gender'],
       city=data['location']['city'],
       state=data['location']['state'],
       coast=data['location']['coast'],
       sale_amount=data['sale_amount']  # Ensure this is converted to Decimal
   )

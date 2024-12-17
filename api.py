import uuid
import random
from dataclasses import dataclass
from Locations import locations
import time
import datetime
import csv
from kafka import KafkaProducer
import json

@dataclass
class Transaction:
    transaction_id: str
    transaction_type: str
    location: dict  # categorized into city, state, and coast
    gender: str
    sale_amount: float


def transaction_generator() -> Transaction:
    gender = ['male', 'female', 'rather not say']
    sale = round(random.uniform(1.00, 100.00), 2)
    transaction_type = ['Credit', 'Debit', 'Cash', 'Refund_Credit', 'Gift_Card']
    transaction = Transaction(
        transaction_id=str(uuid.uuid4()),  # transaction ID
        transaction_type=random.choice(transaction_type),  # Random transaction type
        location=random.choice(locations),  # Choose random location
        gender=random.choice(gender),
        sale_amount=sale  # Choose a random sale amount
    )
    return transaction




def kafka_event_producer(transaction, producer):
    # Send the transaction data to Kafka
    producer.send('incoming-data', value=transaction.__dict__)
    producer.flush()


if __name__ == '__main__':
    # Initialize Kafka producer
    producer = KafkaProducer(
        bootstrap_servers='localhost:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    while True:
        transaction = transaction_generator()
        
        
        # Send to Kafka
        kafka_event_producer(transaction, producer)
        
        time.sleep(5)

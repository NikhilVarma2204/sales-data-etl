import boto3
import logging
import time
def run_crawler():

    client = boto3.client('glue')
    response = client.start_crawler(Name = 'Sales-Transactions-Crawler')
    logging.info(response)
    
run_crawler()
    

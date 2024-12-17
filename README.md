
# Real-Time Data Processing Pipeline

This project involves a real-time data generator that feeds data into a Kafka broker, which then sends it to DynamoDB. A separate Kafka topic is used to replicate the DynamoDB data into S3. A crawler is created to crawl the data and build a catalog. Finally, Athena is used to query the catalog.

<img width="1173" alt="image" src="https://github.com/user-attachments/assets/5e59421f-233b-4087-a712-d9114aaf2e52" />


## Overview

This pipeline allows for:

- Real-time data generation and processing with Kafka
- Data storage in DynamoDB and S3
- Automatic cataloging of the data using AWS Glue Crawler
- Querying the catalog using AWS Athena

## Architecture

1. **Real-Time Data Generator:** Simulates real-time data that is sent to a Kafka broker.
2. **Kafka Broker:** Manages two topics:
   - One sends the data to DynamoDB.
   - The other replicates the DynamoDB data to S3.
3. **AWS Glue Crawler:** Crawls the S3 data and builds a catalog.
4. **AWS Athena:** Queries the cataloged data in S3 for analytics.

## Technologies Used

- **Kafka:** For real-time data streaming.
- **DynamoDB:** NoSQL database for real-time data storage.
- **S3:** Cloud storage for data replication.
- **AWS Glue:** Crawler for creating a data catalog.
- **AWS Athena:** Serverless query service for querying data in S3.

## Setup and Installation

1. **Kafka Setup:**
   - Install Kafka and start the broker.
   - Create the necessary topics for data streaming and replication.

2. **DynamoDB Setup:**
   - Set up DynamoDB tables for storing the data.

3. **S3 Bucket:**
   - Create an S3 bucket for data replication.

4. **Glue Crawler:**
   - Set up the Glue Crawler to crawl the S3 bucket and create a data catalog.

5. **Athena:**
   - Set up Athena to query the catalog created by the Glue Crawler.

## How to Run

1. **Create DynamoDB Table**  
   Run the following command to create the necessary DynamoDB table for storing sales data:  
   ```bash
   python3 /consumer/DynamoDb/create_table.py
sql
Copy code

2. **Create S3 Bucket**  
   Run the following command to create an S3 bucket where data will be replicated:
   ```bash
   python3 /consumer/Bucket/create_bucket.py

sql
Copy code

3. **Start Kafka Producer**  
   Run the following command to start the Kafka producer, which will generate real-time data and send it to the Kafka broker:
   ```bash
   python3 api.py

markdown
Copy code

4. **Run Write Stream Consumer**  
   Run the following command to consume the events generated by `api.py` and push them into DynamoDB:
   ```bash
   python3 /consumer/write_stream.py

vbnet
Copy code

5. **Populate Bucket**  
   Run the following command to populate data into the S3 bucket after replication from DynamoDB:
   ```bash
   python3 /consumer/bucket_populate.py

css
Copy code

6. **Run AWS Glue Crawler**  
   Run the following command to start the AWS Glue Crawler. You can set a timer to run this automatically to update the data catalog in S3:
   ```bash
   python3 /crawler/create_crawler.py

graphql
Copy code

7. **Query Data in Athena**  
Once the Glue Crawler finishes its job, use AWS Athena to query the catalog and perform sales data analysis.

Example Athena query:
SELECT * FROM sales_2024 LIMIT 100;
## Queries in Athena

Once the data is cataloged, you can run SQL queries to analyze the data, for example:

```sql
SELECT * FROM sales_2024 LIMIT 100;


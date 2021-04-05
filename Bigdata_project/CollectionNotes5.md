# Section 5: Domain 4: Analysis

## 84. [Exercise] Kinesis Analytics, Part 1
### TRANSACTION RATE ALARMS

1. Create another Kinesis Data Stream

- Kinesis Stream Name: OrderRateAlarms
- Number of shards: 1

2. Create Kinesis Data Analitics

- Application Name: TransactionRateMonitor
- Description: whatever you like
- Runtime: SQL

**Connect Streaming data source:**

- Kinesis stream: CadabraOrders
- PRESS **schema descover** (you'll need to have some streaming data runing to kinesis data stream)

* Real time analytics

- pase the code in the SQL Editor.
- code: ./code/analytics-query.sql
- save and test if everything is working

**Connect to a destinaiton:**

- Kinesis Stream: OrderRateAlarms
- In-application stream name*: TRIGGER_COUNT_STREAM
- Everything else by default

3. Setup the lambda function

- create a Role for the lambda function
- Select create Role in the IAM and then choose lambda service
- Attach *AWSLambadaKinesisExecutionRole* policy to the lambda Role
- Attach *AmazonSNSFullAccess* policy to the lambda Role
- Attach *CloudWatchLogFullAccess* policy to the lambda Role
- Attach *AWSLambdaBasicExecutionRole* policy to the lambda Role
- Create the role

- Create the lamda
- Name of the function: TransactionRateAlarm
- Don't forget to choose the role while creating the lambda function

- Add kinesis as a trigger for the lambda function (select the OrderRateAlarms)
- Increase the lambda timeout to 1 minute
- Pase the code in the lamda console: ./code/lambda.py

4. Create an AWS SNS Topic

- Topic Name: CadabraAlarms
- Display name: Cadabra
- create a subscription for the topic
    - Protocol: SMS
    - Endpoint: your phone nomber
- Publish a message:
    - Subject: Test
    - Message format: Raw
    - Message: whatever you like
- copy the Topic ARN

5. Update lambda Function

- Paste the SNS Topic ARN

6. Make a test and clean everything





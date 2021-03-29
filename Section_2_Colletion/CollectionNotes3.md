# Section 2: Domain 1: Collection

## 48. [Exercise] DynamoDB

1. Build AWS DaynamoDB Table

- Name: CadabraOrders
- Partition Key: CustomerID | Type: Number
- Sort Key: OrderID | Type: String

2. Set up the consumer Scripts

Inside the t2.micro instace:
- $ sudo pip install boto3

- Setup AWS Credential in the t2.micro as you like

- $	wget http://media.sundog-soft.com/AWSBigData/Consumer.py
- $ chmod a+x Consumer.py
- $ ./Consumer.py

Run the Consumer.py script and also the LogGenerator.py script and see if we put new data into DynamoDB Table



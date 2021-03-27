# Section 2: Domain 1: Collection

## 14. [Exercise] Kinesis Firehose, Part 1

1. Setup Kinesis Data Firehose delivery stream
Name of the bucket: analytics-orderlogs
Name of the Kinesis Delivery stream: PurchaseLogs

## 15. [Exercise] Kinesis Firehose, Part 2

1. Launch an EC2 t2.micro

2. Install Kinesis Client Application
$ sudo yum install -y aws-kinesis-agent

3. Download files
$ wget http://media.sundog-soft.com/AWSBigData/LogGenerator.zip
$ unzip LogGenerator.zip

4. CHange permision to the unzip file
$ chmod a+x LogGenerator.py

5. Checkout the files
$ ls
$ less LogGenerator.py
$ less onlineRetail.csv

6. Create Log directory to put everything in
$ sudo mkdir /var/log/cadabra

7. Kinesis configuration
$ cd /etc/aws-kinesis/
$ ls -al
$ sudo nano agent.json

8. Create IAM Role for the t2.micro with necesary permision

- AdministratorAccess [NOT RECOMENDED!]



9. Modify agent.json 

See original code at /code/agent.json
See updated code at /code/updated_agent.json










x. Download the LogGenerator.py file to myself [OPTIONAL]

You will need to attach a Role with S3 access permision to the t2.micro instance

$ aws s3 cp LogGenerator.py s3://analytics-orderlogs/
download the file in my computer!
aws s3 cp s3://analytics-orderlogs/LogGenerator.py code/


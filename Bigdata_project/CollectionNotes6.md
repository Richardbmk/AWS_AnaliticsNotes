# Section 5: Domain 4: Analysis

## 88. [Exercise] Amazon Elasticsearch Service, Part 1

### NEAR-REAL-TIME LOG ANALYSIS

1. ssh into the t2.micro instance machine

2. Download http logs at:

   - $ wget http://media.sundog-soft.com/AWSBigData/httpd.zip
   - $ unzip httpd.zip

3. Checkout the file:

   - $ cd httpd
   - $ less ssl_access_log

4. Move the httpd files

- $ sudo mv httpd /var/log/httpd

5. Creation of an ElasticSearch Services

- Create new domain
- Choose deployment type: Developing and testing
- Version by default or 6.X

- Elasticsearch Domain Name: cadabra
- Everything else by default

- Network configuration:

  - VPC access (Recommended)
  - Public access (for the seek of easyness we choose these option)

- Change access policy:

  - Allow only our account number

- Review and confirm!

6. Create Firehose Delivery Stream

- Delivery Stream Name: WebLogs (Everythins else by default)
- Transform source records with AWS Lambda

  - Enable
  - Create and/or choose the function (kinesis-firehose-apachelog-to-json)

    - The function should transform Firehose data from Apache access logs to json format.
    - Name of the function: LogTransform
    - Timeout: 1 minute
    - function URL: https://github.com/amazon-archives/serverless-app-examples/blob/master/javascript/kinesis-firehose-syslog-to-json/index.js

- Choose destination: Elasticsearch Service
- Domain: cadabra
- Index: weblogs
- Index Rotation: Every day
- Retention duration: 300

- Backup mode: Failed records only
- Backup s3 bucket: analytics-orderlogs
- Backup s3 bucket prefix: es/

- Buffer intervals: 60 seconds

- Create a default IAM

7. kinesis Agent configuration

- $ sudo nano /etc/aws-kinesis/agent.json
- $ sudo service aws-kinesis-agent restart
- $ tail -f /var/log/aws-kinesis-agent/aws-kinesis-agent.log

8. Checkout ElasticSearch and see if is working

9. Preparing things for Kibana

- Modify the access policy adding this new file: /code/kibana-access.json
- open Kibana an see if is working

10. Kibana configuration setup

- Go to management and make some changes:

  - Create index parttern: weblogs\*
  - Timestamp: @timestamp
  - change the time range

- Learn and Play around with kibana

11. Clean everything to control the budget!

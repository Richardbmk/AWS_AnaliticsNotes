# Section 2: Domain 1: Collection

## 18. [Exercise] Kinesis Data Streams

1. Setup Kinesis Data Stream
- Kinesis Stream Name: CadabraOrders
- Number of shards: 1

2. Cofiguring Kinesis Agent in the t2.micro

- $ cd ~
- $ cd /etc/aws-kinesis/
- $ sudo nano agent.json

See updated code at /code/updated2_agent.json

make necessary changes and save: Ctrl + O and Ctrl + X

- $ sudo service aws-kinesis-agent restart
- $ cd ~
- $ sudo ./LogGenerator.py

- tail -f /var/log/aws-kinesis-agent/aws-kinesis-agent.log

go to the console and se if we have some changes!




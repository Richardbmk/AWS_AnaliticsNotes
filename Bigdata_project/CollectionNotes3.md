# Section 2: Domain 1: Collection

## 48. [Exercise] DynamoDB

1. Build AWS DaynamoDB Table

- Name: CadabraOrders
- Partition Key: CustomerID | Type: Number
- Sort Key: OrderID | Type: String

2. Set up the consumer Scripts

Inside the t2.micro instace:
- $ sudo yum install python3.7
- $ sudo yum install python-pip
- $ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
- $ sudo pip install boto3

3. Setup AWS Credential in the t2.micro as you like

create a IAM user with sample_Firehose_EC2Access.json


USING aws-vault (**I DON'T recomend it, a lot of errors!**)

- $ sudo yum install git-all
- $ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" (PRESS ENTER to continue!)
- Intrucction after install brew:
    - Add Homebrew to your PATH in /home/ec2-user/.bash_profile:
        - $ echo 'eval "$(/home/ec2-user/.linuxbrew/bin/brew shellenv)"' >> /home/ec2-user/.bash_profile
        - $ eval "$(/home/ec2-user/.linuxbrew/bin/brew shellenv)"
    - Run `brew help` to get started
    - $ sudo yum groupinstall 'Development Tools'
    - $ brew install gcc
- $ brew install aws-vault

- $ aws-vault --help
- $ aws-vault --version
- $ aws configure (put some random values)
- $ aws-vault add bigdataUser

USING AWS CREDENTIALS (SIMPLE WAY and work!)
- resource: https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html
- aws configure


- $	wget http://media.sundog-soft.com/AWSBigData/Consumer.py
- $ chmod a+x Consumer.py
- $ ./Consumer.py

Run the Consumer.py script and also the LogGenerator.py script and see if we put new data into DynamoDB Table





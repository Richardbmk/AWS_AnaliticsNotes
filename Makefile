AWS_REGION=us-west-2
TABLE_NAME=CadabraOrders
STREAM_NAME=CadabraOrders
INSTACE_IDS=i-05dd01f53b02d1bd2

create-dynamodb-table:
	aws dynamodb create-table --table-name $(TABLE_NAME) \
	 --attribute-definitions AttributeName=CustomerID,AttributeType=N AttributeName=OrderID,AttributeType=S \
	  --key-schema AttributeName=CustomerID,KeyType=HASH AttributeName=OrderID,KeyType=RANGE \
	   --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1 \
	    --region $(AWS_REGION)

delete-dynamodb-table:
	aws dynamodb delete-table \
	 --table-name $(TABLE_NAME)

create-kinesis-stream:
	aws kinesis create-stream \
	 --stream-name $(STREAM_NAME) \
	 --shard-count 1 \
	 --region $(AWS_REGION)

delete-kinesis-stream:
	aws kinesis delete-stream \
		--stream-name $(STREAM_NAME) \
		--region $(AWS_REGION)

stop-ec2-instances:
	aws ec2 stop-instances --instance-ids $(INSTACE_IDS)

start-ec2-instances:
	aws ec2 start-instances --instance-ids $(INSTACE_IDS)
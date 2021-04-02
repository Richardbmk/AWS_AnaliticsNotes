# Section 4: Domain 3: Processing

## 77. [Exercise] Elastic MapReduce, Part 1
### PRODUCT RECOMENDARION

1. Create a cluster with AWS EMR Service

- Name of the cluster: CadabraRecs
- Release: the last
- Applications: Spark: Spark..
- Instance type: m5.xlarge (Think of what is good for you case study)
- Number of Instaces: 3

2. Configure Security Group for Master

If you wanna ssh into your cluster you will need to enable in the Security Group of the cluster.

Find Master public DNS an ssh into your Master node!

- $ ssh -i "oregonKeypair.pem" hadoop@ec2-44-242-159-56.us-west-2.compute.amazonaws.com

3. Using EMR Recomendacion samples 
We are in m5.xlarge:

- $ cp /usr/lib/spark/examples/src/main/python/ml/als_axample.py ./
- $ ls
- $ nano als_example.py

- $ hadoop fs -mkdir -p /user/hadoop/data/mllib/als ==> this create a directory in HDFS that is share across the cluster
- $ hadoop fs -copyFromLocal /usr/lib/spark/data/mllib/als/sample_movielens_ratings.txt /user/hadoop/data/mllib/als/sample_movielens_ratings.txt ==> coping the needed file into HDFS for the cluster

- $ spark-submit als_example.py ==> run the spark script

4. Update the spark script

- $ nano als_example.py
after the if statement put:
spark.sparkContext.setLogLevel("ERROR")

- $ spark-submit als_example.py ==> run the spark script

Try to use google.colab to test this script!

5. Update again als_example.py

In this case we update the script to use our data

make the buck public (only for the cluster) so the cluster can access


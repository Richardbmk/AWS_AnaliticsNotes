# Section 5: Domain 4: Analysis

## 93. [Exercise] AWS Glue and Athena

### DATA WAREHOUSING & VISUALIZATION

1. Configuring AWS GLUE

- Add a crawler
- Crawler Name: order data
- Choose a data store: S3 bucket (analytics-orderlogs)
- Exclude patterns: es/\*\*
- create IAM role (default setting)
- Add a database. Name: orderlogs
- Run the Crawler

- Edit Schema
  - Edit the column Name of the csv by hand

2. Playing with AWS Athena

test query:
./code/test-query.sql

## 103. [Exercise] Redshift Spectrum, Pt. 1

1. Creation of a cheap (DC2) Readshift cluster

- Choose DC2 Cluster
- Nodes: 1
- Cluster identifier: cadabra
- Create a Role for the cluster
  - Go to IAM and create Role
  - Select Redshift
  - Select Permisions:
    - AmazonS3ReadOnlyAccess
    - AWSGlueConsoleFullAccess
  - Name of Role: RedshiftSpectrum (whatever you like)
- Everything as you like or by default

2. Connect to you Redshift database

3. Create an external schema from Glue data catalog

checkout the video this is getting complicated here

## 110. [Exercise] Amazon Quicksight

- Just play around if you like, this is not important for now

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

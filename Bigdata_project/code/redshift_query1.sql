CREATE external schema orderlog_schema FROM data catalog
database 'orderlogs'
iam_role 'arn:aws:iam:account_id:role/RedshiftSpectrum'
region 'your_region_here'
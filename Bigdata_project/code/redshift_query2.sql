SELECT description, COUNT(*) FROM orderlog_schema.name_of_your_table WHERE country='France' AND year='2019' AND month='02' GROUP BY description

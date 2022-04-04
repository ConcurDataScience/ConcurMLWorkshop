# Below are awsscli commands that you will execute one by one to delete the required resources.

# Day 2 Part 1
# Delete 	Glue Table, DB, Crawler, Trigger(if created), Job(if created)
! aws glue delete-table --database-name {database_name} --name {table_name}
! aws glue delete-database --name {database_name}
! aws glue delete-crawler --name {crawler_name}
! aws glue delete-trigger --name {trigger_name}
! aws glue delete-job --job-name {job_name}

# Day 2 Part 2



# Day 3 Part 1



# Day 3 Part 2


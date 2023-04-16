import csv
import logging

from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.providers.amazon.aws.hooks.s3 import S3Hook

def postgres_task(ds):
        
    # CREATE A CONNECTION WITH THE DATABASE AND RUN THE SELECT QUERY
    hook = PostgresHook(postgres_conn_id="postgres_localhost")
    conn = hook.get_conn()
    cursor = conn.cursor()
    cursor.execute("select * from all_orders where date = %s", (ds,))
    rows = cursor.fetchall()  # Fetch all rows from the cursor
    
    # CREATE A .CSV FILE TO STORE THE ORDERS
    with open(f"dags/get_orders_{ds}.csv", "w", newline="") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow([i[0] for i in cursor.description])
        csv_writer.writerows(rows)

    cursor.close()
    conn.close()

    logging.info("Saved orders data in CSV file: %s", f"get_orders_{ds}.csv")

def raw_data_to_S3(ds):
        
    # CREATE A CONNECTION WITH THE DATA LAKE AND UPLOAD THE FILE TO S3
    s3_hook = S3Hook(aws_conn_id = "s3_conn")
    s3_hook.load_file(
        filename= f"dags/get_orders_{ds}.csv",
        key = f"orders/{ds}.csv",
        bucket_name = "etl-portfolio",
        replace = True
    )

    logging.info("File %s uploaded to S3 bucket etl-portfolio", f"get_orders_{ds}.csv")
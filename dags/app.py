from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

from utils.python_function import postgres_task, raw_data_to_S3

default_args = {
    'owner':'leonardohss0',
    'retries':5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id = 'etl-portfolio',
    description = 'Extracting data from Postgresql nad then inserting raw data in S3',
    start_date = datetime(2023,1,1),
    schedule_interval= '@daily',
    default_args= default_args
) as dag:

    postgresTask = PythonOperator(
        task_id = 'postgres_task',
        python_callable= postgres_task
    )

    rawDataToS3 = PythonOperator(
        task_id = 'raw_data_to_S3',
        python_callable= raw_data_to_S3
    )

    postgresTask >> rawDataToS3
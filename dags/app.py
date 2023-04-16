from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.providers.amazon.aws.operators.glue import GlueJobOperator
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

    # Define an PythonOperator to extract data from a Postgresql
    postgresTask = PythonOperator(
        task_id = 'postgres_task',
        python_callable= postgres_task
    )

    # Define an PythonOperator to push data to a AWS S3 bucket
    rawDataToS3 = PythonOperator(
        task_id = 'raw_data_to_S3',
        python_callable= raw_data_to_S3
    )

    # Define an GlueJobOperator to run the AWS Glue job
    glueTask = GlueJobOperator(
        task_id='glue_task',
        job_name='Transforming Data',  
        aws_conn_id='s3_conn', 
        iam_role_name='AWSGlueServiceRole-AnalyticsGlue',
        script_location='s3://aws-glue-assets-864500937691-us-east-1/scripts/',
        region_name= 'us-east-1'
    )

    finish = BashOperator(
        task_id="finish",
        bash_command="echo The job is finished",
    )

    postgresTask >> rawDataToS3 >> glueTask >> finish
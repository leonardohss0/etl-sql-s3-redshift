# Using Airflow to push data from S3 bucket and run a job from AWS Glue to transform and clean the data. 
Keywords: Python, Airflow, AWS, S3, Redshift, Glue, ETL, Postgresql and Docker

### Description
This project utilizes Apache Airflow, Docker, AWS Glue, and AWS S3 to automate the extraction, transformation, and loading (ETL) process for data stored in a local PostgreSQL database to AWS S3 in both raw and processed formats.

The ETL process is orchestrated using Apache Airflow, a powerful and flexible open-source platform for creating, scheduling, and managing complex workflows. Docker is used to containerize the Airflow environment, making it easy to deploy and run consistently across different environments.

### The project involves several steps:

1. **Extract**: Data is extracted from a local PostgreSQL database using connections defined in Apache Airflow. The extracted data is then stored in AWS S3 in a raw data schema.

2. **Transform and Load**: Apache Airflow is used to trigger an AWS Glue job, which performs data transformation and cleaning tasks on the extracted data in AWS S3. The processed data is then stored in another S3 schema in Parquet format, which is a columnar storage format optimized for large-scale data processing.

3. **Automation**: The entire ETL process is automated using Apache Airflow, which allows for scheduling, monitoring, and managing the workflows.

## Prerequisites
Before running the project, you need to have the following tools and services installed and configured:

* Docker: To containerize and run the Apache Airflow environment.
* AWS Account: To use AWS Glue and S3 services.
* PostgreSQL: To have a local PostgreSQL database with the data to be extracted.

## Setup
Follow the steps below to set up and run the project:

1. Clone the repository to your local machine:
git clone <repository-url>
 
2. Build and run the Docker container for Apache Airflow:
cd <repository-folder>
docker-compose up -d
  
3. Access the Apache Airflow UI by navigating to http://localhost:8080 in your web browser. Use the default credentials (username: airflow, password: airflow) to log in.

4. Define the PostgreSQL connection in Apache Airflow by going to the "Admin" menu in the UI, selecting "Connections", and adding a new connection with the details of your local PostgreSQL database.

5. Create the AWS S3 connection in Apache Airflow by going to the "Admin" menu in the UI, selecting "Connections", and adding a new connection with the credentials of your AWS S3 account.

6. Create the AWS Glue job in your AWS account to perform the data transformation and cleaning tasks. Note the name of the job and the location of the script file in S3.

7. Define the AWS Glue connection in Apache Airflow by going to the "Admin" menu in the UI, selecting "Connections", and adding a new connection with the details of your AWS Glue job.

8. Update the DAGs in the dags/ folder with the appropriate details, such as the name of the PostgreSQL connection, the AWS S3 connection, and the AWS Glue job name and script location.

9. Trigger the DAG in Apache Airflow to start the ETL process. You can monitor the progress and view logs in the Apache Airflow UI.

## Folder Structure
The project follows the following folder structure:
 
etl-sql-s3-redshift/ <br>
├── dags/ <br>
├── logs/ <br>
├── plugins/ <br>
├── db/ <br>
├── docker-compose.yml <br>
├── Dockerfile<br>
├── requirements.txt<br>
└── README.md<br>

## Usage
To use this project, follow the steps mentioned in the "Setup" section to configure the necessary connections, update the DAGs with your specific details, and trigger the DAG in Apache Airflow to start the ETL process.

You can also customize the DAGs and scripts according to your specific requirements. For example, you can modify the data transformation logic in the transform_data.py script, add more DAGs to perform additional data processing tasks, or configure the scheduling of DAGs as per your desired frequency.

## Contributing
If you would like to contribute to this project, please follow standard open-source contribution practices, such as forking the repository, creating a branch, making changes, and submitting a pull request. Make sure to provide detailed information about the changes made and any relevant documentation updates.

## License
This project is released under the MIT License, which allows for free usage, modification, and distribution of the code, with proper attribution. However, please review the license file for the full terms and conditions.

## Contact
For any questions, suggestions, or issues related to this project, please feel free to contact the project maintainer at contato.leonardohss@gmail.com.

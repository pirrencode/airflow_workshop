#!/bin/bash

# Set project name
PROJECT_NAME="project"

# Create project directory
mkdir -p $PROJECT_NAME
cd $PROJECT_NAME || exit

# Create Dockerfile
echo "# Dockerfile for Apache Airflow" > Dockerfile

echo "FROM apache/airflow:2.7.1

# Set environment variables
ENV AIRFLOW_HOME=/opt/airflow

# Copy custom DAGs, plugins, and requirements
COPY dags/ \${AIRFLOW_HOME}/dags/
COPY plugins/ \${AIRFLOW_HOME}/plugins/
COPY requirements.txt \${AIRFLOW_HOME}/requirements.txt

# Set default command
CMD [\"airflow\", \"standalone\"]" >> Dockerfile

# Create dags directory and example DAG
mkdir -p dags
echo "from airflow import DAG
from airflow.operators.dummy import DummyOperator
from datetime import datetime

with DAG(
    'example_dag',
    default_args={'start_date': datetime(2023, 1, 1)},
    schedule_interval=None,
    catchup=False,
) as dag:
    start = DummyOperator(task_id='start')" > dags/example_dag.py

mkdir -p plugins
echo "# Example plugin file" > plugins/example_plugin.py

echo "# Add Python dependencies here, e.g.:
pandas
requests" > requirements.txt

echo "Project structure created successfully."


# Dockerfile for Apache Airflow
FROM apache/airflow:2.7.1

# Set environment variables
ENV AIRFLOW_HOME=/opt/airflow

# Copy custom DAGs, plugins, and requirements
COPY dags/ ${AIRFLOW_HOME}/dags/
COPY plugins/ ${AIRFLOW_HOME}/plugins/
COPY requirements.txt ${AIRFLOW_HOME}/requirements.txt

# Set default command
CMD ["airflow", "standalone"]

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

# Define task functions
def extract_booking_data():
    print("Extracting booking data from external systems...")

def update_availability():
    print("Updating room availability across platforms...")

def notify_guests():
    print("Sending notifications to guests about upcoming bookings...")

def generate_business_report():
    print("Generating daily business performance report...")

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
with DAG(
    'hospitality_management_workflow',
    default_args=default_args,
    description='A DAG for managing hospitality platform operations',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=['hospitality', 'platform_management', 'example'],
) as dag:

    # Define tasks
    task_extract_booking_data = PythonOperator(
        task_id='extract_booking_data',
        python_callable=extract_booking_data,
    )

    task_update_availability = PythonOperator(
        task_id='update_availability',
        python_callable=update_availability,
    )

    task_notify_guests = PythonOperator(
        task_id='notify_guests',
        python_callable=notify_guests,
    )

    task_generate_business_report = PythonOperator(
        task_id='generate_business_report',
        python_callable=generate_business_report,
    )

    # Define task dependencies
    task_extract_booking_data >> task_update_availability >> task_notify_guests >> task_generate_business_report

from airflow import DAG
from airflow.operators.dummy import DummyOperator
from datetime import datetime

with DAG(
    'example_dag',
    default_args={'start_date': datetime(2023, 1, 1)},
    schedule_interval=None,
    catchup=False,
) as dag:
    start = DummyOperator(task_id='start')

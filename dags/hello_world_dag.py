from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

def say_hello():
    print("Hello from your first DAG!")

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

with DAG(
    dag_id='hello_world_dag',
    default_args=default_args,
    description='A simple hello world DAG',
    schedule='@daily',
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=['example'],
) as dag:

    task_hello = PythonOperator(
        task_id='say_hello',
        python_callable=say_hello,
    )

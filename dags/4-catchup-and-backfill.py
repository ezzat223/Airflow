from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'Ezzat',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

# ------------------ DAG ------------------ #
with DAG(
    dag_id='dag_with_catchup_and_backfill_v01',
    default_args=default_args,
    # set it to a Previous date
    start_date=datetime(2024, 9, 27),
    schedule_interval='@daily',
    catchup=True
) as dag:
    task1 = BashOperator(
        task_id='task1',
        bash_command="echo 'Hello world, from catchup and backfill!'"
    )
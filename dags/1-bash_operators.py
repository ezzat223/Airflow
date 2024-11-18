from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'Ezzat',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='first_dag_v5',
    default_args=default_args,
    description='This is the first dag i write',
    # Year/Month/Day/Hour
    start_date=datetime(2024, 10, 27, 2),
    schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command="echo 'Hello world, this is the first task!'"
    )
    task2 = BashOperator(
        task_id='second_task',
        bash_command="echo 'Hey, iam task2 and will run after task1'"
    )
    task3 = BashOperator(
        task_id='third_task',
        bash_command="echo 'Hey, iam task2 and will run in the same time with task2'"
    )
    
    # ----------- method 1 ----------- #
    # make task2 run after task1
    # task1.set_downstream(task2)
    # make task3 run in the same time with task2
    # task1.set_downstream(task3)
    
    # ----------- method 2 ----------- #
    # using bit shift operator
    # task1 >> task2 
    # task1 >> task3
    
    # ----------- method 3 ----------- #
    task1 >> [task2, task3]
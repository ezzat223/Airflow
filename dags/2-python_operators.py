from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator




# The Python functions to be used as a DAG Operator
def greet():
    print("Hello world from Python Operator...")

def greet_name(name: str, age: int):
    print(f"Hello, my name is {name}, and iam {age} yeas old.")

# Go to Admin -> XComs to find the returned values (ti => task instance)
def get_name(ti) -> str:
    ti.xcom_push(key='first_name', value='Jerry')
    ti.xcom_push(key='last_name', value='Fridman')


# input from above task
def greet_from_task(ti, age):
    first_name = ti.xcom_pull(task_ids='get_name', key='first_name')
    last_name = ti.xcom_pull(task_ids='get_name', key='last_name')
    print(f"Hello, my first name is {first_name}, and last name is {last_name}, and iam {age} years old.")


default_args = {
    'owner': 'Ezzat',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

# ---------------- DAG ---------------- #
with DAG(
    dag_id='first_python_operator_dag_v5',
    default_args=default_args,
    description='This is the first dag using Python Operator',
    # Year/Month/Day/Hour
    start_date=datetime(2024, 10, 27, 2),
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet
    )
    task2 = PythonOperator(
        task_id='greet_name',
        python_callable=greet_name,
        # to pass args
        op_kwargs={
            'name': 'Ezzat',
            'age': 23
        }
    )
    task3 = PythonOperator(
        task_id='get_name',
        python_callable=get_name
    )
    task4 = PythonOperator(
        task_id='greet_from_task',
        python_callable=greet_from_task,
        op_kwargs={
            'age': 23
        }
    )
    task1 >> [task2, task3]
    task3 >> [task4]
from airflow import DAG 
from airflow.decorators import dag, task
from datetime import datetime, timedelta


default_args = {
    'owner': 'Ezzat',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

# ---------------- DAG ---------------- #
dag = DAG(
    dag_id='dag_with_taskflow_api_v02',
    default_args=default_args,
    start_date=datetime(2024, 11, 17, 2),
    schedule_interval='@daily'
)
def hello_world_etl():
    # task1
    @task(multiple_outputs=True)
    def get_name():
        return {
            'first_name': 'Jerry',
            'last_name': 'Fridman'
        }
    
    # task2
    @task 
    def get_age():
        return 19
    
    # task3
    @task
    def greet(first_name, last_name, age):
        print(f"Hello world, my first name is {first_name}, my second name is {last_name} and iam {age} years old.")
    
    name_dict = get_name()
    age = get_age()
    greet(
        first_name=name_dict['first_name'],
        last_name=name_dict['last_name'],
        age=age
    )

@task 
def print_load():
    print(f"Data loaded successfully...")

with dag:
    # load_task = load(validate(transform(extract())))
    load_task = hello_world_etl()
    print_task = print_load()
    
    # snowflake_task = SnowflakeOperator(
    #     task_id='snowflake_task',
    #     sql='SELECT 1',
    #     snowflake_conn_id='snowflake_conn'
    # )
    
    load_task >> print_task

# create instance
# greet_dag = hello_world_etl()
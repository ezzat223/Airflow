from airflow import DAG 
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.operators.email import EmailOperator
from datetime import datetime, timedelta
import requests

def print_welcome():
    print("Welcome to AirFlow!")

def print_date():
    print(f"Today is {datetime.today().date()}")

def print_random_quote():
    response = requests.get("https://api.quotable.io/random")
    quote = response.json()['content']
    print(f"Quote of the day: {quote}")

dag = DAG(
    'Welcome_dag',
    # year/month/day
    start_date=datetime(2024, 11, 17),
    # end_date=
    default_args={'retries': 2, 'retry_delay': timedelta(minutes=5)},
    schedule_interval='0 23 * * *',
    catchup=False
)

print_welcome_task = PythonOperator(
    task_id='print_welcome',
    python_callable=print_welcome,
    dag=dag
)

print_date_task = PythonOperator(
    task_id='print_date',
    python_callable=print_date,
    dag=dag
)

# print_random_quote_task = PythonOperator(
#     task_id='print_random_quote',
#     python_callable=print_random_quote,
#     dag=dag
# )

# email
send_email_task = EmailOperator(
    task_id='send_email',
    to="{{ var.value.get('support_email') }}",
    subject='Test email operator',
    html_content='EmailOperator is working successfully',
    dag=dag
)

print_welcome_task >> print_date_task >> send_email_task
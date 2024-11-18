from airflow import DAG 
from airflow.utils.dates import days_ago
# needs to be installed: >
from airflow.providers.github.operators.github import GithubOperator
from airflow.operators.dummy import DummyOperator 
import logging 



dag = DAG(
    'git_repo_dag',
    default_args={'start_date': days_ago(1)},
    schedule_interval='0 23 * * *',
    catchup=False
)

# start dummy operator
start = DummyOperator(task_id='start', dag=dag)

# list git repos tags
list_repo_tags = GithubOperator(
    task_id='list_repo_tags',
    github_method='get_repo',
    github_method_args={"full_name_or_id": "ezzat223"},
    result_processor=lambda repo: logging.info(list(repo.get_tage())),
    dag=dag 
)

# end dummy operator
end = DummyOperator(task_id='end', dag=dag)
- Run in a Docker container "https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html":
>curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.10.2/docker-compose.yaml'

## In docker-compose.yaml
- AIRFLOW__CORE__EXECUTOR: CeleryExecutor => AIRFLOW__CORE__EXECUTOR: 
- Remove AIRFLOW__CELERY__RESULT_BACKEND `AND` AIRFLOW__CELERY__BROKER_URL
- Delete redis from services and from 
depends_on:
    &airflow-common-depends-on
    redis:
      condition: service_healthy

- From services delete airflow-worker and flower

- In environment => AIRFLOW__CORE__LOAD_EXAMPLES => Make it false

## Run the Container
- Now use the command:
>mkdir -p ./dags ./logs ./plugins ./config

- Use this if you're on linux only
echo -e "AIRFLOW_UID=$(id -u)" > .env

- You need to run database migrations and create the first user account (Init Airflow):
>docker compose up airflow-init

- Now run airflow (the one used everytime):
>docker-compose up -d --build

- Now you can find it on: "http://localhost:8080"
    Username and Password are both `airflow`

- To close containers and remove Volumes:
>docker-compose down -v

## Create a DAG
- It's a Python file under the dags directory
- You will automatically find it in the Web Server when you refresh




## Set-up a Virtual Environment
>python -m venv .venv
>source .venv/bin/activate
>pip install --upgrade pip setuptools wheel
>pip install apache-airflow

>AIRFLOW_VERSION=2.10.2
>PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"
>CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

>pip install "apache-airflow[celery]==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

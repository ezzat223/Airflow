FROM apache/airflow:2.10.2

USER root 

RUN apt-get update && \
    apt-get -y install git && \
    apt-get clean

USER airflow

# Install provider packages from requirements.txt (eg: github operator)
COPY requirements.txt /tmp/requirements.txt 
RUN pip install -r /tmp/requirements.txt
# Admin => Connections
# connection is is just some unique id to be used here
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator


load_table = SnowflakeOperator(
    task_id='load_table',
    # a file located in sqls to be executed
    sql='./sqls/profit_uk.sql',
    snowflake_conn_id='snowflake_conn_id',
    # dag=dag
)
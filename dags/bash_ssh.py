from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.contrib.operators.ssh_execute_operator import SSHExecuteOperator
from datetime import datetime, timedelta
from airflow.contrib.hooks import SSHHook
sshHook = SSHHook(conn_id='server_ssh')
import airflow

default_args = {
    'owner': 'airflow',
    'schedule_interval':'@once',
    'start_date': airflow.utils.dates.days_ago(2)
}

dag = DAG('bash_ssh', default_args=default_args)

t1 = SSHExecuteOperator(
    task_id="task1",
    bash_command='echo hello >> /tmp/hello.txt',
    ssh_hook=sshHook,
    dag=dag)



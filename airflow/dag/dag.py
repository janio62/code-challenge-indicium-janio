from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

# Define default arguments
default_args = {
   'owner': 'Jânio César Martins Ferreira',
   'depends_on_past': False,
   'start_date': days_ago(2),
   'retries': 1,
}

# Define the DAG
with DAG(
   'DAG-indicium',
   schedule_interval=timedelta(days=1),
   default_args=default_args
) as dag:

   # Define tasks
   t1 = BashOperator(
       task_id='obj1',
       bash_command="""
       cd $AIRFLOW_HOME/dag/tasks/
       python3 task1.py {{ execution_date }}
       """
   )
   
   t2 = BashOperator(
       task_id='obj2',
       bash_command="""
       cd $AIRFLOW_HOME/dag/tasks/
       python3 task2.py {{ execution_date }}
       """
   )

   t3 = BashOperator(
       task_id='obj3',
       bash_command="""
       cd $AIRFLOW_HOME/dag/tasks/
       python3 task3.py {{ execution_date }}
       """
   )


from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator


def read_data_task():
    import sys
    
    sys.path.append('/django-rest/us_nrc/airflow/dags/models.py')
    from models import Report_data, reactor_unit
    with open('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/powerreactorstatusforlast365days.txt') as f:
        report_data = f.readlines()[1:-1]
        for line in report_data:
            data_lst = line.split('|')
            r_id = reactor_unit.objects.all().filter(PlantName=data_lst[1]).first()
            date_details = data_lst[0].split(' ')
            date = datetime.datetime.strptime(date_details[0],"%m/%d/%Y").date()
            time = date_details[1]
            period = date_details[2]
            b =  Report_data(reactor=r_id, ReportDt = date, ReportTime = time, ReportPeriod = period,Unit = data_lst[1],Power = data_lst[2])
            b.save()
            
with DAG(
    dag_id="read_data_dag",
    schedule_interval="@daily",
    default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 9, 29),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    },
    catchup = False
) as read_data:
    read_data_task = PythonOperator(
        task_id = "read_data_task",
        python_callable=read_data_task,  
    )
    




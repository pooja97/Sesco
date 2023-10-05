import os

REACTOR_API = os.getenv("REACTOR_API", "https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/powerreactorstatusforlast365days.txt")
CSV_FILE_DIR = os.getenv("CSV_FILE_DIR", "/django-rest/airflow/dags/datasets")

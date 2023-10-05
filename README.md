# Django Rest API | API using Django Rest Framework

## Introduction

Created an API using Django rest framework with multiple API endpoints to extract reactor and outage details

## Technologies Used
Programming Language:<br>
    python3<br>

Frameworks:<br>
    1. Django<br>
    2. Django rest framework
    
## Dataset Used

Nuclear reactor details: https://www.nrc.gov/reactors/operating/list-power-reactor-units.html
Reactor Report details: https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/powerreactorstatusforlast365days.txt

## Steps to run

1. Clone this repository in a folder using 
```git clone https://github.com/pooja97/django-rest.git```

2. Change the directory to the folder and install a virtual environment for project dependencies 
``` python3 -m venv env ```

3. Activate virtual environment 
``` source env/bin/activate ```

4. Install project dependencies 
``` pip3 install -r requirements.txt ```

5. Change the directory to the project folder 
``` cd Sesco ```

6. To run the project use 
``` python manage.py runserver ```

To view the API endpoints: <br><br>
    1. To view the last outage date of a reactor: visit - http://127.0.0.1:8000/outage_date_search/ <br><br>
    Enter the reactor name in the content space like below <br> <br>
            {
            "reactor":"Arkansas Nuclear 1"
            } <br> <br>
    2. To view the reactors on outage between a particular date range: visit - http://127.0.0.1:8000/date_range_search/ <br><br>
    Enter the date range in the content space like below <br>
        {
        "start_date":"09/18/2023",
        "end_date":"09/22/2023"
        } <br> <br>
    3. To view the reactor's list based on the state name. visit: http://127.0.0.1:8000/state_search/ <br><br>
        Use the filter option to enter the state name. For instance: CA for California <br> <br>
    4. To view the reactor details based on the PlantName. visit: http://127.0.0.1:8000/reactor_search/ <br>
        Use the filter option to enter the Plant Name. 
    


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
``` cd django-rest ```

6. To run the project use 
``` python manage.py runserver ```
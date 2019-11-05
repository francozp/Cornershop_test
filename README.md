# Cornershop's Backend Test
## Description
Django Project developed for "Cornershop's Backend Test", wich consist in a meal delivery system, where a admin user (Nora) should be able to create and edit a menu and send Slack reminders to all chilean employes. The other users (employees) should be able to choose their preferred meal and specify customizations.

## Requirements .txt
This file includes all the modules that are neccesary for the execution of the project. Packages can be installed using the following command: pip install -r requirements.txt

## Database
Local MySql DB is used in this project. The sql file to create the database is included.

## Bootstrap Theme
The Bootstrap theme can be acquired at https://startbootstrap.com/themes/sb-admin-2/

## Celery
Erlang and RabbitMQ (broker) must be installed to make it work. 
Windows: Instalation guide can be found in https://www.rabbitmq.com/install-windows.html
Ubuntu: Install using: apt-get install -y erlang and apt-get install rabbitmq-server

To execute celery : celery worker -A csweb.celery --loglevel=info --pool=solo -l info
Start the RabbitMQ service

pip install mysqlclient-1.4.4-cp37-cp37m-win32.whl
run the rabbitmq server
celery worker -A csweb.celery -l info -P gevent
python manage.py runserver 192.168.0.45:8000 --insecure
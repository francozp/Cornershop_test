# Cornershop's Backend Test
## Description
Django Project developed for "Cornershop's Backend Test", which consists of a meal delivery system, where an admin user (Nora) should be able to create and edit a menu and also send Slack reminders to all chilean employees. The other users (employees) should be able to choose their preferred meal and specify customizations.

## Setup
### Installing python 3.7.4
1. The very first step is to install python 3.7.4. To do it, go to this page <https://www.python.org/downloads/release/python-374/> and download the file that match your system specifications.
2. Install python following the instructions. 
### Installing the python libraries
1. Open a terminal (Command Promp on Windows)
2. cd to the directory where requirements.txt is located
3. Install required libraries using `pip install -r requirements.txt` in the terminal.
> Note 1: If you have problems installing the mysqlclient library, you can use the Wheel file (.whl) that is in the directory, which can be installed using `pip install mysqlclient-1.4.4-cp37-cp37m-win32.whl`.
> Note 2: My recommendation is to install all the packages in a virtual environment. Official documentation: <https://docs.python.org/3/library/venv.html>
### Installing RabbitMQ
To send the slack reminders asicronically, Celery needs a broker to process the tasks. RabbitMQ provides this function, so we must install.
Windows: Instalation guide can be found in https://www.rabbitmq.com/install-windows.html
Ubuntu: Install using: apt-get install -y erlang and apt-get install rabbitmq-server
### Installing XAMPP
The database used in this proyect is local and XAMPP serves as the local test server. Download link: <https://www.apachefriends.org/es/download.html>
1. Follow the instructions to install XAMPP
2. When it's done, open (xampp-control.exe) it and start the Apache and MySQL services. 
3. When is all running (green), press the admin button of the MySQL service
4. A web page should have been opened: PhpMyAdmin
5. Select the import option and then browse your computer looking for the sql file included in this project "cornershop_test.sql"
6. Press the GO button
7. Now the database should be ready :)









## Bootstrap Theme
The Bootstrap theme can be acquired at https://startbootstrap.com/themes/sb-admin-2/


To execute celery : celery worker -A csweb.celery --loglevel=info --pool=solo -l info
Start the RabbitMQ service

pip install mysqlclient-1.4.4-cp37-cp37m-win32.whl
run the rabbitmq server
celery worker -A csweb.celery -l info -P gevent
python manage.py runserver 192.168.0.45:8000 --insecure
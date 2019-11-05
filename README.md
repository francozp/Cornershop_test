# Cornershop's Backend Test
## Description
Django Project developed for "Cornershop's Backend Test", which consists of a meal delivery system, where an admin user (Nora) should be able to create and edit a menu and also send Slack reminders to all chilean employees. The other users (employees) should be able to choose their preferred meal and specify customizations.

## !Important
I've decided to use the user management included in Django. I've decided to do this because i want to reutilize the code that exist and extend the actual user model with a profile model. **Osvaldo Mena have authorized this**.

## Setup
### Installing python 3.7.4
1. The very first step is to install python 3.7.4 32 bits. To do it, go to this page <https://www.python.org/downloads/release/python-374/> and download the file that match your system specifications.
2. Install python following the instructions. 
### Installing the python libraries
1. Open a terminal (Command Promp on Windows)
2. cd to the directory where requirements.txt is located
3. Install required libraries using `pip install -r requirements.txt` in the terminal.
4. Install gevent using `pip install gevent`
> Note 1: If you have problems installing the mysqlclient library, you can use the Wheel file (.whl) that is in the directory, which can be installed using `pip install mysqlclient-1.4.4-cp37-cp37m-win32.whl`. Then, go back to the step 3.

> Note 2: My recommendation is to install all the packages in a virtual environment. Official documentation: <https://docs.python.org/3/library/venv.html>
### Installing RabbitMQ
To send the slack reminders asicronically, Celery needs a broker to process the tasks. RabbitMQ provides this function, so we must install it.
Windows: Instalation guide can be found in https://www.rabbitmq.com/install-windows.html
Ubuntu: Install using: apt-get install -y erlang and apt-get install rabbitmq-server
### Installing XAMPP
The database used in this proyect is local and XAMPP serves as the local test server. Download link: <https://www.apachefriends.org/es/download.html>
1. Follow the instructions to install XAMPP
2. When it's done, open (xampp-control.exe) it and start the Apache and MySQL services. 
3. When is all running (green), press the admin button of the MySQL service
4. A web page should have been opened: PhpMyAdmin
5. Create a new DB named = 'cornershop_test'
6. Select the created database and then choose the import option and then browse your computer looking for the sql file included in this project "cornershop_test.sql"
7. Press the GO button
8. Now the database should be ready :)

## How to start the Meal Delivery system
We need 3 services running before starting the django project.
1. Run XAMPP and start MySQL and Apache services.
2. Start RabbitMQ service
Then, we can start the project. To this, we have to run the following commands on the main folder of the project (where the file manage.py is)
3. Open a terminal
4. Start your venv if you have created one
5. cd to the directory where manage.py is located
6. Run:  `python manage.py runserver <ipv4>:8000 --insecure`
7. Then run in other terminal, same directory: `celery worker -A csweb.celery -l info -P gevent`
8. Go to the url shown in the terminal. Should be something like http://192.168.0.45:8000/
9. You are now in the Meal Delivery system web page :D
> Note 1: ipv4 is your local ip. You can get it in the terminal, running `ipconfig`, then look for the ipv4 ip.

> Note 2: --insecure flag is used because the DEBUG flag is false. Then, to use static files, we shoul use insecure. I decided to put DEBUG=False because i have troubles with celery and i discover that this change fixes the problem.

> Note 3: gevent fixes compatibility problems between celery and windows 10

## How to use
This system has multiple fuctions, all of which where specified in the description.
In this system exists two types of users: with privileges or without privileges. Depending on this, the user have access to different views.

Now exists only one user: Nora. To login use the following
> user: nora , Password: testmd

### System functions
1. "Elegir Almuerzo": Here the users can choose what they want to eat at lunch (until 11AM CLT), also they can specify any customizations.
2. "Crear Menu": Here the users with privileges can create a menu for any incoming day with many options (an option considers: main dish, salad and the dessert). Also, user can create new main dishes.
3. "Ver Menús y editar": Here users with privileges can see all the created menus. Also, they can edit a specific menu, changing or deleting the options or adding new ones.
4. "Opciones de usuarios": Here, users with privileges can see all the options picked by the users. This includes the date, main dish, salad, dessert and customizations.
5. "Crear usuario": User with privileges can create new users. The users can be created with or without privileges. (usernames are unique)

## Testing
For the system testing, i use the unittest library. I've build 33 tests that verify the good performance of the View, Forms and URLS.
To **run** the test:
1. Open a terminal
2. cd to the directory where manage.py is located
3. Run `python manage.py test csweb` 

## Extras

# Bootstrap Theme
The Bootstrap theme can be acquired at https://startbootstrap.com/themes/sb-admin-2/

# email
Sending e-mails app using django, api, rest framework, celery, postgresql, etc.

STEPS:
1.  Install Python3
2.  Install Git
3.  Install Postgresql and create a database named for instance emaildb
4.  In a terminal create and go into the email-app folder, install and create a virtual environment (recommended), by commands in a terminal:
    - mkdir email-app
    - cd email-app
    - pip install virtualenv
    - virtualenv venv
    - venv\Scripts\activate (for Windows), or: source venv/bin/activate (for Linux {Ubuntu})      
5.  Download the email app from the github repository to the email-app folder
6.  In file .env change <username>, <password> and <db_name> filling your own username, passowrd and database name just created (step 3.), save the file
7.  Install Redis and start a broker's server
    - for Windows:
      - extract Redis-x64-3.2.10.zip file from email-app\emailapp folder
      - run redis-server.exe file as administrator
    - for Linux (Ubuntu), in a terminal make commands:
      - sudo apt update
      - sudo apt install redis
      - sudo apt install redis-server
      - sudo systemctl start redis
8.  Go to the emailapp folder and install modules listed in the requirements.txt file, by commands in a terminal:
    - cd emailapp
    - pip install <module_name>
    - ...
9.  Migrate django models structure to the database, by commands in a terminal:
    - python manage.py migrate
    - python manage.py makemigrations
    - python manage.py migrate
10. Start Celery and Flower, by commands in a terminal (Redis Server must be running, step 4.):
    - celery -A emailapp worker -l info
    - celery -A emailapp flower
11. Run Django Server, by the command in a terminal:
    - python manage.py runserver 
12. Open carts in a browser:
    - 127.0.0.1:8000/api/mailbox
    - 127.0.0.1:8000/api/template
    - 127.0.0.1:8000/api/email
    - localhost:5555/dashboard
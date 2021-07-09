# attractor

git clone git@github.com:zhoomartq/attractor.git ---> ssh key


Set up virtual environment python -m venv venv/ source venv/bin/activate

I used JWT token for authentication and login

I used PostreSQL

I used celery and redis for  send notifications to gmail

Install Dependencies pip install -r requirements.txt



open access in the mail settings as in the picture
![Screenshot from 2021-07-09 21-05-18](https://user-images.githubusercontent.com/72701687/125099203-966aeb00-e0f9-11eb-86f4-47a6b89a6508.png)

add this

EMAIL_PORT=Your host . Usually its 587

EMAIL_HOST_PASSWORD=password

EMAIL_HOST_USER=Your email

![Screenshot from 2021-07-09 21-09-48](https://user-images.githubusercontent.com/72701687/125099794-37f23c80-e0fa-11eb-9a19-f28286148c31.png)


DB_NAME=database name

DB_USER=user name

DB_PASSWORD=your password

DB_HOST=your localhost

DB_PORT=your port. Usually 5432 for postgres

![Screenshot from 2021-07-09 21-11-48](https://user-images.githubusercontent.com/72701687/125100023-77b92400-e0fa-11eb-8c8d-c4da49911a51.png)


Migrate Database python manage.py makmigrations python manage.py migrate

Run Django Server python manage.py runserver

http://localhost:8000/api/v1/docs - swagger documentation where all endpoints are stored





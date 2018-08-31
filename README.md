# desktwo
Help Desk

[![pypi-version]][pypi]

## Getting Started
This project is developed as a test

### Prerequisites
This application is developed with python 3.6 and Django 2.1
It is required to create a virtualenv with python 3.6

### Installing
After creating an environment
```
$ git clone https://github.com/ludiazoctavio/desktwo.git
```
```
$ pip install -r requirements.txt
```
```
$ python manage.py migrate
```
Create a user who can login to the admin site. Run the following command:
```
$ python manage.py createsuperuser
```
```
Username: admin
```
```
Email address: admin@example.com
```
```
Password: **********
Password (again): *********
Superuser created successfully.
```
Start server as follows:
```
$ python manage.py runserver
```
Open your browser with the following route
http://127.0.0.1:8000

## Authors

* **Luis Octavio Diaz Neri** - [PurpleBooth](https://github.com/ludiazoctavio)

## License

This project is licensed under GNU GENERAL PUBLIC LICENSE - see the [LICENSE.md](LICENSE.md) file for details
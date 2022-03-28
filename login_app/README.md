# Django login application
Reference: https://thinkinfi.com/django-stylish-login-logout-tutorial/

## Configuration
Create initial migrations
```python3 manage.py migrate
```
Create superuser
```python3 manage.py createsuperuser
```
Start serving application
```python3 manage.py runserver
```
Make new migrations
```python manage.py makemigrations
python manage.py migrate
```
## Database
### SQLite
In order to review the models created use 
````sqlite3  db.sqlite3
````
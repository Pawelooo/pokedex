### Pokedex - Pokemon Boards API

REST API to work with Pokemons. All of the CRUD operations are available with basic/session auth.


#### How to run
Create virtualenv and run:
``` 
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
#### Swagger
Swagger is auto generated and available under ```/swagger``` endpoint

#### Usage

You have to be authenticated with Basic/session auth to use API

Get all Pokemon objects example
```
127.0.0.1:8000/api/pokemons/
```

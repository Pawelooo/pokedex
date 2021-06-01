## Pokedex - Pokemon Boards API


REST API to work with Pokemons. All of the CRUD operations are available with basic/session auth.

### How to run
Create virtualenv and run:
``` 
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

```

### Swagger
Swagger is auto generated and available under ```/swagger``` endpoint

### Create user

Creating an account for using the application  
```
python manage.py createsuperuser
```
### Usage

You have to be authenticated with Basic/session auth to use API

Get all Pokemon objects example
```
127.0.0.1:8000/api/pokemons/
```

Get Pokemon by id example
```
127.0.0.1:8000/api/pokemons/1/
```

Search Pokemon by name or type example
```
http://127.0.0.1:8000/api/pokemons/?name=name_of_pokemon
http://127.0.0.1:8000/api/pokemons/?name=name_of_pokemon&kind=kind_of_pokemon/
http://127.0.0.1:8000/api/pokemons/?kind=kind_of_pokemon/
```

Pagination on the page is 5 Pokemon example

```
http://127.0.0.1:8000/api/pokemons/?limit=5&offset=5
```


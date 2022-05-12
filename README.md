# Pre-setup

#### After downloading go to the root directory of the project:

```
cd imdb-app-api
```

#### Create a virtual environment:

```
python -m venv venv
```

#### Install requirements:

```
pip install -r requirements.txt
```

# Build Docker containers

Build an app and database containers:

```
docker-compose build
```

# Fill a database

Fill the database with the data from .csv files:

```
python manage.py fill_db queries/fill_db.sql
```
Path ```queries/fill_db.sql``` is an argument that determines the way to the .sql file to fill the database.

# Usage

Run the docker containers:

```
docker-compose up
```

### Movie

#### List of all movies:

```
http://127.0.0.1:8000/api/movie/movies/
```

You can specify the page and number of elements per page in the `url`. Example:

```
http://127.0.0.1:8000/api/movie/movies/?page=2&size=5
```

This `url` will send you on the second page and make max elements per page as five.

#### Movies by director:

In the `url` path specify a director name. You must specify it using `d` as a key `d=director_name`. Example:

```
http://127.0.0.1:8000/api/movie/movies/d=Ahmed/
```

#### Movies by genre:

Same as a director name specify the genre using `g` as a key `g=genre_name`. Example:

```
http://127.0.0.1:8000/api/movie/movies/g=Comedy
```

### Actor

#### Actor information:

General `url`:

```
http://127.0.0.1:8000/api/actor/actor_stats/actor_id/
```

Specify the actor id in the `url` to see information about actor. Example:

```
http://127.0.0.1:8000/api/actor/actor_stats/15000/
```

Via this `url` you can see information about actor with `id=15000`

### Tests
Run all tests:
```
docker-compose run --rm app sh -c "python manage.py test"
```

# Additional information

#### Data folder

All the data which are .csv files for the database are stored in the `data` folder in the root directory.

#### SQL queries

SQL scripts to create tables and fill them with the data from .csv files are stored in the `queries` folder in the root directory.

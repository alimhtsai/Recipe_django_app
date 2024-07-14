## Recipe_django_app
> * Backend/ Frontend: Python, Django
> * Database: PostgreSQL
> * CI/CD: GitHub Actions, Docker

### Introduction
* A recipe app built with Django framework and PostgreSQL, along with GitHub Actions for TDD and Docker for containerization

### How to test in the local environment
1. Run all the unit tests and check linting: `docker-compose run --rm app sh -c "python manage.py test && flake8"`

### How to start the Django app
1. Run `docker-compose up` to start the docker, if successfully launched, the terminal will show the message below:

   ```shell
   ...
   recipe_django_app-app-1  | Django version 3.2.25, using settings 'app.settings'
   recipe_django_app-app-1  | Starting development server at http://0.0.0.0:8000/
   ```

2. Check Swagger API: [http://127.0.0.1:8000/api/docs/](http://127.0.0.1:8000/api/docs/)

### Project Structure

```
..
├── app/                                # Django project

        ├── app/
        ├── core/                       # store models and database migrations
        ├── recipe/ 
        ├── user/
         manage.py                      # entry point for the Django project

├── .github                             # GitHub Actions yaml file
```

### Approach to creating each app with Test-Driven Development
1. Create a new unit test for the model in `app/core/tests` and create a new model class in `app/core/models`.
2. Make database migrations by running `docker-compose run --rm app sh -c "python manage.py makemigrations"`.
3. Create a new Django app folder to store all the endpoints by running `docker-compose run --rm app sh -c "python manage.py startapp [app name]"`.
4. Add each API endpoint unit test and implement the functions.

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
        ├── core/
        ├── user/
         manage.py                      # entry point for the Django project

├── .github                             # GitHub Actions yaml file
```


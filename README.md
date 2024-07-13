## Recipe_django_app
> * Backend/ Frontend: Python, Django
> * Database: PostgreSQL
> * CI/CD: GitHub Actions, Docker

### Introduction
* A recipe app built with Django framework and PostgreSQL, along with GitHub Actions for TDD and Docker for containerization

### How to test in the local environment
1. Run all the unit tests and check linting: `docker-compose run --rm app sh -c "python manage.py test && flake8"`

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


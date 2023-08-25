
## 1. Set up User model
As we use Django built-in User model for simplicity (in practice, we should always have our custom User model even if we don't have any extra fields at the beginning of project).

Let's run `python manage.py migrate` to apply migration files from Django's core apps (auth, account, admin, etc)

Create superuser so that we can set up test data later:
```
python manage.py createsuperuser
```

## 2. Set up other models and sample data

I want to have fresh migrations so let's go to delete `data/migrations/0001_initial.py` and `db.sqlite3`
then run:
```
python manage.py makemigrations
```

Django should generate the initial migration file (`data/migrations/0001_initial`). To generate sample data, I prepared the second migration file (`data/migrations/0002_generate_test_data`)

Then we apply migrations:
```
python manage.py migrate

```

# from django.apps import AppConfig


# class UsersConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'users'


# apps/users/apps.py

from django.apps import AppConfig

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.users'  # Ensure this is correctly set
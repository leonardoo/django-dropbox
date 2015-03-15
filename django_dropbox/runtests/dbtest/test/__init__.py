import django

if django.VERSION < (1, 6):
    from .tests_models import *
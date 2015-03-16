# django-dropbox
> Version 0.0.5

# What

django-dropbox is a Django App that contains a Django Storage which uses Dropbox.

# Installing

## First of all

    pip install django-dropbox

## Add it to your Django Project

INSTALLED_APPS on settings.py

    INSTALLED_APPS = (
        ...
        'django_dropbox',
        ...
    )

additionally you must need to set the next settings:

    DROPBOX_CONSUMER_KEY = 'xxx'
    DROPBOX_CONSUMER_SECRET = 'xxx'
    DROPBOX_ACCESS_TOKEN = 'xxx'
    DROPBOX_ACCESS_TOKEN_SECRET = 'xxx'

    ACCESS_TYPE = 'app_folder'

if you don't have `DROPBOX_CONSUMER_KEY` or `DROPBOX_CONSUMER_SECRET` 
you will need to create an Dropbox app at [Dropbox for Developers](https://www.dropbox.com/developers)
then set `DROPBOX_CONSUMER_KEY` and `DROPBOX_CONSUMER_SECRET` settings in `settings.py`,
after that run:

    $ python manage.py get_dropbox_token

And follow up on screen instructions, finally set the `DROPBOX_ACCESS_TOKEN` and `DROPBOX_ACCESS_TOKEN_SECRET` in `settings.py`


# Config in app

for use in your app project in the models, you have to add

from django_dropbox.storage import DropboxStorage

STORAGE = DropboxStorage()

and in the fields like

file_1 = models.FileField(upload_to="pathtoupload",storage=STORAGE)

or

logo = models.ImageField(upload_to='pathtoupload', storage=STORAGE)



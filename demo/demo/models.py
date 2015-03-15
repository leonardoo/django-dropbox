from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django_dropbox.storage import DropboxStorage


STORAGE = DropboxStorage(location="/test/djangodropbox")


@python_2_unicode_compatible
class TestDropbox(models.Model):
    """
    Userena model which stores all the necessary information to have a full
    functional user implementation on your Django website.

    """
    file_test = models.FileField(upload_to=".",storage = STORAGE, null=True)

    def __str__(self):
        return self.file_testself.filename

#import os
from django.core.files.base import ContentFile
from django.test import TestCase
from django_dropbox.storage import DropboxStorage
from django.utils import six
from demo.demo.models import TestDropbox

class DropboxStorageTest(TestCase):

    def setUp(self):
        self.file_name = "test.txt"
        self.file_content = "this is a test"

    def test_file_create_in_model(self):
        """
        File must be create in model.
        """
        model = TestDropbox()
        model.file_test.save(self.file_name, ContentFile(self.file_content))
        self.assertEqual(str(model),self.file_name)




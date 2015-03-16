from django.core.files.base import ContentFile
from django.test import TestCase
from django_dropbox.storage import DropboxStorage
from django.utils import six
from django_dropbox.runtests.dbtest.models import TestDropbox

class DropboxStorageTest(TestCase):

    def setUp(self):
        self.file_name = "test.txt"
        self.file_content = six.b("this is a test")

    def test_file_create_in_model(self):
        """
        File must be create in model.
        """
        model = TestDropbox()
        model.file_test.save(self.file_name, ContentFile(self.file_content))
        self.assertEqual(model.__str__(),self.file_name)
        model.file_test.delete()

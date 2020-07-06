from django.test import TestCase

from ..models import File

class FileModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified object to be used by all test methods
        File.objects.create(title='Test', uploaded_by='Tester', document='media/test_files/test_file.txt')

    def test_title(self):
        test_file = File.objects.get(id=1)
        test_title = test_file._meta.get_field('title').verbose_name
        self.assertEquals(test_title, 'title')

    def test_uploaded_by(self):
        test_file = File.objects.get(id=1)
        test_uploaded_by = test_file._meta.get_field('uploaded_by').verbose_name
        self.assertEquals(test_uploaded_by, 'uploaded by')

    def test_document(self):
        test_file = File.objects.get(id=1)
        test_document = test_file._meta.get_field('document').verbose_name
        self.assertEquals(test_document, 'document')

    def test_object_name_is_same_as_title(self):
        test_file = File.objects.get(id=1)
        expected_object_name = f'{test_file.title}'
        self.assertEquals(expected_object_name, str(test_file))
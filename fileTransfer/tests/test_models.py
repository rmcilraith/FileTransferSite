from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from ..forms import FileForm

class FileFormTests(TestCase):

    def test_file_upload(self):
        """
        Mock test file upload
        """
        upload_file = open('media/test_files/test_file.txt', 'rb')
        post_dict = {'title': 'Test Title', 'uploaded_by': 'Test'}
        file_dict = {'document': SimpleUploadedFile(upload_file.name, upload_file.read())}
        form = FileForm(post_dict, file_dict)
        self.assertTrue(form.is_valid())
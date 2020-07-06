from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class TestViews(TestCase):

    def setUp(self):
        self.client.force_login(User.objects.get_or_create(username='testuser')[0])

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/fileTransfer/upload/')
        self.assertEqual(response.status_code, 200)
           
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('file_transfer:file_list'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('file_transfer:file_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'fileTransfer/file_list.html')
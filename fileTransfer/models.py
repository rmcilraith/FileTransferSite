from django.core.signing import Signer
from django.db import models
from django.urls import reverse
from django.conf import settings

class File(models.Model):
    title = models.CharField(max_length=100)
    uploaded_by = models.CharField(max_length=100)
    document = models.FileField(upload_to='files/')
    signer = Signer(sep='/', salt='files.File')

    def __str__(self):
        return self.title

    # Override delete function to include deleting stored file
    def delete(self, *args, **kwargs):
        self.document.delete()
        super().delete(*args, **kwargs)

    def get_absolute_url(self):
        signed_pk = self.signer.sign(self.pk)
        path = reverse('file_transfer:single_file', kwargs={'signed_pk': signed_pk})
        url = f'{settings.SITE_URL}{path}'
        return url
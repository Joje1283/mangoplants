from django.db import models
from django.conf import settings

from commons.utils import uuid_name_upload_to


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    plant = models.ForeignKey('plants.Plant', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=uuid_name_upload_to)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

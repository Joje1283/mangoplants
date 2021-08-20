from django.db import models
from django.conf import settings

from commons.utils import uuid_name_upload_to


class Plant(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    photo = models.ImageField(upload_to=uuid_name_upload_to)

    def __str__(self):
        return self.name

from django.utils import timezone
from django.db import models
from django.conf import settings

from commons.utils import uuid_name_upload_to


class Plant(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=20)
    photo = models.ImageField(upload_to=uuid_name_upload_to)
    note = models.TextField(default='')
    last_water = models.DateField(null=True, blank=True)
    joined = models.DateField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def passed_date(self):
        now_date = timezone.now().date()
        if not self.last_water:
            return
        return (now_date - self.last_water).days


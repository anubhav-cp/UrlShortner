from django.db import models
import uuid


class URL(models.Model):
    full_url = models.CharField(max_length=200)
    short_url = models.CharField(max_length=20)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)

    def __str__(self):
        return f'{self.full_url} to {self.short_url}'

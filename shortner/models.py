from django.db import models



class URL(models.Model):
    full_url = models.CharField(max_length=200)
    short_url = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.full_url} to {self.short_url}'

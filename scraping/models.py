from django.db import models
from django.utils import timezone

# Create your models here.
class Report(models.Model):
    url = models.CharField(max_length=250, unique=True)
    title = models.CharField(max_length=40)
    created_date = models.DateTimeField(default=timezone.now)
    fetched = models.BooleanField(default=False)

    def __str__(self):
        return self.title


    class Meta:
        ordering = ['created_date']


    class Admin:
        pass

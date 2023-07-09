from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class PasswordsList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=100,)
    site = models.URLField()
    notes = models.TextField()
    created = models.DateField(default=timezone.now())
    def __str__(self) -> str:
        return self.site or self.notes
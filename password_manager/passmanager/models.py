from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PasswordsList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=100)
    site = models.URLField()
    notes = models.TextField()
    def __str__(self) -> str:
        return self.site or self.notes
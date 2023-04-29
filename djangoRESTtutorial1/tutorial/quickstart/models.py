from django.db import models

# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=30, null=False)
    description = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    



class Snippets(models.Model):
    snippet = models.CharField(max_length=50, null=False)

    def __str__(self) -> str:
        return self.snippet
from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=500)
    excrept = models.TextField()

    def __str__(self):
        return self.title
    
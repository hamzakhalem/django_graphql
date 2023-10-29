from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Quizzes(models.Model):
    title = models.CharField(max_length=200, default="quiz one")
    category = models.ForeignKey(Category,default=1, on_delete= models.CASCADE)
    date_created = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    
class Question(models.Model):

# class Answer(models.Model):
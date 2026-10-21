from django.db import models

# Create your models here.
class Student (models.Model):
    name = models.CharField(max_length=200 , null=False)
    email = models.EmailField(max_length=200 , null=False)
    about = models.TextField()

    def __str__(self):
        return self.name


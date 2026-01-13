from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    message = models.TextField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
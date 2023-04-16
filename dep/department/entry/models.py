from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    department = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    notebook = models.BooleanField(default=False)
    pen = models.BooleanField(default=False)
    papers = models.BooleanField(default=False)


from django.db import models

# Create your models here.

from django.db import models

# Create your models here.
class Users_Data(models.Model):
    image = models.ImageField()
    uniqueName = models.TextField()
    name = models.TextField()
    gender = models.CharField(max_length=6)
    age = models.PositiveSmallIntegerField()
    motherTongue = models.TextField()
    address = models.TextField()
    hobby = models.TextField()
    contactno=models.PositiveIntegerField()
    emailaddress = models.EmailField()
    password = models.CharField(max_length=50)
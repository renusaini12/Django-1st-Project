from django.db import models

# Create your models here.
class Cont(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Subject = models.CharField(max_length=10)
    Contact = models.IntegerField()


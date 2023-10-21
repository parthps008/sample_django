from django.db import models

# Create your models here.
from django.db import models

class CompanyInfo(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

from django.db import models

# Create your models here.
class Company(models.Model):
    name=models.CharField(max_length=50)
    url=models.URLField(max_length=200)
    foundation=models.PositiveBigIntegerField()
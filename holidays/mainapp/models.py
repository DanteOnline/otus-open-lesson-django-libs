from django.db import models


# Create your models here.
class Holiday(models.Model):
    name = models.CharField(max_length=32)
    date = models.DateField()
    img = models.ImageField(upload_to='holidays')

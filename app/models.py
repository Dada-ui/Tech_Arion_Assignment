from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField( max_length=100)
    stock = models.BooleanField(default=False,blank=True)
    description = models.CharField( max_length=500)
    length = models.IntegerField()
    size = models.CharField(max_length=50)
    star = models.CharField(max_length=50)

    def __str__(self):
        return self.title
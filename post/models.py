from django.db import models
from django.utils import timezone
from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    datetime = models.DateTimeField(default=timezone.now)
    objects = models.Manager()
    def __str__(self):
        return self.description

class Emotional(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    score = models.FloatField(null=True,blank=True)
    polarity_neg = models.CharField(max_length=100)
    polarity_pos = models.CharField(max_length=100)
    


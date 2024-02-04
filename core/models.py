from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Image(models.Model):
    image_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='curr_item')
    time_submitted = models.DateTimeField(auto_now_add=True)
    constellation_name = models.CharField(max_length=100)
    notes = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='images/')
    score = models.IntegerField()

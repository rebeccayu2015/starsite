from django.db import models
import json
from django.contrib.auth.models import User
from django.contrib.auth.models import User

# Create your models here.
starDict2 = {}
with open('static/json/constellations.json') as json_star:
    constellations = json.load(json_star)
    for i in range(88):
        name = constellations[i]["latin_name_nom_latin"]
        image_url = ""
        found = 0
        starDict2[name] = [found, image_url]
jsonConstells = json.dumps(starDict2)

class ProfileConstellation(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'curr_prof')
    image_id = models.ImageField(upload_to="images/", height_field=None, width_field=None, max_length=100)
    image_name = models.CharField(max_length = 100)
    found_dict = models.CharField(max_length = 10000, default = 'none')

class Image(models.Model):
    image_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='curr_image')
    time_submitted = models.DateTimeField(auto_now_add=True)
    constellation_name = models.CharField(max_length=100)
    notes = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='images/')
    score = models.IntegerField()

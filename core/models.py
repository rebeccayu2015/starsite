from django.db import models
import json
from django.contrib.auth.models import User

# Create your models here.
starDict2 = {}
with open('constellations.json') as json_star:
    constellations = json.load(json_star)
    for i in range(88):
        name = constellations[i]["latin_name_nom_latin"]
        image_url = ""
        found = 0
        starDict2[name] = [found, image_url]

class ProfileConstellation(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'curr_item')
    image_id = models.ImageField(upload_to="media/", height_field=None, width_field=None, max_length=100)
    image_name = models.CharField(max_length = 100)
    found_dict = dict(starDict2)
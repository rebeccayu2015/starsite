from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from core.models import Image, starDict2
from django.contrib.auth.models import User
from django.contrib import messages
from core.models import ProfileConstellation, jsonConstells
from django.core.exceptions import ObjectDoesNotExist
import json

# Create your views here.
def home(request):
    images = Image.objects.all()
    user = request.user

    context = {
        'images': images,
        'user': user
    }

    return render(request, 'core/home.html', context)

def profile(request):
    json_const = open('static/json/constellations.json')
    constellations = json.load(json_const)
    json_const.close()
    
    context = {
        'constellations' : constellations
    }

    return render(request, 'core/profile.html', context)

def submit(request):
    if request.method == 'POST':
        const_name = request.POST['const-name']
        image_notes = request.POST['notes']
        const_image = request.FILES['image']

        image = Image(constellation_name=const_name,
                    user_id=request.user.id,
                    notes=image_notes,
                    image=const_image,
                    score=0)
        image.save()

        user = User.objects.get(id=request.user.id)
        json_starDict = json.loads(jsonConstells)
        json_starDict[const_name][0] = 1

        try: #if user already present then overwrite
            user_data = ProfileConstellation.objects.get(user_id = user) 
            json_starDict2 = json.loads(user_data.found_dict)
            user_data.image_src = const_image
            user_data.image_name = const_name
            user_data.save()
            user_data = ProfileConstellation.objects.get(user_id = user) 
            json_starDict2[const_name][1] = str(user_data.image_src)
            json_starDict2[const_name][0] = 1
            user_data.found_dict = json.dumps(json_starDict2)
            user_data.save()

        except ObjectDoesNotExist: # if user new then add an entry.
            profConstell = ProfileConstellation(
                user_id = user,
                image_src = const_image,
                image_name = const_name,
                found_dict = json.dumps(json_starDict)
            )
            profConstell.save()
            user_data = ProfileConstellation.objects.get(user_id = user) 
            user_data.image_src = const_image
            user_data.image_name = const_name
            json_starDict2 = json.loads(user_data.found_dict)
            json_starDict2[const_name][1] = str(user_data.image_src)
            json_starDict2[const_name][0] = 1
            user_data.found_dict = json.dumps(json_starDict2)
            user_data.save()



        messages.success(request, "Added image \"" + image.constellation_name + "\".")
        return redirect('home')

    return render(request, 'core/submit.html')

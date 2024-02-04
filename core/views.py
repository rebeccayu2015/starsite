from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from core.models import Image
from django.contrib import messages
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
    json_const = open('users/static/json/constellations.json')
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

        messages.success(request, "Added image \"" + image.constellation_name + "\".")
        return redirect('home')

    return render(request, 'core/submit.html')

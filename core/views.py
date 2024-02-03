from django.shortcuts import render

# Create your views here.
def home(request):
    context = {}

    return render(request, 'core/home.html', context)

def profile(request):
    context = {}

    return render(request, 'core/profile.html', context)

def submit(request):
    context = {}

    return render(request, 'core/submit.html', context)

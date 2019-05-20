from django.shortcuts import render
from .models import Image

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')

def search_image(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = Image    
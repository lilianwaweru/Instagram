from django.shortcuts import render
from .models import Image

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')

def search_image(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = (request.GET.get("image")).title()
        searched_images = Image.search_by_image(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any image"
        return render(request, 'search.html',{"message":message})    

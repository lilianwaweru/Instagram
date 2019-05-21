from django.shortcuts import render,redirect
from .models import Image,Profile
from django.contrib.auth.decorators import login_required
from .forms import getProfile

# Create your views here.
def welcome(request):
    images = Image.objects.all()
    return render(request,'welcome.html',{"images":images})

def search_image(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = (request.GET.get("image")).title()
        searched_images = Image.search_by_image(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any image"
        return render(request, 'search.html',{"message":message})    




def index(request):
    title = "Index Page"
    return render (request, 'index.html', {"title":title})


def edit_profile_info(request):
    logged_user =request.user.id
    if request.method == 'POST':
        form = getProfile(request.POST,request.FILES)
        if form.is_valid():
            edit_profile = form.save(commit=False)
            edit_profile.infor = logged_user
            edit_profile.save()
            return redirect('welcome')
    else:
        form = getProfile()

    return render(request,'Profile.html',{'form':form})







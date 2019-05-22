from django.shortcuts import render,redirect
from .models import Image,Profile,Comments
from django.contrib.auth.decorators import login_required
from .forms import getProfile,uploadPhoto,Comment

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

@login_required(login_url='/accounts/login/')
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

@login_required(login_url='/accounts/login/')
def Photo(request):
    logged_user =request.user.id
    if request.method == 'POST':
        form = uploadPhoto(request.POST,request.FILES)
        if form.is_valid():
            Photo = form.save(commit=False)
            Photo.profile = logged_user
            Photo.save()
            return redirect('welcome')
    else:
        form = uploadPhoto()

    return render(request,'upload.html',{'form':form})


@login_required(login_url='/accounts/login/')
def comment(request,image_id):

    image = Image.objects.get(id = image_id)

    if request.method=='POST':
        current_user=request.user
        form=Comment(request.POST)
        if form.is_valid:
            comments=form.save(commit=False)
            comments.user=current_user
            comments.picture=image.id
            comments.save()

            return redirect('welcome')
    else:
        form=Comment()
    
    comments = Comments.objects.filter(picture=image_id).all
    
    return render(request,"comment.html",{'form':form, "image":image ,"comments":comments})


@login_required(login_url='/accounts/login/')
def profile(request):
    users =request.user.id
    
    try:
        profile = Profile.objects.filter(infor=users).first()
        all_images = Image.objects.filter(infor_id=request.user.id).all()

    except ObjectDoesNotExist:

        return redirect('welcome')

    return render (request,"edit.html",{"profile":profile,"all_images":all_images})

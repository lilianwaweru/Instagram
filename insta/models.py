from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    infor = models.IntegerField(default=0)
    bio = models.CharField(max_length = 70)
    profile_picture = models.ImageField(upload_to = 'images/',blank=True)

    
    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()  


class Image(models.Model):
    name = models.CharField(max_length = 70)
    profile = models.CharField(max_length=30,blank=True)
    image = models.ImageField(upload_to = 'images/',blank=True)
    caption = models.TextField()
    

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()  


    @classmethod
    def search_by_image(cls,search_term):
        images = cls.objects.filter(image__name__icontains = search_term)
        return images
      
class Comments(models.Model):
    picture = models.IntegerField(default=0)
    user = models.ForeignKey(User)
    comments = models.TextField() 

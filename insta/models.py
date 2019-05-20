from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    bio = models.CharField(max_length = 70)
    profile_picture = models.ImageField(upload_to = 'images/',blank=True)
    




class Image(models.Model):
    name = models.CharField(max_length = 70)
    profile = models.ForeignKey(Profile)
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
      

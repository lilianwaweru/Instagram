from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length = 70)
    image = models.ImageField(upload_to = 'images/',blank=True)
    

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()  

# class Profile(models.Model): 
#     profile_image = models.ImageField(upload_to = 'images/',blank=True)
#     Bio =  models.CharField(max_length= 100)
    
      
    

from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length = 70)
    description = models.TextField()
    image = models.ImageField(upload_to = 'images/',blank=True)
    

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()   
    

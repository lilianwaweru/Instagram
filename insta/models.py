from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length = 70)
    caption = models.TextField()
    image = models.ImageField(upload_to = 'images/',blank=True)
    
    

from django.db import models

# Create your models here.

class Product(models.Model):
  name=models.CharField(max_length=250)
  strap_color=models.CharField(max_length=20)
  highlights=models.CharField(max_length=250)
  price=models.FloatField()
  status=models.BooleanField(default=True)
  image=models.ImageField(upload_to='product_images')
  

  def __str__(self): 
    return self.name
  


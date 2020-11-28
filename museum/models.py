from django.db import models

# Create your models here.
class Construction(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=100)
    history = models.TextField(default="")
    author = models.CharField(max_length=200)
    creation_date = models.DateField()
    
    def __str__(self):
        return self.name
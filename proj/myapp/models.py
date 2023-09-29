from django.db import models

# Create your models here.
class Person(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    profileIm=models.ImageField(upload_to="images",null=True,blank=True)
    def __str__(self):
        return self.name
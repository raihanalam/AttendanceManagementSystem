from django.db import models

# Create your models here.
class user(models.Model):
    fullName = models.CharField(max_length=100,blank=False)
    handle = models.CharField(primary_key=True,max_length=100,blank=False,unique=True)
    image = models.ImageField(upload_to='user')
    role = models.CharField(max_length=10,blank=False,null=False)
    email = models.CharField(max_length=100,blank=False,unique=True)
    password = models.CharField(max_length=100,blank=False)
    def __str__(self):
        return self.handle
from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    r_name =models.CharField(max_length=100)
    r_desc = models.TextField(null = True)
    r_image=models.ImageField(upload_to="xyz")


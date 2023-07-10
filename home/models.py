from django.db import models

# Create your models here.



class Student(models.Model):
    r_name =models.CharField(max_length=100)
    r_desc = models.TextField(null = True)
    r_image=models.ImageField(upload_to="xyz")


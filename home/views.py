from django.shortcuts import render, redirect
from django.http import HttpResponse 
from . models import *

# Create your views here.
def home(request):
        
        
        if request.method=="POST":

            data=request.POST
            r_image=request.FILES.get("r_image")
            r_name=data.get("r_name")
            r_desc=data.get("r_desc")
            print(r_name)

            Student.objects.create(
                r_name=r_name,
                r_desc=r_desc,
                r_image=r_image,

            )
            return redirect('/')
        queryset=Student.objects.all()

        if request.GET.get('search'):
            queryset = queryset.filter(r_name__icontains = request.GET.get('search'))

        context = {'home':queryset}
        


        return render(request,"index.html",context)


def update_rec(request,id):
    queryset = Student.objects.get(id=id)
    if request.method=="POST":
            

            data=request.POST
            r_image=request.FILES.get("r_image")
            r_name=data.get("r_name")
            r_desc=data.get("r_desc")
            queryset.r_name=r_name
            queryset.r_desc=r_desc
            if r_image:
                queryset.r_image=r_image
            queryset.save()
            return redirect('/')

    context = {'update':queryset}
    return render(request,"update.html",context)


def delete_rec(request,id):
    queryset =Student.objects.get(id=id)
    queryset.delete()
    return redirect('/')

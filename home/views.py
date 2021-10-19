from typing import Counter
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from account.models import user
from .models import course

# Create your views here.
def home(request):
    userData = user.objects.all()

    context = {
        'userData' : userData
    }
    return render(request,'home/home.html',context)
    
def createCourse(request):
    if request.method =='POST':
        code = request.POST['code']
        title = request.POST['title']
        teacher = request.user.username
        season = request.POST['season']
        key = request.POST['key']

        mycourse = course(code,title,teacher,season,key)
        mycourse.save()

    return render(request,'home/createcourse.html')


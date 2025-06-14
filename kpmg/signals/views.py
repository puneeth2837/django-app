from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

def index(request,id=None):
    res=id
    return HttpResponse(res)

def main(request,name=None):
    res=[1,2,3,4,5,6,7,8,9,10]
    return render(request,"signals/index.html",{"name":name,"res":res})

def student(request,fname=None):
    request.session['fname']=fname
    if fname is None:
      stu=Student.objects.all()
    else:
        stu=Student.objects.filter(fname=fname)
    return render(request,"signals/index.html",{"res":stu})

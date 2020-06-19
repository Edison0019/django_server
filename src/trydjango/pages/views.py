from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request,*args,**kwards):
    print(args,kwards)
    print(request.user)
    #return HttpResponse("<h1>hello world</h1)>") #string in html code
    return render(request,'main.html',{})

def main_page(request,*args,**kwards):
    return render(request,'about.html',{})

def content_page(request,*args,**kwards):
    return render(request,'content.html',{})

def content_base(request,*args,**kwards):
    return render(request,'base.html',{})
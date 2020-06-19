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
    my_content = {
        "my_text" : "this is about us",
        "this_is_true" : True,
        "my_number" : 5,
        "my_list" : [1111,2222,3333,4444,5555,6666,'wefg']
    }
    return render(request,'content.html',my_content)

def content_base(request,*args,**kwards):
    return render(request,'base.html',{})
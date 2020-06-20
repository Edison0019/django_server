from django.shortcuts import render
from .models import products
from .form import product_form
# Create your views here.
def product_detail_view(request):
    obj = products.objects.get(id=1)
    '''context = {
        "title" : obj.title,
        "price" : obj.price,
        "description" : obj.description
    }'''

    context = {
        'object' : obj
    }
    return render(request,'products/product_template.html',context)


'''def product_create_view(request):
    form = product_form(request.POST or None)
    if form.is_valid():
        form.save()
        form = product_form()
    
    context = {
        'form' : form
    }
    
    return render(request,'products/product_form.html',context)'''

def product_create_view(request):
    print(request.POST)
    print(request.GET)
    context = {}
    return render(request,'products/product_form.html',context)
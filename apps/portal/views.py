from django.shortcuts import render, redirect

# Create your views here.

from .models import Product
from .forms import ProductForm

def portal(request):

    products = Product.objects.all()
    context ={ 
        'title': "DeliHellas Portal",
        'products': products,
        }
    return render(request, 'portal/portal.html', context=context)


   

def add_product(request):  
    if request.method == "POST":  
        form = ProductForm(request.POST, request.FILES)  
        if form.is_valid():  
            try:  
                form.save() 

                #model = form.instance
                return redirect('portal')  
            except:  
                pass  
        else:
            return render(request,'portal/add_product.html',{'form':form})  
    else:  
        form = ProductForm()  
    return render(request,'portal/add_product.html',{'form':form})  


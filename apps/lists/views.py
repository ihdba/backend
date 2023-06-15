from django.shortcuts import render, redirect


from .models import Category, Item, Fellowship
from .forms import CategoryForm, ItemForm

# Class based views

from django.views.generic import TemplateView, ListView

# all lists
# def all_lists(request):

#     #items = Items.objects.order_by("theme")
#     items = Items.objects.all()

#     context = {
#         'title': 'All lists',
#         'items': items,
#     }

#     return render(request, 'lists/all_lists.html', context=context)



# list detail
def list_detail(request, id):
    pass



def itemUpdate(request, id):  
    item = Item.objects.get(pk=id)
    form = ItemForm(initial={'item': item.item})
    if request.method == "POST":  
        form = ItemForm(request.POST, instance=item)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('all_lists')  
            except Exception as e: 
                pass    
    return render(request,'lists/edit_item.html',{'form':form})  




def addItem(request):  
    if request.method == "POST":  
        form = ItemForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('all_lists')  
            except:  
                pass  
    else:  
        form = ItemForm()  
    return render(request,'lists/add_item.html',{'form':form})  




# Class based views

# TemplateView - generic view that shows static pages, that is just request. No data from db is recieved
# Used very few

class AboutView(TemplateView):

    

    def get(self, request):

        context = {
        'title': 'About Lists',
        }

        return render(request, 'lists/about.html', context=context)
   
    


# Class based all_lists

class AllListsView(ListView):

    def get(self, request):

        items = Item.objects.all()

        context ={
            'title': 'All Lists',
            'items': items,
        }

       

        return render(request, 'lists/all_lists.html', context=context)
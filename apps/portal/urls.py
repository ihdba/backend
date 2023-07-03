
from django.urls import path, include

# from apps.todo import views 



from . import views

urlpatterns = [
    path('', views.portal, name='portal'),
    path('add_product/', views.add_product, name='add_product'),
] 

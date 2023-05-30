
from django.urls import path, include

# from apps.todo import views 



from . import views

urlpatterns = [
    path('', views.portal, name=''),
    path('blog/', include('apps.blog.urls')),
    path('recipes/', include('apps.recipes.urls')),
] 

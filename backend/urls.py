
from django.contrib import admin
from django.urls import path, include

from apps.todo import views 
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'todo', views.TaskViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include('apps.blog.urls')),
    path('recipes/', include('apps.recipes.urls')),
    path('all_lists/', include('apps.lists.urls')),
    path('training/', include('apps.training.urls')),
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from apps.todo import views 
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'todo', views.TaskViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include('apps.blog.urls')),
    path('recipes/', include('apps.recipes.urls')),
    path('portal/', include('apps.portal.urls')),
    path('all_lists/', include('apps.lists.urls')),
    path('training/', include('apps.training.urls')),
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
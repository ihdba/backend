from django.urls import path

from apps.todo import views 
from rest_framework import routers



router = routers.DefaultRouter()
router.register(r'todo', views.TaskViewSet)



urlpatterns = [
    path('', include(router.urls)),
]
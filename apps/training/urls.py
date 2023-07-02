from django.urls import path

from . import views

urlpatterns=[
    path('', views.training, name= 'training'),
    path('add_training/', views.add_training, name= 'add_training'),
    path('edit_training/<int:id>', views.edit_training, name= 'edit_training'),
]
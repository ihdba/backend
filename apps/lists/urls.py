from django.urls import path

from . import views

from .views import AboutView, AllListsView



urlpatterns = [
    # path('', views.all_lists, name='all_lists'),
    path('add_item/', views.addItem, name='add_item'),
    path('edit_item/<int:id>', views.itemUpdate, name='edit_item'),
    # path('list_detail/<int:id>', views.list_detail, name='list_detail'),

    # using generic views
    path('', AllListsView.as_view(), name='all_lists'),
    path('about/', AboutView.as_view(), name='about'),
]
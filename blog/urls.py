from django.urls import path
from .views import post_create, post_delete, post_list, post_update

urlpatterns = [
    path('',post_list,name='post_list'),
    path('create/',post_create,name='post_create'),
    path('delete/',post_delete,name='post_delete'),    
    path('update/',post_update,name='post_update'),
    
]

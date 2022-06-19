from django.urls import path
from .views import post_create, post_delete, post_list, post_update, post_detail

app_name = 'blog' #! Birden fazla app olduğunda nameler karışmasın diye blog:post_list yazabilmek için
urlpatterns = [
    path('', post_list, name='post_list'),
    path('create/', post_create, name='post_create'),
    path('<str:slug>/', post_detail, name='post_detail'),
    path('<str:slug>/delete/', post_delete, name='post_delete'),    
    path('<str:slug>/update/', post_update, name='post_update'),    
]

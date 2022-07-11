from django.contrib import admin
from .models import Category, Post , Comment, Like, PostView
from import_export.admin import ImportExportModelAdmin
from blog.resources import PostResource

class PostAdmin(ImportExportModelAdmin):    
    resource_class = PostResource

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(PostView)

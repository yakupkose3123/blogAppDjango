from django.contrib import admin
from import_export import resources
from .models import Category, Post , Comment, Like, PostView
from import_export.admin import ImportExportModelAdmin

class PostResource(resources.ModelResource):
        class Meta:
            model = Post
class PostAdmin(ImportExportModelAdmin):
    resource_class = PostResource



admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(PostView)

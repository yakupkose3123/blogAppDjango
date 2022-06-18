from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'


#! signals.py da işlem yapabilmek için 
    def ready(self):
        import blog.signals

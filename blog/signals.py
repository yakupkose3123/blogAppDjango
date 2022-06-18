from django.db.models.signals import pre_save #!kaydetmeden önce
from django.dispatch import receiver #!kaydet e bastığımda bunu yap sonra kaydet
from django.template.defaultfilters import slugify #!boşlukların arasına - koyar
from .models import Post 

#*Bu dosyanın amacı otomatik slug oluşturmak
#* apps.py da signals.py override etmeyi unutma

@receiver(pre_save, sender=Post)
def pre_save_create_slug(sender, instance, **kwargs):
    if not instance.slug: #slug yoksa
        instance.slug = slugify(instance.author.username + " " + instance.title)
        
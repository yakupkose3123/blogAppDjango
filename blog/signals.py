from django.db.models.signals import pre_save #!kaydetmeden önce
from django.dispatch import receiver #!kaydet e bastığımda bunu yap sonra kaydet
from django.template.defaultfilters import slugify #!boşlukların arasına - koyar
from .models import Post 
from .utils import get_random_code

#*Bu dosyanın amacı otomatik slug oluşturmak
#* apps.py da signals.py override etmeyi unutma
#* utils.py da random ıd oluşturuyoruz.

@receiver(pre_save, sender=Post)
def pre_save_create_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title + " " + get_random_code())
        
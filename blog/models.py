from django.db import models
from django.contrib.auth.models import User


#! CATEGORY 
# Bu postun parenti olduğu için daha yukarıda tanımlamalıyız.
class Category(models.Model):
    name = models.CharField(max_length=100)

#! POST
class Post(models.Model):
    OPTIONS = (
        ('DRA', 'DRAFT'),
        ('PUB', 'PUBLISH'),
    )

    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT) #burada protect dediğimizde category silince Post u silmesin 
    publish_date = models.DateTimeField(auto_now_add=True)
    last_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #! Foreignkey one to many için. bir postun tek author u olur ama bir author un birden fazla postu olabilir. CASCADE user silinince psotu da sil demek
    
    status = models.CharField(max_length=10, choices=OPTIONS, default='DRA') #draft ta ise yayınlanmamış olacak(mail deki taslaklar gibi düşün) published de ise yayınlayacak.
    slug = models.SlugField(blank=True, unique=True)

from distutils.command.upload import upload
from email.policy import default
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

#* Media dosyalarının kaydediliş şeklini belirlemek için
def user_directory_path(instance, filename):
    return 'blog/{0}/{1}'.format(instance.author.id, filename)


#! CATEGORY 
# Bu postun parenti olduğu için daha yukarıda tanımlamalıyız.
class Category(models.Model):
    name = models.CharField(max_length=100)
    class Meta : 
        verbose_name_plural = "CATEGORIES"

    def __str__(self):
        return self.name

#! POST
class Post(models.Model):
    OPTIONS = (
        ('DRA', 'DRAFT'),
        ('PUB', 'PUBLISHED'),
    )

    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to=user_directory_path, default = 'django.jpg')
    category = models.ForeignKey(Category, on_delete=models.PROTECT) #burada protect dediğimizde category silince Post u silmesin 
    publish_date = models.DateTimeField(auto_now_add=True)
    last_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #! Foreignkey one to many için. bir postun tek author u olur ama bir author un birden fazla postu olabilir. CASCADE user silinince psotu da sil demek
    
    status = models.CharField(max_length=10, choices=OPTIONS, default='DRA') #draft ta ise yayınlanmamış olacak(mail deki taslaklar gibi düşün) published de ise yayınlayacak.
    slug = models.SlugField(blank=True, unique=True)

    class Meta : 
        verbose_name_plural = "POSTS"
    def __str__(self):
        return self.title
    #! COMMENT COUNT
    def comment_count(self):
        return self.comment_set.all().count() #Comment modelime git(parent) tüm commentlerin sayısını al. Burada fonksiyonu oluştururken aşağıdaki ilgili class ın ilk harfini küçülterek alıyorum.
    #! VIEW COUNT
    def view_count(self):
        return self.postview_set.all().count()
    #! LIKE COUNT
    def like_count(self):
        return self.like_set.all().count()
    #! COMMENTS
    def comments(self):
        return self.comment_set.all() #Oluşturulan tüm commentleri al
    


#! COMMENT (YORUMLAR)

class Comment(models.Model) :
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     post = models.ForeignKey(Post, on_delete=models.CASCADE)
     time_stamp = models.DateTimeField(auto_now_add=True)
     content = models.TimeField()

     def __str__(self):
        return self.user.username



#! LIKE
class Like(models.Model) :
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     post = models.ForeignKey(Post, on_delete=models.CASCADE)
     
     def __str__(self):
            return self.user.username
#! POST VİEW 
class PostView(models.Model) :
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     post = models.ForeignKey(Post, on_delete=models.CASCADE)
     time_stamp = models.DateTimeField(auto_now_add=True)
     
     def __str__(self):
            return self.user.username

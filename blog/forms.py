from django import forms
from .models import Post, Comment, Category

class PostForm(forms.ModelForm):
    status = forms.ChoiceField(choices=Post.OPTIONS) # modeldeki optıons u kullanabiliriz
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Select") #! Başka bir table daki fieldı dropdown olarak göstermmek için. 
    class Meta:
        model = Post
        fields = (
            'title',
            'content',
            'image',
            'category',
            'status',
        )
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        
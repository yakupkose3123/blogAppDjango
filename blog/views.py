from multiprocessing import context
from turtle import ondrag
from django.shortcuts import get_object_or_404, render, redirect
from .models import Post,  Like, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


#! POST LIST
def post_list(request):
    qs = Post.objects.filter(status='PUB')
    context = {
        'object_list' : qs
    }
    return render (request, "blog/post_list.html", context )

#! POST CREATE
@login_required()
def post_create(request):
    # form = PostForm(request.POST or None, request.FILES or None)
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES) #? Bu koşulu update deki 45. satır gibi de yapabiliriz. "form = PostForm(request.POST or None, request.FILES or None, instance=obj)"
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user #!formdaki author kısmı kullanıcıdan çekip ekliyoruz
            post.save()
            messages.success(request, "Post created successfully!")
            return redirect("blog:post_list")
    context = {
        'form' : form
    }
    return render(request, "blog/post_create.html", context)


#! POST DETAİL
def post_detail(request, slug):
    form = CommentForm()
    obj = get_object_or_404(Post, slug = slug)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False) #!Comment i form ile kullanıcıdan al
            comment.user = request.user #! User olarak şu anki userı al
            comment.post = obj #! Bu yukarıda aldığım obj nin postunu al 
            comment.save() #! sonra da formu database kaydet
            return redirect("blog:post_detail", slug=slug) #! sonra da bir önceki sayfaya geri gönder
            # return redirect(request.path)  buda üst satırla aynı
    context = { 
        "object" : obj,
        "form" : form
     }
    return render(request, "blog/post_detail.html", context)

#! POST UPDATE
@login_required()
def post_update(request, slug):
    obj = get_object_or_404(Post, slug = slug)
    if request.user.id != obj.author.id: #! url den postun sahibi olmayanların silmesini engellemek için
        # return HttpResponse("You are not authorized!")
        messages.warning(request, "You are not a writer of this post !")
        return redirect("blog:post_list")
    form = PostForm(request.POST or None, request.FILES or None, instance=obj) 

    if form.is_valid():
        form.save()
        return redirect("blog:post_list")
    
    context = {
        "object" : obj,
        "form" : form
    }

    return render(request, "blog/post_update.html", context)

#! POST DELETE
@login_required()
def post_delete(request, slug):
    obj = get_object_or_404(Post, slug=slug) #slug ı slug olan objeyi al
    if request.user.id != obj.author.id: #! url den postun sahibi olmayanların silmesini engellemek için
        # return HttpResponse("You are not authorized!")
        messages.warning(request, "You are not a writer of this post !")
        return redirect("blog:post_list")
    if request.method == "POST": 
        obj.delete()
        messages.success(request, "Post deleted !!")
        return redirect("blog:post_list")
    
    context = {
        "object" : obj
    }
    return render(request, "blog/post_delete.html", context)

#! LIKE
@login_required()
def like(request, slug):
    if request.method == "POST":
        obj = get_object_or_404(Post, slug=slug)
        like_qs = Like.objects.filter(user=request.user, post=obj) #db de like ım var mı?
        if like_qs: # varsa like ı geri al
            like_qs[0].delete()
        else:
            Like.objects.create(user=request.user, post=obj)
        return redirect("blog:post_detail", slug=slug)
    return redirect("blog:post_detail", slug=slug)
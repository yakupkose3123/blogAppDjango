from turtle import ondrag
from django.shortcuts import get_object_or_404, render, redirect
from .models import Post
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
        form = PostForm(request.POST, request.FILES)
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
    obj = get_object_or_404(Post, slug = slug)
    context = {
        "object" : obj
    }
    return render(request, "blog/post_detail.html", context)


def post_delete(request):
    return render(request, "blog/post_delete.html")

def post_update(request):
    return render(request, "blog/post_update.html")


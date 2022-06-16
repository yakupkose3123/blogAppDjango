from django.shortcuts import render

def post_list(request):
    return render(request, "blog/post_list.html")
def post_delete(request):
    return render(request, "blog/post_delete.html")
def post_create(request):
    return render(request, "blog/post_create.html")
def post_update(request):
    return render(request, "blog/post_update.html")

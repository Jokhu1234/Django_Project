from django.shortcuts import render, redirect
from .models import Blog
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.


def blogs(request):
    blogs = Blog.objects.all()
    return render(request, "blogs.html", {"blogs": blogs})


def blog_page(request, slug):
    blog = Blog.objects.get(slug=slug)
    return render(request, "blog_post.html", {"blog": blog})


@login_required(login_url="/users/login/")
def blog_new(request):
    if request.method == "POST":
        form = forms.CreateBlog(request.POST, request.FILES)
        if form.is_valid():
            # save the post
            newpost = form.save(commit=False)
            newpost.author = request.user
            newpost.save()
            return redirect("blogs:bloglist")

    else:
        form = forms.CreateBlog()
    return render(request, "blog_new.html", {"form": form})
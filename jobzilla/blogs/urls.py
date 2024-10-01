from django.urls import path
from . import views

app_name = "blogs"

urlpatterns = [
    path("", views.blogs, name="bloglist"),
    path("new-blog/", views.blog_new, name="new-blog"),
    path("<slug:slug>", views.blog_page, name="blogdetails"),
]

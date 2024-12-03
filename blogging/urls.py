from django.urls import path
from blogging.views import BlogListView, BlogDetailView, add_post

urlpatterns = [
    path("add/", add_post, name="add_post"),
    path("posts/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("", BlogListView.as_view(), name="blog_index"),
]

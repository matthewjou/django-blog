from django.urls import path
from blogging.views import list_view, detail_view, BlogListView, BlogDetailView

urlpatterns = [
    # old views
    # path('posts/<int:post_id>/', detail_view, name="blog_detail"),
    # path('', list_view, name="blog_index"),
    path("posts/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("", BlogListView.as_view(), name="blog_index"),
]
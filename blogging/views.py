from django.shortcuts import render
from blogging.models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import PostForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class BlogListView(LoginRequiredMixin, ListView):
    queryset = Post.objects.exclude(published_date__exact=None).order_by(
        "-published_date"
    )
    template_name = "blogging/list.html"


class BlogDetailView(LoginRequiredMixin, DetailView):
    queryset = Post.objects.exclude(published_date__exact=None)
    template_name = "blogging/detail.html"


@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/')
    else:
        form = PostForm()
    return render(request, 'blogging/add.html', {'form': form})
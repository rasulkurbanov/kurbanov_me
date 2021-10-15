from django import forms
from django.shortcuts import get_object_or_404, render
from datetime import date
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .forms import CommentForm
from .models import Post

# Create your views here.
class StartingPageView(ListView):
    template_name = 'blog/index.html'
    model = Post
    ordering = ['-date', 'title']
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data

class AllPostsView(ListView):
    model = Post
    template_name = 'blog/posts.html'
    ordering = ['-date']
    context_object_name = 'all_posts'

class SinglePostDetailView(DetailView):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        post_tags = post.tag.all()
        form = CommentForm()
        context = {'post': post, 'post_tags': post_tags, 'form': form}
        return render(request, 'blog/post-detail.html', context)



from django import forms
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from datetime import date
from django.views.generic import ListView
from django.views.generic.base import View
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

class SinglePostDetailView(View):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        post_tags = post.tag.all()
        post_comments = post.comments.all().order_by('-id')
        form = CommentForm()
        context = {
            'post': post, 
            'post_tags': post_tags, 
            'form': form,
            'comments': post_comments
            }
        return render(request, 'blog/post-detail.html', context)


    def post(self, request, slug):
        post = Post.objects.get(slug=slug)
        post_tags = post.tag.all()
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse('post-detail-page', args=[slug]))

        context = {
            'post': post,
            'post_tags': post_tags,
            'comment_form': comment_form,
            'post_comments': post.comments.all().order_by('-id')
        }
        return render(request, 'blog/post-detail.html', context)

class ReadLaterView(View):
    def get(self, request):
        stored_posts = request.session.get('stored_posts')

        context = {}

        if stored_posts is None or len(stored_posts) == 0:
            context['posts'] = []
            context['has_posts'] = False
        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context['posts'] = posts
            context['has_posts'] = True

        return render(request, 'blog/stored-posts.html', context)


    def post(self, request):
        stored_posts = request.session.get('stored_posts')

        if stored_posts is None:
            stored_posts = []

        post_id = int(request.POST.get('post_id'))

        if post_id not in stored_posts:
            stored_posts.append(post_id)


        return HttpResponseRedirect('/')






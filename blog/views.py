from django.shortcuts import get_object_or_404, render
from datetime import date
from .models import Post

def get_date(post):
    return post['date']

# Create your views here.
def starting_page(request):
    latest_posts = Post.objects.all().order_by('-date')[:3]
    context = {'posts': latest_posts}
    return render(request, 'blog/index.html', context)

def posts(request):
    all_posts = Post.objects.all()
    context = {'all_posts': all_posts}
    return render(request, 'blog/posts.html', context)


def post_detail(request, slug):
    print('heeey')
    single_post = get_object_or_404(Post, slug=slug)
    post_tags = single_post.tag.all()
    context = {'post': single_post, 'post_tags': post_tags}
    return render(request, 'blog/post-detail.html', context)

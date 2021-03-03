from blog.models import Post
from django.shortcuts import render


def post_list(request):
    qs = Post.objects.all()
    return render(request, 'blog/post_list.html', {'post_list': qs})

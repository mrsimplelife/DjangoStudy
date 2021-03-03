from instagram.models import Post
from django.http import HttpRequest
from django.shortcuts import render


def post_list(request: HttpRequest):
    q = request.GET.get('q', '')
    qs = Post.objects.all()
    if q:
        qs = qs.filter(message__icontains=q)
    return render(request, 'instagram/post_list.html', {
        'post_list': qs,
        'q': q
    })

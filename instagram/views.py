from django.views.generic import ListView
from django.http import HttpRequest, HttpResponse
# from django.shortcuts import render
from instagram.models import Post

post_list = ListView.as_view(model=Post)
# def post_list(request: HttpRequest) -> HttpResponse:
#     q = request.GET.get('q', '')
#     qs = Post.objects.all()
#     if q:
#         qs = qs.filter(message__icontains=q)
#     return render(request, 'instagram/post_list.html', {
#         'post_list': qs,
#         'q': q
#     })


def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    response = HttpResponse()
    response.write(f'{pk}')
    return response


def archives_year(request: HttpRequest, year: int) -> HttpResponse:
    return HttpResponse(f'{year}')
    # return HttpResponse(f'2020')

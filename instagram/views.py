# from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from django.http import Http404, HttpRequest, HttpResponse
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

post_detail = DetailView.as_view(model=Post)
# def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'instagram/post_detail.html', {
#         'post': post
#     })
#     # try:
#     #     post = Post.objects.get(pk=pk)
#     # except Post.DoesNotExist as err:
#     #     raise Http404 from err
#     # return render(request, 'instagram/post_detail.html', {
#     #     'post': post
#     # })
#     # response = HttpResponse()
#     # response.write(f'{pk}')
#     # return response


def archives_year(request: HttpRequest, year: int) -> HttpResponse:
    return HttpResponse(f'{year}')
    # return HttpResponse(f'2020')

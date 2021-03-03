# from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from django.http import Http404, HttpRequest, HttpResponse
from instagram.models import Post
from django.db.models import query


class PostListView(ListView):
    model = Post
    paginate_by = 10


post_list = PostListView.as_view()
# post_list = ListView.as_view(model=Post)
# def post_list(request: HttpRequest) -> HttpResponse:
#     q = request.GET.get('q', '')
#     qs = Post.objects.all()
#     if q:
#         qs = qs.filter(message__icontains=q)
#     return render(request, 'instagram/post_list.html', {
#         'post_list': qs,
#         'q': q
#     })


class PostDetailView(DetailView):
    model = Post
    # queryset = Post.objects.filter(is_public=True)
    # pass

    def get_queryset(self) -> query.QuerySet:
        qs = super().get_queryset()
        if not self.request.user.is_authenticated:
            qs = qs.filter(is_public=True)
        return qs


post_detail = PostDetailView.as_view()

# post_detail = DetailView.as_view(
#     model=Post, queryset=Post.objects.filter(is_public=True))
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

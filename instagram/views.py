from typing import Any, Union
from django.forms import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
# from django.shortcuts import get_object_or_404, redirect, render, resolve_url
from django.urls import reverse_lazy
# from django.utils.decorators import method_decorator
# from django.shortcuts import get_object_or_404, render
# from django.contrib.auth.decorators import login_required
from django.views.generic import (
    CreateView, ListView, YearArchiveView, ArchiveIndexView, DetailView, UpdateView, DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import query
from django.contrib import messages
from instagram.models import Post
from instagram.forms import PostForm


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('instagram:post_list')
    object: Union[Post, None] = None

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        response = super().get(request, *args, **kwargs)
        if self.object.author != request.user:
            messages.error(request, 'only author cna delete')
            return redirect(self.object)
        return response


post_delete = PostDeleteView.as_view()

# @login_required
# def post_delete(request: HttpRequest, pk: int) -> HttpResponse:
#     post = get_object_or_404(Post, pk=pk)
#     if post.author != request.user:
#         messages.error(request, 'only author cna delete')
#         return redirect(post)
#     if request.method == 'POST':
#         post.delete()
#         messages.success(request, 'post deleted')
#         return redirect('instagram:post_list')
#     return render(request, 'instagram/post_delete.html', {
#         'post': post
#     })


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    object: Union[Post, None] = None

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        response = super().get(request, *args, **kwargs)
        if self.object.author != request.user:
            messages.error(request, 'only author cna edit')
            return redirect(self.object)
        return response

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        messages.success(self.request, 'post edited')
        return super().form_valid(form)


post_edit = PostUpdateView.as_view()
# @login_required
# def post_edit(request: HttpRequest, pk: int) -> HttpResponse:
#     post = get_object_or_404(Post, pk=pk)

#     if post.author != request.user:
#         messages.error(request, 'only author cna edit')
#         return redirect(post)

#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES, instance=post)
#         if form.is_valid():
#             post = form.save()
#             messages.success(request, 'post edited')
#             return redirect(post)
#     else:
#         form = PostForm(instance=post)
#     return render(request, 'instagram/post_form.html', {
#         'form': form,
#         'post': post
#     })


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        post = form.save(commit=False)
        post.author = self.request.user
        messages.success(self.request, 'post saved')
        return super().form_valid(form)


post_new = PostCreateView.as_view()
# @login_required
# def post_new(request: HttpRequest):
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.save()
#             messages.success(request, 'post saved')
#             return redirect(post)
#     else:
#         form = PostForm()
#     return render(request, 'instagram/post_form.html', {
#         'form': form
#     })

# @method_decorator(login_required, name='dispatch')


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    paginate_by = 10

    # @method_decorator(login_required)
    # def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
    #     return super().dispatch(request, *args, **kwargs)


# post_list = login_required(PostListView.as_view())
post_list = PostListView.as_view()

# post_list = ListView.as_view(model=Post)


# @login_required
# def post_list(request: HttpRequest) -> HttpResponse:
#     q = request.GET.get('q', '')
#     qs = Post.objects.all()
#     if q:
#         qs = qs.filter(message__icontains=q)

#     messages.info(request, 'test!!!!!')
#     return render(request, 'instagram/post_list.html', {
#         'post_list': qs,
#         'q': q
#     })


# @method_decorator(login_required, name='dispatch')
class PostDetailView(LoginRequiredMixin, DetailView):
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


class PostArchiveIndexView(ArchiveIndexView):
    model = Post
    date_field = 'created_at'
    paginate_by = 10


post_arcive = PostArchiveIndexView.as_view()
# def archives_year(request: HttpRequest, year: int) -> HttpResponse:
#     return HttpResponse(f'{year}')
#     # return HttpResponse(f'2020')


class PostYearArchiveView(YearArchiveView):
    model = Post
    date_field = 'created_at'
    make_object_list = True


post_arcive__year = PostYearArchiveView.as_view()

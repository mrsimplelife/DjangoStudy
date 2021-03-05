from typing import Any
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model, login as auth_login
from django.contrib.auth.views import (LoginView, LogoutView)
from django.forms import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import (CreateView, TemplateView)
from accounts.models import Profile
from accounts.forms import LoginForm, ProfileForm, SignupForm

User = get_user_model()


class SignupView(CreateView):
    object = None
    model = User
    form_class = SignupForm
    template_name = 'accounts/signup_form.html'
    success_url = settings.LOGIN_URL

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        if request.user.is_authenticated:
            return redirect(self.success_url)
        return super().get(request, *args, **kwargs)

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        response = super().form_valid(form)
        auth_login(self.request, self.object)
        return response


signup = SignupView.as_view()
# def signup(request: HttpRequest):
# return HttpResponse('yet')


class MyLoginView(LoginView):
    template_name = 'accounts/login_form.html'
    form_class = LoginForm
    redirect_authenticated_user = True


login = MyLoginView.as_view()


class MyLogoutView(LogoutView):
    next_page = 'login'


logout = MyLogoutView.as_view()
# def logout(request: HttpRequest):
#     return HttpResponse('yet')


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/profile.html"


profile = ProfileView.as_view()
# @login_required
# def profile(request: HttpRequest):
#     return render(request, 'accounts/profile.html', {})


@login_required
def profile_edit(request):
    try:
        user_profile = request.user.profile
    except Profile.DoesNotExist:
        user_profile = None
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            form.save()
            return redirect('profile')
    form = ProfileForm(instance=user_profile)
    return render(request, 'accounts/profile_form.html', {'form': form})
# class ProfileUpdateView(LoginRequiredMixin, UpdateView):
#     model = Profile
#     form_class = ProfileForm


# profile_edit = ProfileUpdateView.as_view()

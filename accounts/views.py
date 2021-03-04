from django.conf import settings
from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
# from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, CreateView)

from accounts.models import Profile
from accounts.forms import ProfileForm, SignupForm

User = get_user_model()


class SignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'accounts/signup_form.html'
    success_url = settings.LOGIN_URL


signup = SignupView.as_view()
# def signup(request: HttpRequest):
# return HttpResponse('yet')


def logout(request: HttpRequest):
    return HttpResponse('yet')


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/profile.html"


# @login_required
# def profile(request: HttpRequest):
#     return render(request, 'accounts/profile.html', {})


@login_required
def profile_edit(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = None
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            form.save()
            return redirect('profile')
    form = ProfileForm(instance=profile)

    return render(request, 'accounts/profile_form.html', {'form': form})


# class ProfileUpdateView(LoginRequiredMixin, UpdateView):
#     model = Profile
#     form_class = ProfileForm


# profile_edit = ProfileUpdateView.as_view()

from django.shortcuts import redirect, render
from django.http import HttpRequest
# from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, UpdateView)
from accounts.models import Profile
from accounts.forms import ProfileForm


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

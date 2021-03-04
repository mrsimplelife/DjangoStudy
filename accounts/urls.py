from accounts import views
from django.urls import path
from django.contrib.auth.views import LoginView


class MyLoginView(LoginView):
    template_name = 'accounts/login_form.html'


urlpatterns = [
    path('login/', MyLoginView.as_view(), name="login"),
    path('profile/', views.ProfileView.as_view(), name="profile"),
    path('profile/edit', views.profile_edit, name="profile_edit"),
]

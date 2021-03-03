from django.urls.conf import path
from blog import views

urlpatterns = [
    path('', views.post_list, name="post_list")
]

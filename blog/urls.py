
from blog import views
from django.urls.conf import path

urlpatterns = [
    path('', views.post_list, name="post_list")
]

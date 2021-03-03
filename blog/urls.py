from django.urls.conf import path
from blog import views


app_name = 'blog'
urlpatterns = [
    path('', views.post_list, name='post_list')
]


from instagram import views
from django.urls import path, re_path


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    # re_path(r'(?P<pk>\d+)/$', views.post_detail,)
]

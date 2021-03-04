from django.urls import path, register_converter
from instagram import views
from instagram.converters import DayConverter, MonthConverter, YearConverter


register_converter(YearConverter, 'year')
register_converter(MonthConverter, 'month')
register_converter(DayConverter, 'day')
app_name = 'instagram'
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    # re_path(r'(?P<pk>\d+)/$', views.post_detail,)
    # path('archives/2020/', views.archives_year),
    # path('archives/2019/', views.archives_year)
    # path('archives/<int:year>/', views.archives_year)
    # re_path('archives/(?P<year>\\d+)/', views.archives_year)
    # re_path(r'archives/(?P<year>20\d{2})/', views.archives_year)
    # path('archives/<year:year>/', views.archives_year)
    path('archive/', views.post_arcive, name='post_arcive'),
    path('archive/<year:year>/', views.post_arcive__year, name="post_arcive__year"),
    path('new/', views.post_new, name='post_new')
]

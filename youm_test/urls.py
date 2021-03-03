"""youm_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from typing import Union
from django.conf import settings
from django.views.generic import TemplateView, RedirectView
from django.contrib import admin
from django.urls import URLPattern, URLResolver, path
from django.urls.conf import include
from django.conf.urls.static import static
import debug_toolbar


# class RootView(TemplateView):
#     template_name = 'root.html'

class RootView(RedirectView):
    pattern_name = 'instagram:post_list'


urlpatterns: list[Union[URLPattern, URLResolver]] = [
    path('admin/', admin.site.urls),

    # path('', TemplateView.as_view(template_name='root.html'), name='root'),
    # path('', RootView.as_view(), name='root'),
    # path('', RedirectView.as_view(
    #     # url='/instagram/'
    #     pattern_name='instagram:post_list'
    # ), name='root'),
    path('', RootView.as_view(), name='root'),
    path('blog/', include('blog.urls')),
    path('instagram/', include('instagram.urls')),
    path('accounts/', include('accounts.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

    urlpatterns += [path('__debug__/', include(debug_toolbar.urls)), ]

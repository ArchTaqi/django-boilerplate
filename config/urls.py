"""django_boilerplate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^post/', include('post.urls'))
"""
from django.conf import settings
from django.urls import include, path
from django.contrib import admin
from django.views.defaults import (permission_denied,
                                   page_not_found,
                                   server_error)
from django.conf.urls.static import static
from django.views.generic import TemplateView
admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path(r'api/', include('config.api')),
]

urlpatterns += [
    path(r'', TemplateView.as_view(template_name='base.html'), name='home'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    try:
        import debug_toolbar
        urlpatterns += [
            path(r'__debug__/', include(debug_toolbar.urls)),
        ]
    except ImportError:
        pass

    # Show error pages during development
    urlpatterns += [
        path(r'403/', permission_denied),
        path(r'404/', page_not_found),
        path(r'500/', server_error)
    ]

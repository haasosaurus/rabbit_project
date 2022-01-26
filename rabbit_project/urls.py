# -*- coding: utf-8 -*-


"""rabbit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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


# django related
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView


urlpatterns = [

    # admin site urls
    path('admin/', admin.site.urls),

    # main app urls
    # path('rabbit/', include('rabbit.urls')),
    path('', include('rabbit.urls')),
    # path(r'^&', RedirectView.as_view(url='rabbit/'), permanent=True),

    # redirect root to rabbit_app
    # path('', RedirectView.as_view(url='rabbit/', permanent=True)),

    # static urls
    *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
]

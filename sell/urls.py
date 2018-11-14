"""sell URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import RedirectView
from django.template.response import HttpResponse

urlpatterns = [
    # re_path(r'^(?P<category>)', include('shop.urls')),
    re_path(r'^favicon\.jpg', RedirectView.as_view(url='/static/img/favicon.jpg'), name='favicon'),
    path('', include('shop.urls')),
    re_path(r'^google-site-verification-file\.html$',
     lambda r: HttpResponse("google-site-verification: google-site-verification-file.html")),
    path('admin/', admin.site.urls)
]

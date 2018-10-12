from django.urls import path, re_path
from shop.views import catalogue


#''  (page-(\d+)/)?$  (?:page-(?P<page_number>\d+)/)?$  path('<category>/'...)
urlpatterns = [
    re_path(r'((?P<category>[a-zA-Z0-9_.-]+)/)?$', catalogue, name='shop-home'),
]

from django.urls import path, re_path
from shop.views import catalogue, category

# ''  (page-(\d+)/)?$  (?:page-(?P<page_number>\d+)/)?$  path('<category>/'...)
urlpatterns = [
    path('', catalogue, name='shop-home'),
    re_path(r'(^category/(?P<category>[a-zA-Z0-9_.-]+)/)?$', category, name='shop-home'),
]

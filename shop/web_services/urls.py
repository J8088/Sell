from django.conf.urls import url, include
from .catalogue.services import ProductsService, SingleProductService, \
    CategoriesService, FiltersService, ImageService


urlpatterns = [
    url(r'^products/$', ProductsService.as_view()),
    url(r'^categories/$', CategoriesService.as_view()),
    url(r'^image/$', ImageService.as_view()),
    url(r'^filters/$', FiltersService.as_view()),
    url(r'^product/(?P<product_id>\w+)/$|$', SingleProductService.as_view()),
]
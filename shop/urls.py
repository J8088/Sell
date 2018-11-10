from django.conf import settings
from django.urls import path, re_path
from django.conf.urls.static import static
from shop.views import catalogue, category, product

# ''  (page-(\d+)/)?$  (?:page-(?P<page_number>\d+)/)?$  path('<category>/'...)
urlpatterns = [
                  path('', catalogue.Catalogue.as_view(), name='shop-catalogue'),
                  re_path(r'^category/(?P<category>[a-zA-Z0-9_.-]+)/?$', category.Category.as_view(), name='shop-category'),
                  re_path(r'^product/(?P<product>[a-zA-Z0-9_.-]+)/?$', product.Product.as_view(), name='shop-product'),
                  path('about/', catalogue.Catalogue.as_view(), name='shop-catalogue'),
                  path('contacts/', catalogue.Catalogue.as_view(), name='shop-catalogue'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib.sitemaps import Sitemap
from shop.models import Product, Category
import datetime


class ProductSitemap(Sitemap):
    priority = 0.8

    def items(self):
        return Product.objects.all()

    def lastmod(self, obj):
        return obj.updated_date

    def location(self, obj):
        return "/product/{}".format(obj.product_id)


class HomeSitemap(Sitemap):
    priority = 1
    changefreq = 'daily'

    def items(self):
        return ['main']

    def lastmod(self, obj):
        return datetime.datetime.now()

    def location(self, item):
        return '/'


class CategorySitemap(Sitemap):
    priority = 0.8

    def items(self):
        return Category.objects.all()

    def lastmod(self, obj):
        return datetime.datetime.now()

    def location(self, obj):
        return "/category/{}/".format(obj.category_code)

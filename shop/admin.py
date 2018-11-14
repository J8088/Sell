from django.contrib import admin

# Register your models here.
from .models import Product, ProductToCategory, ProductToFilter, \
    ProductImage, ProductStates, FilterGroup, Filter, FilterToCategory, \
    Category, Settings


admin.site.register(Product)
admin.site.register(ProductToCategory)
admin.site.register(ProductToFilter)
admin.site.register(ProductImage)
admin.site.register(ProductStates)
admin.site.register(FilterGroup)
admin.site.register(Filter)
admin.site.register(FilterToCategory)
admin.site.register(Category)
admin.site.register(Settings)
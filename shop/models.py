"""
python manage.py makemigrations
python manage.py sqlmigrate shop 0003(migrations number)
python manage.py migrate

INSERT INTO tbl_name (a,b,c) VALUES(1,2,3),(4,5,6),(7,8,9);

"""

from django.db import models


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_parent_id = models.IntegerField(blank=True, null=True)
    category_name = models.CharField(max_length=500)
    category_code = models.CharField(max_length=500, blank=True, null=True)
    category_img = models.CharField(max_length=1000, blank=True, null=True)
    category_description = models.CharField(max_length=500)
    active = models.BooleanField(default=True)
    visible = models.BooleanField(default=False)


class ProductStates(models.Model):
    product_state_id = models.AutoField(primary_key=True)
    product_state_code = models.CharField(max_length=500, default=None)
    product_state_name = models.CharField(max_length=500, default=None)
    product_state_description = models.CharField(max_length=500, default=None)

    class Meta:
        db_table = 'shop_product_states'


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=500)
    product_description = models.CharField(max_length=500)
    product_state = models.ForeignKey(ProductStates, on_delete=models.CASCADE, blank=True, null=True)
    product_price = models.FloatField()
    product_currency = models.CharField(max_length=20, default='грн')
    product_img_path = models.CharField(max_length=2000, default=None)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField()
    active = models.BooleanField(default=True)
    visible = models.BooleanField(default=False)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_image_id = models.AutoField(primary_key=True)
    product_image_path = models.CharField(max_length=2000, default=None)

    class Meta:
        db_table = 'shop_product_image'


class ProductToCategory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'shop_product_to_category'


class FilterGroup(models.Model):
    filter_group_id = models.AutoField(primary_key=True)
    filter_group_name = models.CharField(max_length=500, default=None)
    filter_group_description = models.CharField(max_length=500, default=None)
    filter_group_code = models.CharField(max_length=500, blank=True, null=True)
    active = models.BooleanField(default=True)
    visible = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'shop_filter_group'


class Filter(models.Model):
    filter_group = models.ForeignKey(FilterGroup, on_delete=models.CASCADE)
    filter_id = models.AutoField(primary_key=True)
    filter_name = models.CharField(max_length=500, default=None)
    filter_description = models.CharField(max_length=500, default=None)
    filter_code = models.CharField(max_length=500, blank=True, null=True)
    active = models.BooleanField(default=True)
    visible = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)


class ProductToFilter(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    filter = models.ForeignKey(Filter, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'shop_product_to_filter'


class FilterToCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    filter = models.ForeignKey(Filter, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'shop_filter_to_category'


"""
python manage.py makemigrations
python manage.py sqlmigrate shop 0003(migrations number)
python manage.py migrate

INSERT INTO tbl_name (a,b,c) VALUES(1,2,3),(4,5,6),(7,8,9);

"""

from django.db import models
from django.forms.models import model_to_dict


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_parent_id = models.IntegerField(blank=True, null=True)
    category_name = models.CharField(max_length=500)
    category_code = models.CharField(unique=True, max_length=255, default=None)
    category_img = models.CharField(max_length=1000, blank=True, null=True)
    category_description = models.CharField(max_length=500)
    category_sector = models.CharField(max_length=100, blank=True, null=True)
    category_seo = models.CharField(max_length=500, blank=True, null=True)
    active = models.BooleanField(default=True)
    visible = models.BooleanField(default=False)

    def as_data(self):
        """Return the Product as a dict suitable for passing as kwargs.
        """
        data = model_to_dict(self)
        return data

    def __str__(self):
        return '{} ------ {} ------ {}'.format(self.category_name, self.category_code, self.category_id)


class ProductStates(models.Model):
    product_state_id = models.AutoField(primary_key=True)
    product_state_code = models.CharField(max_length=500, default=None)
    product_state_name = models.CharField(max_length=500, default=None)
    product_state_description = models.CharField(max_length=500, default=None)

    class Meta:
        db_table = 'shop_product_states'

    def __str__(self):
        return '{} ------ {} ------ {}'.format(self.product_state_name, self.product_state_code, self.product_state_id)


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=500)
    product_code = models.CharField(unique=True, max_length=255, blank=True, null=True)
    product_description = models.TextField(blank=True, null=True)
    product_state = models.ForeignKey(ProductStates, on_delete=models.CASCADE, blank=True, null=True)
    product_price = models.FloatField()
    product_currency = models.CharField(max_length=20, default='грн')
    product_slug = models.CharField(max_length=100, default='00000')
    product_seo = models.CharField(max_length=500, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField()
    active = models.BooleanField(default=True)
    visible = models.BooleanField(default=False)

    def as_data(self):
        """Return the Product as a dict suitable for passing as kwargs.
        """
        data = model_to_dict(self)
        return data

    def __str__(self):
        return '{} ------ {} ------ state: {}'.format(self.product_name, self.product_id, self.product_state)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_image_id = models.AutoField(primary_key=True)
    product_optional_image_path = models.CharField(max_length=2000, blank=True, null=True)
    product_photo = models.ImageField(upload_to='product_photos', default=None)
    product_image_order_no = models.IntegerField(default=1)

    def as_data(self):
        """Return the ProductImage as a dict suitable for passing as kwargs.
        """
        data = model_to_dict(self)
        return data

    class Meta:
        db_table = 'shop_product_image'

    def __str__(self):
        return '{} ------ {}'.format(self.product_photo, self.product.product_name)


class ProductToCategory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'shop_product_to_category'

    def __str__(self):
        return '{} ------ категорія: {}'.format(self.product.product_name, self.category.category_name)


class FilterGroup(models.Model):
    filter_group_id = models.AutoField(primary_key=True)
    filter_group_name = models.CharField(max_length=500, default=None)
    filter_group_description = models.CharField(max_length=500, default=None)
    filter_group_code = models.CharField(max_length=500, blank=True, null=True)
    active = models.BooleanField(default=True)
    visible = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    def as_data(self):
        """Return the FilterGroup as a dict suitable for passing as kwargs.
        """
        data = model_to_dict(self, exclude=['id', 'user'])
        return data

    class Meta:
        db_table = 'shop_filter_group'

    def __str__(self):
        return '{} ------ {} ------ {}'.format(self.filter_group_name, self.filter_group_code, self.filter_group_id)


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

    def as_data(self):
        """Return the Filter as a dict suitable for passing as kwargs.
        Result does not contain the filter_group.
        """
        data = model_to_dict(self, exclude=['filter_group'])
        return data

    def __str__(self):
        return '{} ------ {} ------ {}'.format(self.filter_name, self.filter_code, self.filter_id)


class ProductToFilter(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    filter = models.ForeignKey(Filter, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'shop_product_to_filter'

    def __str__(self):
        return '{} ------ {}'.format(self.product.product_name, self.filter.filter_name)


class Settings(models.Model):
    setting_name = models.CharField(max_length=100, default=None)
    setting_code = models.CharField(max_length=100, default=None)
    setting_value = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return '{} ------ {}'.format(self.setting_name, self.setting_code)

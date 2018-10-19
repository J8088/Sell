from shop.models import Product
from shop.utils.category_system import CategorySystem


class ProductSystem:
    def __init__(self, user=None):
        self.user = user

    def get_products(self):
        return Product.objects.all()

    """
    Returns products of all categories from the tree by category code.
    Deprecated
    Args:
        category_code: category code.

    Returns:
        products of all categories from the tree by category code.
    """

    def get_products_by_category_tree(self, category_code):
        category_system = CategorySystem()
        parent_category = category_system.get_single_category_by_code(category_code)
        categories = category_system.get_categories_tree(parent_category)

        category_ids = list(map(lambda category: category.category_id, categories))
        category_ids.append(parent_category.category_id)

        return Product.objects.filter(category__category_id__in=category_ids)

    def get_products_by_category(self, category_code):
        return Product.objects.filter(producttocategory__category__category_code=category_code)

    def get_products_by_categories_filters(self, category_codes=None, filter_codes=None):
        """

        :param category_codes: list of category codes
        :param filter_codes: list of filter codes
        :return: products QuerySet
        """
        if category_codes is None:
            category_codes = []
        if filter_codes is None:
            filter_codes = []

        products_set = Product.objects.filter(productimage__product_image_order_no=1). \
            values('product_id', 'product_name', 'product_description',
                   'product_state_id', 'product_price', 'product_currency',
                   'active', 'visible', 'productimage__product_photo', 'category_id',
                   'created_date', 'updated_date')

        if len(category_codes) > 0:
            products_set = products_set.filter(producttocategory__category__category_code__in=category_codes)

        if len(filter_codes) > 0:
            products_set = products_set.filter(producttofilter__filter__filter_code__in=filter_codes)
        products_set = products_set.distinct()

        return products_set

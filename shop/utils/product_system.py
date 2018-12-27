import operator
from functools import reduce
from django.db.models import Q, Subquery, OuterRef
from shop.models import Product, ProductImage, Category, Filter
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
        product_images = ProductImage.objects.filter(product=OuterRef('pk')).order_by('product_image_id')
        product_image_subquery = Subquery(product_images.values('product_photo')[:1])

        return Product.objects.filter(productimage__product_image_order_no=1,producttocategory__category__category_code=category_code).\
            values('product_id', 'product_name', 'product_primary_name', 'product_description',
                   'product_state_id', 'product_state__product_state_name', 'product_price', 'product_currency', 'product_slug', 'product_seo',
                   'active', 'visible', 'created_date', 'updated_date').annotate(product_photo=product_image_subquery)

    def get_products_by_categories_filters(self, category_codes=None, filter_codes=None, query=None):
        """

        :param category_codes: list of category codes
        :param filter_codes: list of filter codes
        :param query: search query
        :return: products QuerySet
        """
        if category_codes is None:
            category_codes = []
        if filter_codes is None:
            filter_codes = []
        # TODO Change logic in order to find image separately

        product_images = ProductImage.objects.filter(product=OuterRef('pk')).order_by('product_image_id')
        product_image_subquery = Subquery(product_images.values('product_photo')[:1])

        print('!@@@@@@@@')

        products_set = Product.objects. \
            values('product_id', 'product_name', 'product_primary_name', 'product_description',
                   'product_state_id', 'product_state__product_state_name', 'product_price', 'product_currency', 'product_slug', 'product_seo',
                   'active', 'visible', 'created_date', 'updated_date').annotate(product_photo=product_image_subquery)

        if len(category_codes) > 0:
            products_set = products_set.filter(producttocategory__category__category_code__in=category_codes)

        if len(filter_codes) > 0:
            products_set = products_set.filter(producttofilter__filter__filter_code__in=filter_codes)
        products_set = products_set.distinct()

        if query:
            query_list = query.split()
            products_set = products_set.filter(
                reduce(operator.and_,
                       (Q(product_name__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(product_description__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(product_price__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(product_slug__icontains=q) for q in query_list))
            )

        products_set = products_set.order_by('-updated_date')

        print("__file__={0}, ==> products_set.query => {1}".format(__file__, products_set.query))

        return products_set

    def get_product_by_id(self, product_id):
        product_set = Product.objects.filter(product_id=product_id).first().as_data()
        product_images_set = ProductImage.objects.filter(product_id=product_set['product_id'])
        product_set.update({'product_images': [prod_image.as_data() for prod_image in product_images_set]})

        return product_set

    @classmethod
    def get_categories_by_product_id(self, product_id):
        categories_set = Category.objects.filter(producttocategory__product_id=product_id).distinct()
        return categories_set

    @classmethod
    def get_filters_by_product_id(cls, product_id):
        return Filter.objects.filter(producttofilter__product_id=product_id).distinct()

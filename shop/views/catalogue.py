from django.views.generic import View
from django.template.response import TemplateResponse
from django.conf import settings
from ..utils.product_system import ProductSystem
from ..utils.category_system import CategorySystem
from ..utils.filters_system import FilterSystem
from ..utils import get_paginator_items


class Catalogue(View):
    template_name = 'catalogue.html'

    def get(self, request):
        """
        1. get full categories list
        2. get full filters list by categories list
        3. get full products list by filters list and categories list
        :param request:
        :param category:
        :return:
        """
        category_system = CategorySystem()
        product_system = ProductSystem()
        main_categories = category_system.get_categories()

        """
        filters for displaying in the menu
        """
        filters_with_groups = FilterSystem.get_filter_groups_with_filters_by_categories_dict()

        """
        filters for filtering products 
        """
        filters = FilterSystem.populate_filters_with_checked(filters_with_groups, request.GET)

        if len(filters) == 0:
            filter_objects = FilterSystem.get_filters_by_categories(
                list(map(lambda cat: cat.category_code, main_categories)))
            filters = list(map(lambda fl: fl.filter_code, filter_objects))

        products = product_system.get_products_by_categories_filters(
            list(map(lambda cat: cat.category_code, main_categories)),
            filters)
        page = request.GET.get('page', '1')
        products_paginated, page_range = get_paginator_items(products, settings.PAGINATE_BY, page)
        restricted = [key for key, value in settings.DISPLAY_FEATURES_DICT.items() if not value]
        primary_categories = [category for category in main_categories if category.category_sector == 'primary']
        secondary_categories = [category for category in main_categories if category.category_sector == 'secondary']
        ctx = {'categories': primary_categories,
               'secondary_categories': secondary_categories,
               'products': products_paginated,
               'page_range': page_range,
               'filters': filters_with_groups,
               'currentCategory': None,
               'restricted': restricted}
        return TemplateResponse(request, self.template_name, ctx)

from django.shortcuts import render
from django.views.generic import View
from django.template.response import TemplateResponse
from django.conf import settings
from ..utils.product_system import ProductSystem
from ..utils.category_system import CategorySystem
from ..utils.filters_system import FilterSystem
from ..utils import get_paginator_items
from ..utils.settings_system import SettingsSystem


class Category(View):
    template_name = 'catalogue.html'

    def get(self, request, category=None):
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
        category_object = category_system.get_single_category_by_code(category)
        main_categories = category_system.get_categories()

        phone_numbers_set = SettingsSystem.get_settings('phone.number')
        phone_numbers = list(map(lambda num: num.setting_value, phone_numbers_set))

        greetings_set = SettingsSystem.get_settings('greeting')
        greetings = list(map(lambda gr: gr.setting_value, greetings_set))

        """
        filters for displaying in the menu
        """
        filters_with_groups = FilterSystem.get_filter_groups_with_filters_by_categories_dict(
            [category] if category else None
        )

        """
        filters for products filtering
        """
        filters = FilterSystem.populate_filters_with_checked(filters_with_groups, request.GET)

        if len(filters) == 0:
            filter_objects = FilterSystem.get_filters_by_categories([category_object.category_code])
            filters = list(map(lambda fl: fl.filter_code, filter_objects))

        products = product_system.get_products_by_categories_filters([category_object.category_code], filters)
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
               'currentCategory': category_object,
               'restricted': restricted,
               'phone_numbers': phone_numbers,
               'greetings': greetings}
        return TemplateResponse(request, self.template_name, ctx)


class CatalogueWithVerticalCategories(View):
    template_name = 'catalogue_with_vertical_categories.html'

    def get(self, request, category=None):
        category_system = CategorySystem()
        product_system = ProductSystem()

        main_categories = category_system.get_categories()
        products = product_system.get_products_by_category(category) if category else product_system.get_products()
        category_object = category_system.get_single_category_by_code(category)

        if category is None:
            vertical_categories_tree = category_system.get_categories_tree_with_children(
                list(map(lambda cat: cat.category_code, main_categories))
            )
        else:
            vertical_categories_tree = category_system.get_categories_tree_with_children([category])

        breadcrumb_path = []
        if category:
            upward_tree = category_system.get_upward_tree_categories_by_child(category)
            upward_tree.sort(key=lambda cat: cat.category_parent_id if cat.category_parent_id else 0)
            breadcrumb_path = [
                {
                    'tokenId': token.category_id,
                    'tokenName': token.category_name,
                    'tokenCode': token.category_code,
                    'tokenType': 'category'
                }
                for token in upward_tree
            ]

        context = {
            'products': products,
            'categories': main_categories,
            'currentCategory': category_object,
            'verticalCategoriesTree': vertical_categories_tree,
            'breadcrumbPath': breadcrumb_path
        }
        return render(request, self.template_name, context)


class CategoriesCatalogue(View):
    template_name = 'categories-catalogue.html'

    def get(self, request, category=None):
        category_system = CategorySystem()

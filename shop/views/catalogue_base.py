from django.views.generic import View
from django.conf import settings
from ..utils.filters_system import FilterSystem
from ..utils import get_paginator_items
from ..utils.mixins import SystemMixin


class CatalogueBase(SystemMixin, View):
    def _get_seo(self, page, site_name):
        raise NotImplemented

    def _get_checked_filters(self, request):
        filters = FilterSystem.populate_filters_with_checked(self.data_cached_dict['filters'], request.GET)

        if len(filters) == 0:
            categories = [self.data_cached_dict['current_category']] if self.data_cached_dict['current_category'] else self.data_cached_dict['categories']
            filter_objects = FilterSystem.get_filters_by_categories(
                list(map(lambda cat: cat.category_code, categories)))
            filters = list(map(lambda fl: fl.filter_code, filter_objects))

        return filters

    def _get_products(self, categories, filters, query, page):
        """

        :param categories:
        :param filters:
        :param query:
        :param page:
        :return:
        """
        products = self.product_system_ins.get_products_by_categories_filters(
            list(map(lambda cat: cat.category_code, categories)),
            filters, query=query)
        products_paginated, page_range = get_paginator_items(products, settings.PAGINATE_BY, page)
        return products_paginated, page_range

    @classmethod
    def _get_restricted_items(cls):
        return [key for key, value in settings.DISPLAY_FEATURES_DICT.items() if not value]

    @classmethod
    def _get_categories_by_sector(cls, categories, sector_code):
        return [category for category in categories if category.category_sector == sector_code]

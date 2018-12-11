from django.template.response import TemplateResponse
from .catalogue_base import CatalogueBase


class Catalogue(CatalogueBase):
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
        page = request.GET.get('page', None)
        query = self.request.GET.get('q')

        (title_seo_base, description_seo_base, keywords_seo_base) = self._get_seo(page, self.settings_cached_dict['site_name'])

        filters = self._get_checked_filters(request)

        products_paginated, page_range = self._get_products(
            self.data_cached_dict['categories'], filters, query, page)

        primary_categories = self.__class__._get_categories_by_sector(
            self.data_cached_dict['categories'], 'primary')
        secondary_categories = self.__class__._get_categories_by_sector(
            self.data_cached_dict['categories'], 'secondary')

        ctx = {'categories': primary_categories,
               'secondary_categories': secondary_categories,
               'products': products_paginated,
               'page_range': page_range,
               'filters': self.data_cached_dict['filters'],
               'currentCategory': None,
               'restricted': self.__class__._get_restricted_items(),
               'phone_numbers': self.settings_cached_dict['phone_numbers'],
               'greetings': self.settings_cached_dict['greetings'],
               'footer_info': self.settings_cached_dict['footer_info'],
               'query': query or '',
               'title_seo': title_seo_base,
               'description_seo': description_seo_base,
               'keywords_seo': keywords_seo_base,
               'og_title_seo': ''}
        return TemplateResponse(request, self.template_name, ctx)

    def _get_seo(self, page, site_name):
        self.set_seo_codes('title.seo.base', 'description.seo.base', 'keywords.seo.base')
        seo_settings = self.seo_settings_cached_dict

        title_seo_base_set = seo_settings['title.seo.base']
        page_str = 'стор.{}'.format(page) if page else ''
        title_seo_base = "{} - {}{}".format(
            next(iter(list(map(lambda item: item.setting_value, title_seo_base_set))), ''), site_name, page_str)

        description_seo_base_set = seo_settings['description.seo.base']
        description_seo_base = "{} - {}".format(
            next(iter(list(map(lambda item: item.setting_value, description_seo_base_set))), ''), site_name)

        keywords_seo_base_set = seo_settings['keywords.seo.base']
        keywords_seo_base = "{}".format(
            next(iter(list(map(lambda item: item.setting_value, keywords_seo_base_set))), ''))

        return title_seo_base, description_seo_base, keywords_seo_base

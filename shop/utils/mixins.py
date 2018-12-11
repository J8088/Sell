from django.utils.functional import cached_property
from .product_system import ProductSystem
from .category_system import CategorySystem
from .filters_system import FilterSystem
from .settings_system import SettingsSystem


class SystemMixin:

    def __init__(self):
        self.category_system_class = CategorySystem
        self.product_system_class = ProductSystem
        self.filter_system_class = FilterSystem
        self.settings_system_class = SettingsSystem

        self.category_system_ins = CategorySystem()
        self.product_system_ins = ProductSystem()
        self.filter_system_ins = FilterSystem()

        self.current_category_code = None
        self.seo_settings = []

    def set_current_category(self, category_code):
        self.current_category_code = category_code

    def set_seo_codes(self, *args):
        self.seo_settings = args

    @cached_property
    def data_cached_dict(self):
        categories = self.category_system_ins.get_categories()
        current_category = self.category_system_ins.\
            get_single_category_by_code(self.current_category_code) if self.current_category_code else None
        filters = self.filter_system_class.get_filter_groups_with_filters_by_categories_dict([current_category.category_code] if current_category else None)
        return {
            "categories": categories,
            "filters": filters,
            "current_category": current_category
        }

    @cached_property
    def settings_cached_dict(self):
        phone_numbers_set = self.settings_system_class.get_settings('phone.number')
        phone_numbers = list(map(lambda num: num.setting_value, phone_numbers_set))

        greetings_set = self.settings_system_class.get_settings('greeting')
        greetings = list(map(lambda gr: gr.setting_value, greetings_set))

        site_name_set = self.settings_system_class.get_settings('site.name')
        site_name = next(iter(list(map(lambda item: item.setting_value, site_name_set))), '')

        footer_info_set = self.settings_system_class.get_settings('footer.info')
        footer_info = next(iter(list(map(lambda item: item.setting_value, footer_info_set))), '')

        return {
            "phone_numbers": phone_numbers,
            "site_name": site_name,
            "greetings": greetings,
            "footer_info": footer_info
        }

    @cached_property
    def seo_settings_cached_dict(self):
        settings_dict = {}
        for key in self.seo_settings:
            settings_dict[key] = self.settings_system_class.get_settings(key)

        return settings_dict




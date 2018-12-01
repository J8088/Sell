from django.views.generic import View
from django.template.response import TemplateResponse
from ..utils.settings_system import SettingsSystem
from ..utils.category_system import CategorySystem
from ..utils.product_system import ProductSystem
from ..models import Carousel


class Home(View):
    template_name = 'home.html'

    def get(self, request):
        ctx = {
            'greetings': self.__class__._get_settings_by_code('greeting'),
            'footer_info': self.__class__._get_first_setting_by_code('footer.info'),
            'phone_numbers': self.__class__._get_settings_by_code('phone.number'),
            'categories': self.__class__._get_categories_by_sector('primary', True),
            'categories_header': self.__class__._get_first_setting_by_code('categories.header'),
            'secondary_categories': self.__class__._get_categories_by_sector('secondary', True),
            'carousel_categories': self.__class__._get_categories_by_sector('carousel', False),
            'new_products': self.__class__._get_products_by_category_code('new'),
            'new_products_header': self.__class__._get_first_setting_by_code('new.products.header'),
            'top_products': self.__class__._get_products_by_category_code('top'),
            'top_products_header': self.__class__._get_first_setting_by_code('top.products.header'),
            'popular_products': self.__class__._get_products_by_category_code('popular'),
            'carousel_items': self.__class__._get_carousel_items()
        }

        return TemplateResponse(request, self.template_name, ctx)

    @classmethod
    def _get_categories_by_sector(cls, category_sector, visible):
        main_categories = CategorySystem().get_categories(visible=visible)
        return [category for category in main_categories if category.category_sector == category_sector]

    @classmethod
    def _get_settings_by_code(cls, code):
        settings_set = SettingsSystem.get_settings(code)
        return list(map(lambda item: item.setting_value, settings_set))

    @classmethod
    def _get_first_setting_by_code(cls, code):
        settings_set = SettingsSystem.get_settings(code)
        return next(iter(list(map(lambda item: item.setting_value, settings_set))), '')

    @classmethod
    def _get_products_by_category_code(cls, category_code):
        product_system = ProductSystem()
        return product_system.get_products_by_category(category_code)

    @classmethod
    def _get_carousel_items(cls):
        return Carousel.objects.filter(active=True, visible=True)

from django.views.generic import View
from django.template.response import TemplateResponse
from django.conf import settings
from ..utils.product_system import ProductSystem
from ..utils.category_system import CategorySystem
from ..utils.settings_system import SettingsSystem


class Product(View):
    template_name = 'product-details.html'

    def get(self, request, product=None):
        product_system = ProductSystem()
        main_categories = CategorySystem().get_categories()
        product_dict = product_system.get_product_by_id(product)

        phone_numbers_set = SettingsSystem.get_settings('phone.number')
        phone_numbers = list(map(lambda num: num.setting_value, phone_numbers_set))

        greetings_set = SettingsSystem.get_settings('greeting')
        greetings = list(map(lambda gr: gr.setting_value, greetings_set))

        site_name_set = SettingsSystem.get_settings('site.name')
        site_name = next(iter(list(map(lambda item: item.setting_value, site_name_set))), '')

        footer_info_set = SettingsSystem.get_settings('footer.info')
        footer_info = next(iter(list(map(lambda item: item.setting_value, footer_info_set))), '')

        title_seo_set = SettingsSystem.get_settings('product.seo.title')
        title_seo = "{} {} – {}".format(product_dict['product_name'],
                                        next(iter(list(map(lambda item: item.setting_value, title_seo_set))), ''),
                                        site_name)

        description_seo_set = SettingsSystem.get_settings('product.seo.description')
        description_seo = "{} {}".format(product_dict['product_name'],
                                         next(iter(list(map(lambda item: item.setting_value, description_seo_set))),
                                              ''))

        keywords_seo_set = SettingsSystem.get_settings('product.seo.keywords')
        keywords_seo = "{} {}".format(product_dict['product_name'],
                                      next(iter(list(map(lambda item: item.setting_value, keywords_seo_set))),
                                           ''))

        og_title_seo_set = SettingsSystem.get_settings('product.seo.title')
        og_title_seo = "{} {}".format(product_dict['product_name'],
                                      next(iter(list(map(lambda item: item.setting_value, og_title_seo_set))),
                                           ''))

        show_full = settings.PRODUCT_DETAILS['full']
        description = settings.PRODUCT_DETAILS['descriptionTitle']
        categories = product_system.get_categories_by_product_id(product)
        primary_categories = [category for category in main_categories if category.category_sector == 'primary']
        secondary_categories = [category for category in main_categories if category.category_sector == 'secondary']
        breadcrumb_path = [
            {
                'tokenId': token.category_id,
                'tokenName': token.category_name,
                'tokenCode': token.category_code,
                'tokenType': 'category'
            }
            for token in categories
        ]
        breadcrumb_path.append({
            'tokenId': product_dict['product_id'],
            'tokenName': product_dict['product_name'],
            'tokenCode': str(product_dict['product_id']),
            'tokenType': 'product'
        })
        ctx = {
            'categories': primary_categories,
            'secondary_categories': secondary_categories,
            'product': product_dict,
            'footer_info': footer_info,
            'currentCategory': None,
            'showFull': show_full,
            'description': description,
            'breadcrumbPath': breadcrumb_path,
            'phone_numbers': phone_numbers,
            'greetings': greetings,
            'title_seo': title_seo,
            'description_seo': description_seo,
            'keywords_seo': keywords_seo,
            'og_title_seo': og_title_seo
        }
        return TemplateResponse(request, self.template_name, ctx)

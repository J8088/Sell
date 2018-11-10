from django.views.generic import View
from django.template.response import TemplateResponse
from django.conf import settings
from ..utils.product_system import ProductSystem
from ..utils.category_system import CategorySystem


class Product(View):
    template_name='product-details.html'

    def get(self, request, product=None):
        product_system = ProductSystem()
        main_categories = CategorySystem().get_categories()
        product_dict = product_system.get_product_by_id(product)
        show_full = settings.PRODUCT_DETAILS['full']
        categories = product_system.get_categories_by_product_id(product)
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
            'categories': main_categories,
            'product': product_dict,
            'currentCategory': None,
            'showFull': show_full,
            'breadcrumbPath': breadcrumb_path
        }
        return TemplateResponse(request, self.template_name, ctx)
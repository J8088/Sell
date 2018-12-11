from django.shortcuts import render
from django.views.generic import View
from ..utils.product_system import ProductSystem
from ..utils.category_system import CategorySystem


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
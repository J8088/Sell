from django.shortcuts import render
from django.template.response import TemplateResponse
from .utils.product_system import ProductSystem
from .utils.category_system import CategorySystem
from .utils.filters_system import FilterSystem


def catalogue(request, category=None):
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
        filter_objects = FilterSystem.get_filters_by_categories(
            list(map(lambda cat: cat.category_code, main_categories)))
        filters = list(map(lambda fl: fl.filter_code, filter_objects))

    products = product_system.get_products_by_categories_filters(
        list(map(lambda cat: cat.category_code, main_categories)),
        filters)
    ctx = {'categories': main_categories,
           'products': products,
           'filters': filters_with_groups,
           'currentCategory': category_object}
    return TemplateResponse(request, 'catalogue.html', ctx)


def catalogue_with_vertical_categories(request, category=None):
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
                'categoryId': token.category_id,
                'categoryName': token.category_name,
                'categoryCode': token.category_code
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
    return render(request, 'catalogue_with_vertical_categories.html', context)

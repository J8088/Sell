from django import template

register = template.Library()

CONTEXT_KEY = 'DJANGO_BREADCRUMB_LINKS'


@register.inclusion_tag('horizontal-menu.html', takes_context=True)
def horizontal_menu(context, items, current_category):
    return {'menu_items': items, 'current_category': current_category}


@register.inclusion_tag('vertical-menu.html', takes_context=True)
def vertical_menu(context, items, current_category, child=None):
    return {'menu_items': items, 'current_category': current_category, 'child': child}


@register.inclusion_tag('vertical_filters.html', takes_context=True)
def vertical_filters(context, items, current_category, current_filters=None, restricted=None):
    if current_filters is None:
        current_filters = []
    return {'filters': items,
            'current_category': current_category,
            'current_filters': current_filters,
            'restricted': restricted}


@register.inclusion_tag('breadcrumbs.html', takes_context=True)
def breadcrumb(context, path, token):
    breadcrumbs = [
        {'id': '', 'name': 'SELL', 'code': 'sell', 'url': '/'}
    ]

    if path:
        for item in path:
            if item['tokenType'] == 'category':
                url = '/{}/{}/'.format('category', item['tokenCode']) if item['tokenCode'] else ''
            else:
                url = '/{}/{}/'.format('product', str(item['tokenId'])) if item['tokenId'] else ''
            breadcrumbs.append({
                'id': item['tokenId'],
                'name': item['tokenName'],
                'code': item['tokenCode'],
                'url': url
            })

    if token and not path:
        breadcrumbs.append({
            'id': '',
            'name': token.category_name,
            'code': token.category_code,
            'url': token.category_code + '/' if token.category_code else ''})

    breadcrumbs[-1]['url'] = ''

    return {'breadcrumbs': breadcrumbs}

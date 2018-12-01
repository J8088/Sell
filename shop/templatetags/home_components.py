from django import template

register = template.Library()


@register.inclusion_tag('carousel.html', takes_context=True)
def carousel(context, carousels, section_id):
    return {'carousel_items': carousels, 'section_id': section_id}


@register.inclusion_tag('home-categories-section.html', takes_context=True)
def carousel_categories_section(context, categories, section_title):
    return {'categories': categories, 'section_title': section_title}


@register.inclusion_tag('home-products-section.html', takes_context=True)
def home_products_section(context, products, section_title):
    return {'products': products, 'section_title': section_title}


@register.inclusion_tag('home-footer-section.html', takes_context=True)
def home_footer_section(context, info=''):
    return {'context_info': info}

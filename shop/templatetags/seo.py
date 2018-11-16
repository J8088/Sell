from django import template

register = template.Library()


@register.inclusion_tag('seo-header.html', takes_context=True)
def seo_header(context, **kwargs):
    return {'title_seo': kwargs['title_seo'],
            'description_seo': kwargs['description_seo'],
            'keywords_seo': kwargs['keywords_seo'],
            'og_title_seo': kwargs['og_title_seo']}
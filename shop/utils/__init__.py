from django.core.paginator import InvalidPage, Paginator
from django.http import Http404


def get_paginator_items(items, paginate_by, page_number, slice_number=3):
    if not page_number:
        page_number = 1
    paginator = Paginator(items, paginate_by)
    try:
        page_number = int(page_number)
    except ValueError:
        raise Http404('Page can not be converted to an int.')

    try:
        items = paginator.page(page_number)
    except InvalidPage as err:
        raise Http404('Invalid page (%(page_number)s): %(message)s' % {
            'page_number': page_number, 'message': str(err)})

    # Get index of the current page
    # TODO correct the logic of displaying right pages number
    index = items.number - 1
    max_index = len(paginator.page_range)
    start_index = index - slice_number if index >= slice_number else 0
    end_index = index + slice_number if index <= max_index - slice_number else max_index
    page_range = list(paginator.page_range)[start_index:end_index]
    return items, page_range

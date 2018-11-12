from ..models import Filter, FilterGroup, ProductToFilter, ProductToCategory


class FilterSystem:
    @classmethod
    def get_filters_by_group_code(cls, filter_group_code):
        return Filter.objects.filter(filter_group__filter_group_code=filter_group_code)

    @classmethod
    def get_filters_by_categories(cls, category_codes=None):
        if category_codes is None:
            category_codes = []

        filters_set = Filter.objects.all()
        if len(category_codes) > 0:
            filters_set = filters_set.filter(filtertocategory__category__category_code__in=category_codes)

        return filters_set

    @classmethod
    def get_filter_groups_with_filters_by_categories_dict(cls, category_codes=None):
        result = []
        if category_codes is None:
            category_codes = []
        filter_groups_set = FilterGroup.objects.all()
        filters_set = Filter.objects.filter(visible=True)
        product_to_filter = ProductToFilter.objects.filter(product__visible=True)

        if len(category_codes) > 0:
            filters_set = filters_set.filter(filtertocategory__category__category_code__in=category_codes)
            product_to_category = ProductToCategory.objects.filter(category__category_code__in=category_codes)
            product_to_filter = product_to_filter.filter(product__producttocategory__in=product_to_category)

        filters_set = filters_set.filter(producttofilter__in=product_to_filter).distinct()

        for filter_group in filter_groups_set:
            filters = filters_set.filter(filter_group_id=filter_group.filter_group_id)
            filters_list = [filter_obj.as_data() for filter_obj in filters]
            if len(filters_list) > 0:
                result.append({'filter_group': filter_group.as_data(), 'filters': filters_list})
        return result

    @classmethod
    def get_filter_groups(cls):
        return FilterGroup.objects.all()

    @classmethod
    def populate_filters_with_checked(cls, filters_with_groups, filters_query_dict):
        filter_codes = []
        for filter_group_dict in filters_with_groups:
            filters_list = filters_query_dict.getlist(filter_group_dict['filter_group']['filter_group_code'], [])
            for filter_code in filters_list:
                filter_codes.append(filter_code)
            for filter_dict in filter_group_dict['filters']:
                if filter_dict['filter_code'] in filter_codes:
                    filter_dict.update({'checked': True})
        return filter_codes

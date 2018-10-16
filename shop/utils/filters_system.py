from ..models import Filter, FilterGroup


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
        filters_set = Filter.objects.all()

        if len(category_codes) > 0:
            filters_set = filters_set.filter(filtertocategory__category__category_code__in=category_codes)

        for filter_group in filter_groups_set:
            filters = filters_set.filter(filter_group_id=filter_group.filter_group_id)
            filters_list = [filter_obj.as_data() for filter_obj in filters]
            if len(filters_list) > 0:
                result.append({'filter_group': filter_group.as_data(), 'filters': filters_list})
        return result




    @classmethod
    def get_filter_groups(cls):
        return FilterGroup.objects.all()

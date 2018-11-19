from shop.models import Category


class CategorySystem:
    def __init__(self, user=None):
        self.user = user

    def get_categories(self):
        """
        Returns all parent categories
        :return: parent categories QuerySet
        """
        return Category.objects.filter(category_parent_id__isnull=True, active=True, visible=True)

    def get_single_category_by_code(self, category_code):
        return Category.objects.filter(category_code__exact=category_code).first()

    def _get_category_by_id(self, category_id):
        return Category.objects.filter(category_id=category_id).first()

    def _get_root_nodes(self):
        return Category.objects.filter(category_parent_id__isnull=True)

    def _get_children_nodes(self, parent_node):
        return Category.objects.filter(category_parent_id__exact=parent_node.category_id)

    def _get_children_nodes_by_parent_code(self, parent_code):
        parent_category = self.get_single_category_by_code(parent_code)
        return Category.objects.filter(category_parent_id__exact=parent_category.category_id)

    def _get_tree_recursively(self, results, parent):
        if parent:
            nodes = self._get_children_nodes(parent)
        else:
            nodes = self._get_root_nodes()
        for node in nodes:
            results.append(node)
            self._get_tree_recursively(results, node)

    def _get_tree_recursively_with_children_by_code(self, results, parent_code):
        if parent_code:
            nodes = self._get_children_nodes_by_parent_code(parent_code)
        else:
            nodes = self._get_root_nodes()
        for node in nodes:
            item = {'node': node, 'children': []}
            results.append(item)
            self._get_tree_recursively_with_children_by_code(item['children'], node.category_code)

    def get_categories_tree(self, parent=None):
        results = []
        self._get_tree_recursively(results, parent)
        return results

    def get_categories_tree_with_children(self, category_codes=None):
        """
        Used to render vertical categories tree
        :param category_codes: all parent categories, for example - horizontal menu
        :return:
        """
        if category_codes is None:
            category_codes = [None]
        returns = []
        for category_code in category_codes:
            results = []
            self._get_tree_recursively_with_children_by_code(results, category_code)
            returns.extend(results)

        return returns

    def get_upward_tree_categories_by_child(self, category_code, result=None):
        """
        Used to render breadcrumb path from a child to parent
        :param category_code:
        :param result:
        :return:
        """
        if result is None:
            result = []
        category = self.get_single_category_by_code(category_code)
        result.append(category)
        if category.category_parent_id:
            parent_category = self._get_category_by_id(category.category_parent_id)
            result = self.get_upward_tree_categories_by_child(parent_category.category_code, result)

        return result


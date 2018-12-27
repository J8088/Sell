from rest_framework.response import Response
from rest_framework.views import APIView
from ...utils.product_system import ProductSystem
from ...utils.category_system import CategorySystem
from ...utils.filters_system import FilterSystem
from ...models import ProductImage, Product, ProductToCategory, ProductToFilter
from datetime import datetime
from django.utils import formats
# from .auth import CsrfExemptSessionAuthentication
from django.views.decorators.csrf import csrf_exempt


class ProductsService(APIView):
    def get(self, request):
        product_system = ProductSystem()
        products = product_system.get_products()
        count = len(products)
        # products_dict =
        return Response({
            'items': [product.as_data() for product in products],
            'totalResults': count
        })


class SingleProductService(APIView):
    def get(self, request, product_id):
        product = self._get_product_by_id(product_id)
        return Response(product)

    def post(self, request, product_id):
        print(request.data)
        print(product_id)

        data_product_id = request.data.get('product_id')

        if data_product_id:
            product = self._update(data=request.data)
        else:
            product = self._create(data=request.data)

        return Response(product)

    def _get_product_by_id(self, product_id):
        product_system = ProductSystem()
        product = product_system.get_product_by_id(product_id)
        categories = ProductSystem.get_categories_by_product_id(product_id)
        filters = ProductSystem.get_filters_by_product_id(product_id)

        categories_dict = [category.as_data() for category in categories]

        for category in categories_dict:
            category.update({'category_img': category['category_img'].url if category['category_img'] else ''})

        filters_dict = [filters.as_data() for filters in filters]

        product.update({'categories': categories_dict, 'filters': filters_dict})

        for product_img in product['product_images']:
            product_img.update({'product_photo': product_img['product_photo'].url})

        product.update({'updated_date': formats.date_format(product.get('updated_date'), "DATETIME_FORMAT")})

        return product

    def _update(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        data = kwargs.get('data')
        product_id = data.get('product_id')
        try:
            obj = Product.objects.get(product_id=product_id)
            for key, value in data.items():
                if key not in ['categories',
                               'updated_date',
                               'product_images',
                               'categories',
                               'filters',
                               'product_state']:
                    setattr(obj, key, value)
            obj.updated_date = datetime.now()
            obj.save()
        except Product.DoesNotExist as e:
            return Response({'Error': 'Product Does Not Exist'})

        # Categories
        categories = ProductToCategory.objects.filter(product_id=product_id)
        front_category_ids = [cat['category_id'] for cat in data.get('categories')]
        server_category_ids = [cat.category_id for cat in categories]
        category_ids_to_add = list(set(front_category_ids) - set(server_category_ids))
        category_ids_to_remove = list(set(server_category_ids) - set(front_category_ids))

        ProductToCategory.objects.bulk_create([
            ProductToCategory(product_id=product_id,
                              category_id=_category_id) for _category_id in category_ids_to_add
        ])

        for _category_id in category_ids_to_remove:
            ProductToCategory.objects.filter(product_id=product_id, category_id=_category_id).delete()

        # Filters
        filters = ProductToFilter.objects.filter(product_id=product_id)
        front_filter_ids = [filter['filter_id'] for filter in data.get('filters')]
        server_filter_ids = [filter.filter_id for filter in filters]
        filter_ids_to_add = list(set(front_filter_ids) - set(server_filter_ids))
        filter_ids_to_remove = list(set(server_filter_ids) - set(front_filter_ids))
        ProductToFilter.objects.bulk_create([
            ProductToFilter(product_id=product_id,
                            filter_id=_filter_id) for _filter_id in filter_ids_to_add
        ])

        for _filter_id in filter_ids_to_remove:
            ProductToFilter.objects.filter(product_id=product_id, filter_id=_filter_id).delete()

        # Images
        product_images = ProductImage.objects.filter(product_id=product_id)
        front_product_image_ids = [image['product_image_id'] for image in data.get('product_images')]
        server_product_image_ids = [image.product_image_id for image in product_images]
        product_image_ids_to_add = list(set(front_product_image_ids) - set(server_product_image_ids))

        for image_id in product_image_ids_to_add:
            product_image = ProductImage.objects.get(product_image_id=image_id)
            product_image.product_id = product_id
            product_image.save()

        return self._get_product_by_id(product_id)

    def _create(self, **kwargs):
        """

        :param kwargs:
        :return:
        """

        data = kwargs.get('data')
        product_id = -1
        try:
            obj = Product()
            for key, value in data.items():
                if key not in ['categories',
                               'updated_date',
                               'product_images',
                               'categories',
                               'filters',
                               'product_state']:
                    setattr(obj, key, value)
            obj.updated_date = datetime.now()
            obj.save()
            product_id = obj.product_id
        except Product.DoesNotExist as e:
            return Response({'Error': 'Product Does Not Exist'})


        # Categories
        front_category_ids = [cat['category_id'] for cat in data.get('categories')]
        ProductToCategory.objects.bulk_create([
            ProductToCategory(product_id=product_id,
                              category_id=_category_id) for _category_id in front_category_ids
        ])

        # Filters
        front_filter_ids = [filter['filter_id'] for filter in data.get('filters')]
        ProductToFilter.objects.bulk_create([
            ProductToFilter(product_id=product_id,
                            filter_id=_filter_id) for _filter_id in front_filter_ids
        ])

        # Images
        front_product_image_ids = [image['product_image_id'] for image in data.get('product_images')]

        for image_id in front_product_image_ids:
            product_image = ProductImage.objects.get(product_image_id=image_id)
            product_image.product_id = product_id
            product_image.save()

        return self._get_product_by_id(product_id)


class CategoriesService(APIView):
    def get(self, request):
        category_system = CategorySystem()
        categories = category_system.get_categories()

        categories_dict = [category.as_data() for category in categories]

        for category in categories_dict:
            category.update({'category_img': category['category_img'].url if category['category_img'] else ''})

        return Response({
            'items': categories_dict,
            'totalResults': len(categories_dict)})


class FiltersService(APIView):
    def get(self, request):
        filters = FilterSystem.get_filters()
        filters_dict = [filter.as_data() for filter in filters]
        return Response({
            'items': filters_dict,
            'totalResults': len(filters_dict)
        })


class ImageService(APIView):
    # authentication_classes = (CsrfExemptSessionAuthentication)
    # @csrf_exempt
    def post(self, request):
        try:
            file = request.data['file']
            image = ProductImage.objects.create(product_photo=file)
        except Exception as e:
            return Response({'error': e})

        return Response({'product_photo': image.product_photo.url, 'product_image_id': image.product_image_id})

    def delete(self, request):
        try:
            ProductImage.objects.filter(product_image_id=request.data.get('product_image_id')).delete()
        except Exception as e:
            return Response({'error': e})

        return Response({'message': 'OK'})

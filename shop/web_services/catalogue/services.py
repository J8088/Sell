from rest_framework.response import Response
from rest_framework.views import APIView
from ...utils.product_system import ProductSystem
from ...utils.category_system import CategorySystem
from ...utils.filters_system import FilterSystem
from ...models import ProductImage
# from .auth import CsrfExemptSessionAuthentication
from django.views.decorators.csrf import csrf_exempt


class ProductsService(APIView):
    def get(self, request):
        product_system = ProductSystem()
        products = product_system.get_products()
        count = len(products)
        return Response({
            'items': [product.as_data() for product in products],
            'totalResults': count
        })


class SingleProductService(APIView):
    def get(self, request, product_id):
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
        return Response(product)

    def post(self, request, product_id):
        print(request.data)
        print(product_id)
        return Response({'message': 'OK'})


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
            ProductImage.objects. \
                filter(product_image_id=request.data.get('product_image_id'))
                # . \
                # delete()
        except Exception as e:
            return Response({'error': e})

        return Response({'message': 'OK'})

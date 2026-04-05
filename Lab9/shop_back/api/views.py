import json
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .models import Product, Category
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from api.models import Category, Product
from api.serializers import CategorySerializer, ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    @action(detail=True, methods=['get'])
    def products(self, request, pk=None):
        category = self.get_object()
        products = category.products.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

def product_to_dict(p):
    return {
        'id': p.id,
        'name': p.name,
        'price': p.price,
        'description': p.description,
        'count': p.count,
        'is_active': p.is_active,
        'category_id': p.category_id,
    }


def category_to_dict(c):
    return {
        'id': c.id,
        'name': c.name,
    }


@require_GET
def product_list(request):
    products = list(Product.objects.all())
    return JsonResponse([product_to_dict(p) for p in products], safe=False)


@require_GET
def product_detail(request, id):
    try:
        product = Product.objects.get(pk=id)
        return JsonResponse(product_to_dict(product))
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Not found'}, status=404)


@require_GET
def category_list(request):
    categories = list(Category.objects.all())
    return JsonResponse([category_to_dict(c) for c in categories], safe=False)


@require_GET
def category_detail(request, id):
    try:
        category = Category.objects.get(pk=id)
        return JsonResponse(category_to_dict(category))
    except Category.DoesNotExist:
        return JsonResponse({'error': 'Not found'}, status=404)


@require_GET
def category_products(request, id):
    try:
        category = Category.objects.get(pk=id)
        products = list(category.products.all())
        return JsonResponse([product_to_dict(p) for p in products], safe=False)
    except Category.DoesNotExist:
        return JsonResponse({'error': 'Not found'}, status=404)
    
@require_GET
def product_list(request):
    products = Product.objects.all()
    
    min_pr = request.GET.get('min') 
    max_pr = request.GET.get('max') 
    if min_pr:
        products = products.filter(price__gte=min_pr) 
    if max_pr:
        products = products.filter(price__lte=max_pr) 
    
    return JsonResponse([product_to_dict(p) for p in list(products)], safe = False)
    
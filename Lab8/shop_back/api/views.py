import json
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .models import Product, Category


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
from catalog.models import Product
from django.core.cache import cache

CATEGORY_CACHE_TIMEOUT = 60 * 15

PRODUCTS_LIST_CACHE_KEY = 'products_list'
PRODUCTS_LIST_CACHE_TIMEOUT = 60 * 15

def get_products_by_category(category_id):
    """Возвращает все товары указанной категории."""
    cache_key = f'category_{category_id}'

    products = cache.get(cache_key)

    if products is None:
        products = list(
            Product.objects.filter(
                category_id=category_id
            ).order_by('-created_at')
        )

        cache.set(
            cache_key,
            products,
            timeout=CATEGORY_CACHE_TIMEOUT,
        )

    return products

def get_products_from_cache():
    """Возвращает список товаров из кеша или базы данных."""
    products = cache.get(PRODUCTS_LIST_CACHE_KEY)

    if products is None:
        products = list(
            Product.objects.all().order_by('-created_at')
        )

        cache.set(
            PRODUCTS_LIST_CACHE_KEY,
            products,
            timeout=PRODUCTS_LIST_CACHE_TIMEOUT,
        )

    return products


def clear_products_list_cache():
    """Удаляет сохранённый список товаров из кеша."""
    cache.delete(PRODUCTS_LIST_CACHE_KEY)

CATEGORY_CACHE_TIMEOUT = 60 * 15


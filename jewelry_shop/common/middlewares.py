from jewelry_shop.shop.models import Product


def last_viewed_products_middleware(get_response):
    def middleware(request):
        product_photo_ids = request.session.get('last_viewed_products_ids', [])
        products = Product.objects.filter(id__in=product_photo_ids)
        request.last_viewed_products_ids = products
        return get_response(request)

    return middleware

from django.urls import path

from jewelry_shop.shopping_cart.views import add_to_cart, order_details, delete_from_cart, checkout, \
    update_transaction_records, success, process_payment

urlpatterns = [
    path('add-to-cart/<item_id>', add_to_cart, name='add_to_cart'),
    path('order-summary/', order_details, name='order_summary'),
    path('success/', success, name='purchase_success'),
    path('item/delete/<item_id>/', delete_from_cart, name='delete_item'),
    path('checkout/', checkout, name='checkout'),
    path('payment/<order_id>', process_payment, name='process payment'),
    path('update-transaction/<order_id>/', update_transaction_records, name='update_records'),
]

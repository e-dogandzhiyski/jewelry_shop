from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from jewelry_shop.accounts.models import Profile
from jewelry_shop.shop.models import Product
from jewelry_shop.shopping_cart.extras import generate_order_id
from jewelry_shop.shopping_cart.models import Order, OrderItem


def get_user_pending_order(request):
    user_profile = get_object_or_404(Profile, user=request.user)
    order = Order.objects.filter(owner=user_profile, is_ordered=False)
    if order.exists():
        return order[0]
    return 0


@login_required()
def add_to_cart(request, **kwargs):
    user_profile = get_object_or_404(Profile, user=request.user)
    product = Product.objects.filter(id=kwargs.get('item_id', "")).first()

    order_item, status = OrderItem.objects.get_or_create(product=product)
    user_order, status = Order.objects.get_or_create(owner=user_profile, is_ordered=False)
    user_order.items.add(order_item)
    if status:
        user_order.ref_code = generate_order_id()
        user_order.save()

    # messages.info(request, "item added to cart")
    return redirect(reverse('dashboard'))


@login_required()
def delete_from_cart(request, item_id):
    item_to_delete = OrderItem.objects.filter(pk=item_id)
    if item_to_delete.exists():
        item_to_delete[0].delete()
        # messages.info(request, "Item has been deleted")
    return redirect(reverse('order_summary'))


@login_required()
def order_details(request, **kwargs):
    existing_order = get_user_pending_order(request)
    context = {
        'order': existing_order
    }
    return render(request, 'shopping_cart/order_summary.html', context)


@login_required()
def checkout(request):
    existing_order = get_user_pending_order(request)
    context = {
        'order': existing_order,
    }
    return render(request, 'shopping_cart/checkout.html', context)


@login_required()
def process_payment(request, order_id):
    return redirect(reverse('update_records', kwargs={'order_id': order_id, }))


@login_required()
def checkout(request):
    existing_order = get_user_pending_order(request)
    context = {
        'order': existing_order,
    }
    return render(request, 'shopping_cart/checkout.html', context)


@login_required()
def update_transaction_records(request, order_id):
    # get the order being processed
    order_to_purchase = Order.objects.filter(pk=order_id).first()

    # update the placed order
    order_to_purchase.is_ordered = True
    order_to_purchase.date_ordered = datetime.now()
    order_to_purchase.save()

    # get all items in the order - generates a queryset
    order_items = order_to_purchase.items.all()

    # update order items
    order_items.update(is_ordered=True, date_ordered=datetime.now())

    # Add products to user profile
    user_profile = get_object_or_404(Profile, user=request.user)
    # get the products from the items
    order_products = [item.product for item in order_items]
    user_profile.products.add(*order_products)
    user_profile.save()

    # messages.info(request, "Thank you! Your purchase was successful!")
    print("Thank you! Your purchase was successful!")                                       # returns message but i don't know how to do messages
    return redirect(reverse('dashboard'))


def success(request, **kwargs):
    # a view signifying the transaction was successful
    return render(request, 'shopping_cart/purchase_success.html', {})

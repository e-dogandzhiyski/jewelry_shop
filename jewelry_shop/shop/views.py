from django.contrib.auth import mixins as auth_mixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from jewelry_shop.common.views_mixins import RedirectToDashboard
from jewelry_shop.shop.forms import DeleteProductForm
from jewelry_shop.shop.models import Product
from jewelry_shop.shopping_cart.models import Order


class HomeView(RedirectToDashboard, views.TemplateView):
    template_name = 'shop/home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_additional_nav_items'] = True
        return context


class DashboardView(views.ListView):
    model = Product
    template_name = 'shop/dashboard.html'
    context_object_name = 'products'


class DashboardNoProfileView(views.ListView):
    model = Product
    template_name = 'shop/dashboard_no_user.html'
    context_object_name = 'products'


class CreateProductView(auth_mixin.LoginRequiredMixin, views.CreateView):
    model = Product
    template_name = 'shop/product_create.html'
    fields = ('photo', 'description', 'type', 'price', 'name')

    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProductDetailsView(auth_mixin.LoginRequiredMixin, views.DetailView):
    model = Product
    template_name = 'shop/product_details.html'
    context_object_name = 'product'


class EditProductView(views.UpdateView):
    model = Product
    template_name = 'shop/photo_edit.html'
    fields = ('description', 'photo', 'name', 'type', 'price')

    def get_success_url(self):
        return reverse_lazy('product details', kwargs={'pk': self.object.id})


def delete_product(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = DeleteProductForm(instance=product)

    context = {
        'form': form,
        'product': product,
    }

    return render(request, 'shop/product_delete.html', context)


@login_required
def product_list(request):
    object_list = Product.objects.all()
    filtered_orders = Order.objects.filter(owner=request.user.profile, is_ordered=False)
    current_order_products = []
    if filtered_orders.exists():
        user_order = filtered_orders[0]
        user_order_items = user_order.items.all()
        current_order_products = [product.product for product in user_order_items]

    context = {
        'object_list': object_list,
        'current_order_products': current_order_products
    }

    return render(request, 'accounts/products_list.html', context)

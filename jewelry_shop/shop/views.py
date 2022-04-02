# from django.shortcuts import render
from django.contrib.auth import mixins as auth_mixin
from django.urls import reverse_lazy
from django.views import generic as views
from jewelry_shop.common.views_mixins import RedirectToDashboard
from jewelry_shop.shop.forms import CreateProductForm, DeleteProductForm  # , DeleteProductPhotoForm
# from jewelry_shop.shop.models import ProductPhoto
from jewelry_shop.shop.models import Product


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


class DeleteProductView(views.DeleteView):
    template_name = 'shop/product_delete.html'
    form_class = DeleteProductForm

from django.urls import path

from jewelry_shop.shop.views import HomeView, DashboardView, CreateProductView, DashboardNoProfileView, \
    ProductDetailsView, EditProductView, product_list, delete_product     #DeleteProductView

urlpatterns = (
    path('', HomeView.as_view(), name='index'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('dashboard-no-profile', DashboardNoProfileView.as_view(), name='dashboard without profile'),

    path('create-product', CreateProductView.as_view(), name='create product'),

    path('product/details/<int:pk>/', ProductDetailsView.as_view(), name='product details'),
    path('product/edit/<int:pk>/', EditProductView.as_view(), name='edit product'),
    # path('product/delete/<int:pk>/', DeleteProductView.as_view(), name='delete product'),
    path('product/delete/<int:pk>/', delete_product, name='delete product'),

    path('product-list', product_list, name='product list'),
)


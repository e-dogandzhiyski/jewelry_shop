from django.urls import path

from jewelry_shop.shop.views import HomeView, DashboardView, DashboardNoProfileView, \
    ProductDetailsView, EditProductView, product_list, delete_product, CreateProductView, ShowAllProfiles

urlpatterns = (
    path('', HomeView.as_view(), name='index'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    path('all-profiles/', ShowAllProfiles.as_view(), name='profiles'),

    path('dashboard-no-profile', DashboardNoProfileView.as_view(), name='dashboard with-out profile'),

    path('product-create/', CreateProductView.as_view(), name='create product'),
    path('product/edit/<int:pk>/', EditProductView.as_view(), name='edit product'),
    path('product/delete/<int:pk>/', delete_product, name='delete product'),
    path('product/details/<int:pk>/', ProductDetailsView.as_view(), name='product details'),

    path('product-list', product_list, name='product list'),
)

from django.urls import path

from jewelry_shop.shop.views import HomeView, DashboardView, CreateProductView, DashboardNoProfileView, \
    ProductDetailsView, EditProductView, DeleteProductView

urlpatterns = (
    path('', HomeView.as_view(), name='index'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('dashboard-no-profile', DashboardNoProfileView.as_view(), name='dashboard without profile'),

    path('create-product', CreateProductView.as_view(), name='create product'),

    path('photo/details/<int:pk>/', ProductDetailsView.as_view(), name='product details'),
    path('photo/edit/<int:pk>/', EditProductView.as_view(), name='edit product'),
    path('photo/delete/<int:pk>/', DeleteProductView.as_view(), name='delete product'),
)

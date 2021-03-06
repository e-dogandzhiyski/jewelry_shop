from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from jewelry_shop.accounts.views import UserRegisterView, UserLoginView, UserLogoutView, ProfileDetailsView, \
    ChangeUserPasswordView, AddShippingAddressView, \
    AddCardView, my_profile
from jewelry_shop.shopping_cart.views import process_payment

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register user'),
    path('login/', UserLoginView.as_view(), name='login user'),
    path('logout/', UserLogoutView.as_view(), name='logout user'),

    path('<int:pk>/', ProfileDetailsView.as_view(), name='profile details'),

    path('add-shipping-address/', AddShippingAddressView.as_view(), name='shipping address'),
    path('add-card-info/', AddCardView.as_view(), name='card info'),

    path('edit-password/', ChangeUserPasswordView.as_view(), name='change password'),
    path('password_change_done/', RedirectView.as_view(url=reverse_lazy('dashboard')), name='password change done'),

    path('payment/<order_id>', process_payment, name='process payment'),
    path('profile/', my_profile, name='my_profile'),
]

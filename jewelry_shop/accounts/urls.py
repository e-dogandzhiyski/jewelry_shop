from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from jewelry_shop.accounts.views import UserRegisterView, UserLoginView, UserLogoutView, ProfileDetailsView, \
    ChangeUserPasswordView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register user'),
    path('login/', UserLoginView.as_view(), name='login user'),
    path('logout/', UserLogoutView.as_view(), name='logout user'),

    path('<int:pk>/', ProfileDetailsView.as_view(), name='profile details'),
    path('edit-password/', ChangeUserPasswordView.as_view(), name='change password'),
    path('password_change_done/', RedirectView.as_view(url=reverse_lazy('dashboard')), name='password_change_done'),
]

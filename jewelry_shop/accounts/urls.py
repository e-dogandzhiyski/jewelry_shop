from django.urls import path

from jewelry_shop.accounts.views import UserRegisterView, UserLoginView, UserLogoutView, ProfileDetailsView

urlpatterns = (
    path('register/', UserRegisterView.as_view(), name='register user'),
    path('login/', UserLoginView.as_view(), name='login user'),
    path('logout/', UserLogoutView.as_view(), name='logout user'),

    path('<int:pk>/', ProfileDetailsView.as_view(), name='profile details'),
)

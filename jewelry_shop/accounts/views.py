from django.contrib.auth import login
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views

from jewelry_shop.accounts.forms import CreateProfileForm, ShippingAddressForm, CardInfoForm
from jewelry_shop.accounts.models import Profile, ShippingAddress
from jewelry_shop.shopping_cart.models import Order


def my_profile(request):
    my_user_profile = Profile.objects.filter(user=request.user).first()
    my_orders = Order.objects.filter(is_ordered=True, owner=my_user_profile)
    context = {
        'my_orders': my_orders
    }

    return render(request, 'accounts/profile.html', context)


class UserRegisterView(views.CreateView):
    form_class = CreateProfileForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login_page.html'

    def get_success_url(self):
        next = self.request.GET.get('next', None)
        if next:
            return next
        return reverse_lazy('index')


class UserLogoutView(auth_views.LogoutView):
    pass


class ProfileDetailsView(views.DetailView):
    model = Profile
    template_name = 'accounts/profile_details.html'
    context_object_name = 'profile'


class ChangeUserPasswordView(auth_views.PasswordChangeView):
    template_name = 'accounts/change_password.html'


class ProfileOrdersView(views.DetailView):
    model = Profile
    template_name = 'accounts/my_orders.html'
    context = 'products'
    # context = 'orders'


class AddShippingAddressView(views.CreateView):
    template_name = 'accounts/shipping_address.html'
    form_class = ShippingAddressForm
    success_url = reverse_lazy('checkout')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    #
    # def get_success_url(self):
    #     return reverse_lazy('process payment', kwargs={'pk': self.object.id})


class AddCardView(views.CreateView):
    template_name = 'accounts/card_info.html'
    form_class = CardInfoForm
    success_url = reverse_lazy('shipping address')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

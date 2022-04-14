from django.contrib.auth.views import redirect_to_login
from django.shortcuts import redirect
from django.contrib.auth.mixins import PermissionRequiredMixin


class RedirectToDashboard:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')

        return super().dispatch(request, *args, **kwargs)


class UserAccessMixin(PermissionRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect_to_login(self.request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())
        if not self.has_permission():
            return redirect('page not found')
        return super(UserAccessMixin, self).dispatch(request, *args, **kwargs)

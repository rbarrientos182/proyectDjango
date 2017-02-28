from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_require
from django.shortcuts import redirect

class AuthRedirectMixin(object):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('/')
        else:
            return super(AuthRedirectMixin, self).get(self, request, *args, **kwargs)

class LoginRequiredMixini(object):
    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiedMixin, self).dispatch(request, *args, **kwargs)

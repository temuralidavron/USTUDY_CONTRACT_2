from django.http import HttpResponseForbidden
from functools import wraps

def admin_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden("Siz ro'yxatdan o'tmagansiz.")
        if not getattr(request.user, 'is_admin', False):
            return HttpResponseForbidden("Sizda bu sahifaga kirish ruxsati yo'q.")
        return view_func(request, *args, **kwargs)
    return _wrapped_view

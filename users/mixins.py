from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy


class ProfileRequiredMixin:
    url = reverse_lazy('create_profile')

    def dispatch(self, request, *args, **kwargs):
        if request.user.has_profile():
            return super().dispatch(request, *args, **kwargs)
        return redirect(self.url)


class NoProfileRequiredMixin:
    url = reverse_lazy('my_profile')

    def dispatch(self, request, *args, **kwargs):
        if request.user.has_profile():
            return redirect(self.url)
        return super().dispatch(request, *args, **kwargs)


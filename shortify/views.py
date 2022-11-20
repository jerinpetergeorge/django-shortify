from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views import generic

from .forms import ShortifyCreateForm
from .models import ShortifyURL


class ShortifyCreateView(LoginRequiredMixin, generic.CreateView):
    model = ShortifyURL
    template_name = "shortify/create.html"
    form_class = ShortifyCreateForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ShortifyDetailView(LoginRequiredMixin, generic.DetailView):
    model = ShortifyURL
    template_name = "shortify/detail.html"


class ShortifyRedirectView(generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        shortify_object = get_object_or_404(ShortifyURL, slug=kwargs["slug"])
        shortify_object.hits += 1
        shortify_object.save(update_fields=["hits"])
        return shortify_object.url

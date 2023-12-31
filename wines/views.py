from django.views.generic import (
    TemplateView, CreateView,
    ListView, DetailView,
    DeleteView, UpdateView)
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from .models import Wine
from .forms import WineForm


"""View home screen"""


class index(TemplateView):
    template_name = "wines/index.html"


"""View about list"""


class about(ListView):
    template_name = "wines/about.html"
    model = Wine
    context_object_name = "wines"

    def get_queryset(self):
        return self.model.objects.all()[:3]


"""View all wines"""


class Wines(ListView):
    template_name = "wines/wines.html"
    model = Wine
    context_object_name = "wines"
    form_class = WineForm
    success_url = "/wines/"

    def get_queryset(self, **kwargs):
        query = self.request.GET.get('q')
        if query:
            wines = self.model.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query)
            )
        else:
            wines = self.model.objects.all()
        return wines


"""Add a wine view"""


class WineDetail(DetailView):
    template_name = "wines/wine_detail.html"
    model = Wine
    context_object_name = "wine"


"""Add wine review"""


class AddWine(LoginRequiredMixin, CreateView):
    template_name = "wines/add_wine.html"
    model = Wine
    context_object_name = "wines"
    form_class = WineForm
    success_url = "/wines/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddWine, self).form_valid(form)


"""Delete wine review"""


class DeleteWine(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Wine
    success_url = '/wines/'

    def test_func(self):
        return self.request.user == self.get_object().user


"""Edit wine review"""


class EditWine(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "wines/edit_wine.html"
    model = Wine
    form_class = WineForm
    success_url = '/wines/'

    def test_func(self):
        return self.request.user == self.get_object().user

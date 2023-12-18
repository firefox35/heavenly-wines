from django.views.generic import (
    TemplateView, CreateView,
    ListView, DetailView,
    DeleteView, UpdateView)
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from .models import Wine
from .forms import WineForm


class index(TemplateView):
    template_name = "wines/index.html"


class about(ListView):
    template_name = "wines/about.html"
    model = Wine
    context_object_name = "wines"

    def get_queryset(self):
        return self.model.objects.all()[:3]


class Wines(ListView):
    """View all wines"""
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


class WineDetail(DetailView):
    """Add a wine view"""
    template_name = "wines/wine_detail.html"
    model = Wine
    context_object_name = "wine"


class AddWine(LoginRequiredMixin, CreateView):
    """Add wine review"""
    template_name = "wines/add_wine.html"
    model = Wine
    context_object_name = "wines"
    form_class = WineForm
    success_url = "/wines/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddWine, self).form_valid(form)


class DeleteWine(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete wine review"""
    model = Wine
    success_url = '/wines/'

    def test_func(self):
        return self.request.user == self.get_object().user


class EditWine(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit wine review"""
    template_name = "wines/edit_wine.html"
    model = Wine
    form_class = WineForm
    success_url = '/wines/'

    def test_func(self):
        return self.request.user == self.get_object().user

from django.views.generic import TemplateView, CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Wine
from .forms import WineForm


class index(TemplateView):
    template_name = 'wines/index.html'


class AddWine(LoginRequiredMixin, CreateView):
    """ Add wine view """
    template_name = 'wines/add_wine.html'
    model = Wine
    form_class = WineForm
    success_url = '/wines/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddWine, self).form_valid(form)

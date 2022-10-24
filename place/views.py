from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, TemplateView

from .models import Place


# Create your views here.
# url -> view -> html
class HomePage(TemplateView):
    template_name = "homepage.html"

class HomePlaces(ListView):
    template_name = "homeplaces.html"
    model = Place

class DetailsPlace(DetailView):
    template_name = "detailsplace.html"
    model = Place

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

    # def get(self, request, *args, **kwargs):
    #     place = self.get_object()
    #     average_rating = 
        
        
    #     return super().get(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super(DetailsPlace,self).get_context_data(**kwargs)
        related_places = Place.objects.filter(category=self.get_object().category)
        context["related_places"] = related_places 
        return context


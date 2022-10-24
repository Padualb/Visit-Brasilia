from django.shortcuts import render

from .models import Place


# Create your views here.
# url -> view -> html
def homepage(request):
    return render(request, "homepage.html")

def homeplaces(request):
    context = {}
    places_list = Place.objects.all()
    context['places_list'] = places_list
    return render(request, "homeplaces.html", context)

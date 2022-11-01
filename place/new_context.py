from xml.etree.ElementTree import Comment

from .models import Place


def list_recent_places(request):
    list_places = Place.objects.all().order_by('creation_date')
    return{"list_recent_places": list_places}


def list_categorys(request):
    list_categorys = ("Restaurants", "Attractions", "Parties", "Other")
    return{"list_categorys": list_categorys}

def list_attractions(request):
    list_attractions = Place.objects.filter(category="ATTRACTIONS")
    return{"list_attractions": list_attractions}

def list_parties(request):
    list_parties = Place.objects.filter(category="PARTIES")
    return{"list_parties": list_parties}

def list_restaurants(request):
    list_restaurants= Place.objects.filter(category="RESTAURANTS")
    return{"list_restaurants": list_restaurants}

def list_others(request):
    list_others = Place.objects.filter(category="OTHER")
    return{"list_others": list_others}       

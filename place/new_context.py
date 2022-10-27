from xml.etree.ElementTree import Comment

from .models import Place


def list_recent_places(request):
    list_places = Place.objects.all().order_by('creation_date')
    return{"list_recent_places": list_places}


def list_categorys(request):
    list_categorys = ("Restaurants", "Attractions", "Parties", "Other")
    return{"list_categorys": list_categorys}


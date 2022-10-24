# url -> view -> template

from django.urls import include, path

from place.models import Place

from .views import DetailsPlace, HomePage, HomePlaces

app_name = 'place'

urlpatterns = [
    path('', HomePage.as_view(), name='homepage'),
    path('places/', HomePlaces.as_view(), name='homeplaces'),
    path('places/<int:pk>', DetailsPlace.as_view(), name='detailsplace')
] 

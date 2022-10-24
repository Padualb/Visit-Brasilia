# url -> view -> template

from django.urls import include, path

from .views import homepage, homeplaces

urlpatterns = [
    path('', homepage),
    path('places/', homeplaces),

] 

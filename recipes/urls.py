from django.urls import path
from recipes.views import my_response, home


urlpatterns = [
    path('', home),
    path('hello/', my_response),
]
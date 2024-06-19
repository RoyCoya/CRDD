
from django.urls import path
from .views import *

app_name = 'Ontology'

urlpatterns = [
    path('search_by_name/', search_by_name, name='search_by_name'),
]
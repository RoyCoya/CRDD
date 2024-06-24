
from django.urls import path
from .views import *

app_name = 'Ontology'

urlpatterns = [
    path('concept/search/', search_concept, name='search_concept'),
    path('concept/<str:element_id>/', retrieve_concept, name='retrieve_concept'),

]
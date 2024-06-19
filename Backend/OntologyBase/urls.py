
from django.urls import path
from .views import *

app_name = 'Ontology'

urlpatterns = [
    path('search/ontology/', get_concept_id_by_representation, name='search_ontology'),
    path('search/concept/', get_presentations_by_concept, name='search_concept'),
]
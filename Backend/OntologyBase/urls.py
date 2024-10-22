
from django.urls import path
from .views import Concept, DefinitionSet

app_name = 'Ontology'

url_concept = [
    path('concepts/', Concept.Concepts.as_view(), name='concepts'),
    path('concepts/<str:concept_element_id>/', Concept.Concept.as_view(), name='concept'),

    path('concepts/<str:concept_element_id>/representations/', Concept.Representations.as_view(), name='concept_representations'),
    path('concepts/<str:concept_element_id>/representations/<str:representation_element_id>/', Concept.Representation.as_view(), name='concept_representation'),

    path('concepts/<str:concept_element_id>/relations/', Concept.Relations.as_view(), name='concept_relations'),
    path('concepts/<str:concept_element_id>/relations/<str:relation_element_id>/', Concept.Relation.as_view(), name='concept_relation'),

    path('concepts/<str:concept_element_id>/prefer_terms/', Concept.PreferTerms.as_view(), name='concept_prefer_terms'),
    path('concepts/<str:element_id>/synonyms/', Concept.Synonyms.as_view(), name='concept_synonyms'),
]

url_definition_set = [
    path('definition_sets/', DefinitionSet.DefinitionSets.as_view(), name='definition_sets'),
    path('definition_sets/<str:element_id>/', DefinitionSet.DefinitionSet.as_view(), name='definition_set'),
]

urlpatterns = url_concept + url_definition_set + []
from django.http import JsonResponse, HttpRequest
from OntologyBase.response import *
from MainFrame.response import *
from django.core.paginator import Paginator
from rest_framework.views import APIView
import OntologyBase.ontology.Concept as concept
import OntologyBase.ontology.DefinitionSet as definition_set

# TODO: all


class DefinitionSets(APIView):
    def get(self, request):
        return TODO


class DefinitionSet(APIView):
    def get(self, request, element_id):
        try:
            data = definition_set.retrive(element_id)
            if not data: return NOT_FOUND
            return success(data=data)
        except Exception as e:
            return server_error(str(e))

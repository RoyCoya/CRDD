from django.http import JsonResponse, HttpRequest
import OntologyBase.response as response
from django.core.paginator import Paginator
from rest_framework.views import APIView
import OntologyBase.ontology.Concept as concept
import OntologyBase.ontology.DefinitionSet as definition_set

# TODO: all


class DefinitionSets(APIView):
    def get(self, request):
        return response.TODO


class DefinitionSet(APIView):
    def get(self, request, element_id):
        try:
            data = definition_set.retrive(element_id)
            if not data: return response.NOT_FOUND
            return response.success(data=data)
        except Exception as e:
            return response.server_error(str(e))

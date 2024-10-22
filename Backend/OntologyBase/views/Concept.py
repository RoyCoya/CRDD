from django.http import JsonResponse, HttpRequest
import OntologyBase.response as response
from django.core.paginator import Paginator
from rest_framework.views import APIView
import OntologyBase.ontology.Concept as concept

# TODO: api description, see obsidian CRDD/API

class Concepts(APIView):
    def get(self, request):
        try:
            # TODO: search all when no query parameter gived
            definition_set, coding_set, code, representation = [
                request.GET.get(param)
                for param in ["definition_set", "coding_set", "code", "representation"]
            ]
            if definition_set and coding_set and code:
                return response.success(
                    concept.search_by_code(definition_set, coding_set, code)
                )
            if representation:
                return response.success(
                    concept.search_by_representation(representation, request.GET.get("limit"))
                )
            return response.CONCEPT_SEARCHING_REQUIREMENTS
        except Exception as e:
            return response.server_error(str(e))


class Concept(APIView):
    def get(self, request, concept_element_id):
        """retrieve an concept's basic infos and its related infos

        Args:
        - `element_id`: concept's element id

        Return:
        - `concept_eid` str: concept's element id (given by user)
        - `representations` list[dict]: all representations to represent the concept
            - `element_id` str
            - `value` str
        - `codes` list[dict]: coding set that encoded the concept
            - `element_id` str: code's element id
            - `value` str: code
            - `definition_set` dict
                - `element_id` str: definition's element id
                - `value` str: definition set's name
            - `coding_set` list[dict]
                - `element_id` str: conding set's element id
                - `value` str: coding set's name
        - TODO:`related_infos` list[dict]
            - `relationship` dict
                - `element_id` str: relationship's element id in semantic net
                - `value` str: relationship's name
                - `object` dict
                    - `element_id` str: concept's element id
                    - `value` str: concept's name
        """
        try:
            data = concept.retrive(concept_element_id)
            if data and len(data) == 1:
                return response.success(data)
            else:
                return response.NOT_FOUND
        except Exception as e:
            return response.server_error(str(e))


# TODO: 仅获取首选语言、首选definition set的term
class Representations(APIView):
    def get(self, request, concept_element_id):
        try:
            data = concept.get_representations(
                concept_element_id,
                request.GET.get("language"),
                request.GET.get("limit"),
            )
            if not data:
                return response.NOT_FOUND
            return response.success(data)
        except Exception as e:
            return response.server_error(str(e))


# TODO: 留用
class Representation(APIView):
    def get(self, request, concept_element_id, representation_element_id):
        return response.TODO


# TODO: 根据类型搜索
class Relations(APIView):
    def get(self, request, concept_element_id):
        data = concept.get_relations(concept_element_id, request.GET.get("limit"), request.GET.get("query_type"))
        return response.success(data)


# TODO: 留用
class Relation(APIView):
    def get(self, request, concept_element_id, relation_element_id):
        return response.TODO


class PreferTerms(APIView):
    def get(self, request, concept_element_id):
        try:
            prefer_definition_set, prefer_language, limit = [
                request.GET.get(param)
                for param in ["definition_set", "language", "limit"]
            ]
            data = concept.get_prefer_terms(
                concept_element_id, prefer_definition_set, prefer_language, limit
            )
            if not data:
                return response.NOT_FOUND
            return response.success(data)
        except Exception as e:
            return response.server_error(str(e))


class Synonyms(APIView):
    def get(self, request, element_id):
        try:
            prefer_definition_set, prefer_language, limit = [
                request.GET.get(param)
                for param in ["definition_set", "language", "limit"]
            ]
            data = concept.get_synonyms(
                element_id, prefer_definition_set, prefer_language, limit
            )
            if not data:
                return response.NOT_FOUND
            return response.success(data)
        except Exception as e:
            return response.server_error(str(e))

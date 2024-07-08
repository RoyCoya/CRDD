from django.http import JsonResponse, HttpRequest
from .neo import *
import OntologyBase.response as response
from django.core.paginator import Paginator


def search_concept(request: HttpRequest):
    """search by concept's defined code or its representations
    
    Args:
    1. When search by code, three parameters are needed: `definition_set`, `coding_set`, `code`.
    2. When parameters above are not complete or not given, search by given parameter `representation`.
    3. If the condition is not included above, return InputError
    4. Else return InternalError

    Return:
    - `message` str: respose message
    - `data` list
        - `concept` dict
            - `element_id` str
        - `representations` list[dict]: all representations to represent the concept
            - `element_id` str
            - `value` str
    ```
    """
    try:
        if not request.GET: return response.client_error(response.CONCEPT_SEARCHING_REQUIREMENTS)
        definition_set, coding_set, code, representation = [request.GET.get(param) for param in ["definition_set", "coding_set", "code", "representation"] ]
        if definition_set and coding_set and code: return  response.success(get_concept_by_code(definition_set, coding_set, code))
        if representation: return response.success(get_concept_by_representation(representation, 10))
        return response.client_error(response.CONCEPT_SEARCHING_REQUIREMENTS)
    except Exception as e: return response.server_error(str(e))

def retrieve_concept(request: HttpRequest, element_id):
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
        if not request.method == "GET": return response.client_error("Invalid Request Method", 405)
        data = get_concept(element_id)
        print(data)
        if data: return response.success(data)
        else: return response.client_error(title="Not Found", msg=element_id, status=404)
    except Exception as e: return response.server_error(str(e))

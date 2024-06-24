from django.http import JsonResponse, HttpRequest
from .neo import *
from .response import *
from django.core.paginator import Paginator


def search_concept(request: HttpRequest):
    """search by concept's defined code or its representations
    
    Args:
    1. When search by code, three parameters are needed: `definition_set`, `coding_set`, `code`.
    2. When parameters above are not complete or not given, search by given parameter `representation`.
    3. If the condition is not included above, return InputError
    4. Else return InternalError

    Return:
    - `message` str: `successed` or error information
    - `data` list
        - `concept` dict
            - `element_id` str: concept's element id
        - `representations` list[dict]
            - `element_id` str: representation's element id
            - `value` str: representation in text
    ```
    """
    try:
        if not request.GET: return ERROR_INPUT
        definition_set, coding_set, code, representation = [request.GET.get(param) for param in ["definition_set", "coding_set", "code", "representation"] ]
        if definition_set and coding_set and code: return JsonResponse({"message": "successed", "data": get_concept_by_code(definition_set, coding_set, code)})
        if representation: return JsonResponse({"message": "successed","data": get_concept_by_representation(representation, 100),})
        return ERROR_INPUT
    except Exception as e: return JsonResponse({"message": "Internal Error: " + str(e)}, status=500)


def retrieve_concept(request: HttpRequest, element_id):
    """retrieve an concept's basic infos and its related infos
    
    Args:
    - `element_id`: concept's element id
    
    Return:
    - `concept_eid`: concept's element id (given by user)
    - `representations`: all representations to represent the concept
    - `coding_set`: coding set that encoded the concept
    """
    return 0
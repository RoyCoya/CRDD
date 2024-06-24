from django.http import JsonResponse

ERROR_INPUT = JsonResponse(
    {
        "message": """
        Input error: no search parameter has been given or parameter combination are invalid.
        Support combination:
        1. element id
        2. coding set and code
        3. representation
        """
    },
    status=400,
)
UNKOWN_ERROR = JsonResponse(
    {"message": "Unkown error: if you see this, please contact with admin"}, status=500
)

SUCCESS = JsonResponse({"message": "successed"})

from django.http import JsonResponse

CONCEPT_SEARCHING_REQUIREMENTS = """
        Input error: no search parameter has been given or parameter combination are invalid.
        Support combination:
        1. element id
        2. coding set and code
        3. representation
        """

UNKOWN_ERROR = "Unkown error: if you see this, please contact with admin"

SUCCESS = "successed"

def client_error(msg, title="Bad Request", status=400):
    return JsonResponse({"message": title + ": " + msg}, status=status)

def server_error(msg, title="Internal Error", status=500):
    return JsonResponse({"message": title + ": " + msg}, status=status)

def success(data=None):
    return JsonResponse({"message": "successed", "data": data})
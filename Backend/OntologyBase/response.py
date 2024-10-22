from django.http import JsonResponse

def client_error(msg, title="Bad Request", status=400):
    return JsonResponse({"message": title + ": " + msg}, status=status)

def server_error(msg, title="Internal Error", status=500):
    return JsonResponse({"message": title + ": " + msg}, status=status)

def success(data=None):
    return JsonResponse({"message": "Successed", "data": data})

CONCEPT_SEARCHING_REQUIREMENTS = server_error("""
        Input error: no search parameter has been given or parameter combination are invalid.
        Support combination:
        1. element id
        2. coding set and code
        3. representation
        """)
UNKOWN_ERROR = server_error("Unkown error: if you see this, please contact with admin")
NOT_FOUND = server_error("Resource not found", status=404)
TODO = server_error("This is an uncompleted function, please request later", status=501)

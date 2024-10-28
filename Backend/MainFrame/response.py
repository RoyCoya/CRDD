from django.http import JsonResponse

def client_error(msg, title="Bad Request", status=400):
    return JsonResponse({"message": title + ": " + msg}, status=status)

def server_error(msg, title="Internal Error", status=500):
    return JsonResponse({"message": title + ": " + msg}, status=status)

def success(data=None):
    return JsonResponse({"message": "成功\t Successed", "data": data})


UNKOWN_ERROR = server_error("未知错误，请联系管理人员或开发人员\t Unkown error: if you see this, please contact with admin")
NOT_AUTHORIZED = client_error("无访问权限\t No permission", status=401)
NOT_FOUND = server_error("未找到该资源\t Resource not found", status=404)
TODO = server_error("未完成的功能，敬请期待\t This is an uncompleted function, please request later", status=501)

from django.http import JsonResponse
from .utils import check_connection, driver, cjk_regex
from django.core.paginator import Paginator

@check_connection
def search_by_name(request):
    onto_name = request.GET.get("onto_name")
    is_cjk = bool(cjk_regex.search(onto_name))
    query = f"""
        call db.index.fulltext.queryNodes("{"representation_cjk" if is_cjk else "representation_eng"}", $onto_name) yield node
        match (node)-[:Represent]->(concept:Concept)
        WITH concept
        LIMIT 50
        match (represent)-[:Represent]->(concept:Concept)
        return concept, collect(represent) as represents
    """
    # TODO: check failed
    if not onto_name: return JsonResponse({
        "message":"Input error: no search parameter has been given"
    }, status=400)

    try:
        result = driver.execute_query(query, parameters_={"onto_name": onto_name})
        print(result)
        # TODO: data type issue
        return JsonResponse({
            "message":"successed",
            # "data":list[result],
        })
    except Exception as e:
        return JsonResponse({
            "message":f"Database Error : {str(e)}"
            }, status=500)

# def post(self, request, *args, **kwargs):
#     # 处理POST请求，例如创建新节点
#     query = "CREATE (n:Person {name: $name}) RETURN n"
#     try:
#         result = neo4j_conn.query(query, parameters={"name": request.data.get("name")})
#         data = [record["n"] for record in result]
#         return Response(data, status=status.HTTP_201_CREATED)
#     except Exception as e:
#         return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

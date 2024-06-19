from django.http import JsonResponse
from .utils import check_connection, driver, cjk_regex
from django.core.paginator import Paginator

# TODO: one API do only one thing and make one query, don't decouple it, to decrease database cost
@check_connection
def get_concept_id_by_representation(request):
    name = request.GET.get("name")
    if not name: return JsonResponse({
        "message":"Input error: no search parameter has been given"
    }, status=400)
    is_cjk = bool(cjk_regex.search(name))
    query = f"""
        call db.index.fulltext.queryNodes("{"representation_cjk" if is_cjk else "representation_eng"}", $name) yield node
        match (node)-[:Represent]->(concept:Concept)
        WITH concept
        LIMIT 50
        return id(concept)
    """
    
    try:
        result = driver.execute_query(query, parameters_={"name": name})
        data = [r.data()['id(concept)'] for r in result.records]
        # TODO: why always unknow?
        time = str(result.summary.result_available_after) + "ms" if result.summary.result_available_after else "Unkown"
        driver.close()
        return JsonResponse({
            "message":"successed",
            "summary":"Concept ID list",
            "time_consumption":time,
            "data":data,
        })
    except Exception as e:
        driver.close()
        return JsonResponse({
            "message":f"Database Error : {str(e)}"
            }, status=500)

@check_connection
def get_presentations_by_concept(request):
    return 0
from neo4j import GraphDatabase, Record
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from functools import wraps
from .utils import isCJK
import atexit

driver = GraphDatabase.driver(
    f"bolt://{settings.NEO4J['ip']}:{settings.NEO4J['bolt_port']}",
    auth=(settings.NEO4J['user'], settings.NEO4J['password']), 
    database='ontology'
)
atexit.register(driver.close)


def check_connection(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try: driver.verify_connectivity()
        except Exception as e:return Response({"Database Error": e}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return func(*args, **kwargs)
    return wrapper

def run_query(query, params=None)-> list[Record]:
    try:
        result = driver.execute_query(query_=query, parameters_=params)
        data = [r.data() for r in result.records]
        return data
    except: raise

@check_connection
def get_concept_by_code(definition_set, coding_set, code):
    try: return run_query("""
        match (:DefinitionSet {value:$definition_set})-[:Provide]->(:CodingSet {value:$coding_set})-[:Provide]->(code:Code {value:$code})-[:Encode]->(concept:Concept)
        with concept
        match (representation)-[represent:Represent]->(concept)
        set representation.element_id = elementid(representation)
        set concept.element_id = elementid(concept)
        return concept{.element_id} as concept, collect(representation{.value, .element_id}) as representations
    """, params={
        "definition_set": definition_set,
        "coding_set": coding_set,
        "code": code
    })
    except: raise


@check_connection
def get_concept_by_representation(representation, limit):
    try:
        index = "representation_cjk" if isCJK(representation) else "representation_eng"
        return run_query("""
        call db.index.fulltext.queryNodes($index,$representation) yield node, score
        match (node)-[:Represent]->(concept)
        with concept limit $limit
        match (representation)-[:Represent]->(concept)
        set representation.element_id = elementid(representation)
        set concept.element_id = elementid(concept)
        return concept{.element_id} as concept, collect(representation{.value, .element_id}) as representations
        """, params={
            "index": index,
            "representation": representation,
            "limit": limit,
        })
    except: raise

@check_connection
def get_concept(element_id):
    try:
        return run_query("""
        match (representation)-[:Represent]->(c:Concept)
        where elementid(c) = $element_id
        set representation.element_id = elementid(representation)
        with representation, c
        match (definition_set:DefinitionSet)-[:Provide]->(coding_set:CodingSet)-[:Provide]->(code:Code)-[:Encode]->(c)
        set definition_set.element_id = elementid(definition_set)
        set coding_set.element_id = elementid(coding_set)
        set code.element_id = elementid(code)
        return $element_id as concept_eid,
                collect(distinct code{
                   .value, 
                   .element_id, 
                   definition_set: definition_set{.element_id, .value}, 
                   coding_set: coding_set{.element_id, .value}
                }) AS codes，
                collect(distinct representation{.value, .element_id}) as representations,
        """, params={
            "element_id": element_id
        })
    except: raise
# check_connection
# def get

# @check_connection
# def get_concept_id_by_representation(request):
#     name = request.GET.get("name")
#     is_cjk = bool(cjk_regex.search(name))
#     query = f"""
#         call db.index.fulltext.queryNodes("{"representation_cjk" if is_cjk else "representation_eng"}", $name) yield node
#         match (node)-[:Represent]->(concept:Concept)
#         WITH concept
#         LIMIT 50
#         return id(concept)
#     """
    
#     try:
#         result = driver.execute_query(query, parameters_={"name": name})
#         data = [r.data()['id(concept)'] for r in result.records]
#         # TODO: why always unknow?
#         time = str(result.summary.result_available_after) + "ms" if result.summary.result_available_after else "Unkown"
#         driver.close()
#         return JsonResponse({
#             "message":"successed",
#             "summary":"Concept ID list",
#             "time_consumption":time,
#             "data":data,
#         })
#     except Exception as e:
#         driver.close()
#         return JsonResponse({
#             "message":f"Database Error : {str(e)}"
#             }, status=500)

# @check_connection
# def get_presentations_by_concept(request):
#     return 0
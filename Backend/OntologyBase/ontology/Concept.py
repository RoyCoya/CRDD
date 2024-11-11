from .Neo import check_connection, run_query
from OntologyBase.utils import getTextIndex
import OntologyBase.ontology.DefinitionSet as DefinitionSet
import time

DEFAULT_LIMIT = 50

# @check_connection
# def retrive(element_id):
#     try:
#         return run_query(
#             """
#         match (representation)-[:Represent]->(concept:Concept)
#         where elementid(concept) = $element_id
#         match (definition_set:DefinitionSet)-[:Provide]->(coding_set:CodingSet)-[:Provide]->(code:Code)-[:Encode]->(concept)
#         optional match (definition_set:DefinitionSet)-[:PreferTerm]->(representation)
#         optional match (prefer_term_definition_set:DefinitionSet)-[:PreferTerm]->(representation)
#         optional match (concept)-[:IsA]->(up:Concept)
#         optional match (concept)<-[:IsA]-(down:Concept)
#         with collect(distinct prefer_term_definition_set{.value, element_id:elementid(prefer_term_definition_set)}) as prefer_term_definition_set, concept, code, representation, up, down, definition_set, coding_set
#         return concept{element_id:elementid(concept)}, collect(distinct code{element_id:elementid(code),definition_set:definition_set.value,coding_set:coding_set.value, .value}) as codes, collect(distinct representation{element_id:elementid(representation), .value, languages:labels(representation), prefer_term:prefer_term_definition_set}) as representations, collect(distinct up{element_id:elementid(up)}) as up, collect(distinct down{element_id:elementid(down)}) as down
#         """,
#             params={"element_id": element_id},
#         )
#     except:
#         raise


@check_connection
def retrive(element_id):
    try:
        return run_query(
            """
        match (concept:Concept)
        where elementid(concept) = $element_id
        return elementid(concept) as element_id
        """,
            params={"element_id": element_id},
        )
    except:
        raise


def create():
    try:
        return run_query(
            """

        """
        )
    except:
        raise

@check_connection
def search_by_code(definition_set, coding_set, code):
    # try: return run_query("""
    #     match (:DefinitionSet {value:$definition_set})-[:Provide]->(:CodingSet {value:$coding_set})-[:Provide]->(code:Code {value:$code})-[:Encode]->(concept:Concept)
    #     with concept
    #     match (representation)-[represent:Represent]->(concept)
    #     return concept{element_id:elementid(concept)} as concept, collect(representation{.value, element_id:elementid(representation)}) as representations
    # """, params={
    #     "definition_set": definition_set,
    #     "coding_set": coding_set,
    #     "code": code
    # })
    # except: raise
    return "暂时用不上，还没做"


# TODO: 两种索引应该是优先查某一个，而不是只查某一个
@check_connection
def search_by_representation(representation, limit):
    try:
        print(time.time())
        exact_result = run_query(
            """
        MATCH(node:Representation)-[:Represent]->(concept:Concept)
        WHERE node.value = $representation
        RETURN elementid(concept) as element_id
        """,
            params={"representation": representation},
        )
        exact_ids = [row["element_id"] for row in exact_result]
        fuzzy_results = run_query(
            query="""
        CALL db.index.fulltext.queryNodes($index, $representation) YIELD node, score
        MATCH (node:Representation)-[:Represent]->(concept:Concept)
        WHERE NOT elementid(concept) IN $exact_ids
        WITH concept, max(score) as maxScore
        ORDER BY maxScore DESC
        RETURN elementid(concept) as element_id
        LIMIT $limit
        """,
            params={
                "index": getTextIndex(representation),
                "representation": representation,
                "exact_ids": exact_ids,
                "limit": int(limit) if limit else DEFAULT_LIMIT,
            },
        )
        return exact_result + fuzzy_results
    except:
        raise


@check_connection
def get_representations(element_id, language, limit):
    try:
        query = f"""
        match (concept:Concept)
        where elementid(concept) = $element_id
        match (representation:Representation{":" + language if language else ""})-[:Represent]->(concept)
        return distinct elementid(representation) as element_id, representation.value as value
        limit $limit
        """
        params = {
            "element_id": element_id,
            "limit": int(limit) if limit else DEFAULT_LIMIT,
        }
        return run_query(query, params)
    except:
        raise


@check_connection
def get_relations(element_id, limit, query_type=None):
    try:
        query = {
            "any": """
            MATCH (a:Concept)-[r]-(b:Concept)
            WHERE elementid(a) = $element_id
            RETURN elementid(r) as element_id, elementid(startNode(r)) AS start, type(r) AS relation, elementid(endNode(r)) AS end
            LIMIT $limit
            """,
            "tree": """""",
            "graph": """""",
            "test": "return $element_id as element_id",
        }

        if not query_type or query_type not in query:
            query_type = "any"
        query_string = query[query_type]
        params = {
            "element_id": element_id,
            "limit": int(limit) if limit else DEFAULT_LIMIT,
        }

        return run_query(
            query_string,
            params=params,
        )
    except:
        raise


@check_connection
def get_prefer_terms(element_id, definition_set, language, limit):
    try:
        if definition_set:
            definition_set = DefinitionSet.retrive(definition_set)
            definition_set = definition_set[0]["value"]
        definition_set_p = ""
        if definition_set:
            definition_set_p = "and p.DefinitionSet = '" + definition_set + "'"

        query = f"""
        match (concept:Concept)-[p:PreferTerm]->(representation:Representation{":" + language if language else ""})
        where elementid(concept) = $element_id {definition_set_p}
        with distinct representation, p
        optional match (definition_set:DefinitionSet {{value:p.DefinitionSet}})
        return elementid(representation) as element_id, 
            representation.value as value,
            collect(elementid(definition_set)) as definition_sets,
            labels (representation) as languages
        limit $limit
        """
        params = {
            "element_id": element_id,
            "limit": int(limit) if limit else DEFAULT_LIMIT,
        }
        data = run_query(query, params)
        return data
    except:
        raise


@check_connection
def get_synonyms(element_id, definition_set, language, limit):
    try:
        if definition_set:
            definition_set = DefinitionSet.retrive(definition_set)
            definition_set = definition_set[0]["value"]

        query = f"""
        match (representation:Representation{":" + language if language else ""})-[:Represent]->(concept:Concept)
        where elementid(concept) = $element_id and not (concept)-[:PreferTerm]->(representation)
        with distinct representation
        optional match (definition_set:DefinitionSet {f"{{value:'{definition_set}'}}" if definition_set else ""})-[:Provide]->(:CodingSet)-[:Provide]->(:Code)-[:Encode]->(representation)
        return elementid(representation) as element_id, 
            representation.value as value,
            collect(elementid(definition_set)) as definition_sets,
            labels (representation) as languages
        limit $limit
        """
        params = {
            "element_id": element_id,
            "limit": int(limit) if limit else DEFAULT_LIMIT,
        }
        data = run_query(query, params)
        return data
    except:
        raise

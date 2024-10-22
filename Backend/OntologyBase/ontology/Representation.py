from .Neo import check_connection, run_query

@check_connection
def retrive(element_id):
    try:
        return run_query(
            """
        match (representation:Representation)
        where elementid(representation) = $representation
        with representation limit 1
        return elementid(representation) as element_id
        """,
            params={"element_id": element_id},
        )
    except:
        raise
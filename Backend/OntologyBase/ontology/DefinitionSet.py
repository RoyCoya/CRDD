from .Neo import check_connection, run_query

@check_connection
def retrive(element_id):
    try:
        return run_query(
        """
        match (d:DefinitionSet)
        where elementid(d) = $element_id
        return elementid(d) as element_id, d.value as value, d.abbreviation as abbreviation
        """,
            params={"element_id": element_id},
        )
    except:
        raise

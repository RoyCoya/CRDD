from neo4j import GraphDatabase
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from functools import wraps
import re

cjk_regex = re.compile(
    r'[\u4E00-\u9FFF\u3400-\u4DBF\u20000-\u2A6DF'
    r'\u2A700-\u2B73F\u2B740-\u2B81F\u2B820-\u2CEAF'
    r'\u2CEB0-\u2EBEF\uF900-\uFAFF]'
)

driver = GraphDatabase.driver(
    f"bolt://{settings.NEO4J['ip']}:{settings.NEO4J['bolt_port']}",
    auth=(settings.NEO4J['user'], settings.NEO4J['password']), 
    database='ontology'
)

def check_connection(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try: driver.verify_connectivity()
        except Exception as e:return Response({"Database Error": e}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return func(*args, **kwargs)
    return wrapper
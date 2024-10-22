from neo4j import GraphDatabase, Record
from django.conf import settings
from functools import wraps
import atexit

# TODO: 把各个对象的操作方法拆成一个包

driver = GraphDatabase.driver(
    f"bolt://{settings.NEO4J['ip']}:{settings.NEO4J['bolt_port']}",
    auth=(settings.NEO4J["user"], settings.NEO4J["password"]),
    database="ontology",
)
atexit.register(driver.close)


def check_connection(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            driver.verify_connectivity()
        except:
            raise
        return func(*args, **kwargs)

    return wrapper


def run_query(query, params=None) -> list[Record]:
    try:
        result = driver.execute_query(query_=query, parameters_=params)
        data = [r.data() for r in result.records]
        return data
    except:
        raise

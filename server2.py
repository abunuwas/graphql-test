import random
import string

from ariadne import QueryType, make_executable_schema
from ariadne.asgi import GraphQL


query = QueryType()  # A


@query.field("hello")  # B
def resolve_hello(*_):  # C
    return "".join(
        random.choice(string.ascii_letters) for _ in range(10)
    )  # D


schema = """
type Query {    #E
        hello: String
    }
"""

server = GraphQL(make_executable_schema(schema, [query]), debug=True)

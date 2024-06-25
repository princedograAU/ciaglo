from gql.nodes.listing import PropertyNode
from graphene import ObjectType, Schema
from graphene_django import DjangoConnectionField


class Query(ObjectType):
    # listing = DjangoConnectionField(listing)
    properties = DjangoConnectionField(PropertyNode)


schema = Schema(query=Query)

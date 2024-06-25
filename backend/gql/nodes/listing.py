from gql.nodes.base import Connection
from gql.nodes.common import AddressNode
from graphene import Field, relay
from graphene_django import DjangoObjectType
from listing.models import Property


class PropertyNode(DjangoObjectType):
    class Meta:
        model = Property
        interfaces = (relay.Node,)
        connection_class = Connection
        fields = "__all__"

    address = Field(AddressNode)


# class ListingNode(DjangoObjectType):
#     pass

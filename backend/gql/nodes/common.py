from common.models import Address
from gql.nodes.base import Connection
from graphene import relay
from graphene_django import DjangoObjectType


class AddressNode(DjangoObjectType):
    class Meta:
        model = Address
        interfaces = (relay.Node,)
        connection_class = Connection
        fields = "__all__"

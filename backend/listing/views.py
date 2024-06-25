from rest_framework import generics, permissions

from .models import Listing, Property
from .serializers import ListingSerializer, PropertySerializer


class PropertyListView(generics.ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = (permissions.AllowAny,)


class ListingListView(generics.ListAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = (permissions.AllowAny,)

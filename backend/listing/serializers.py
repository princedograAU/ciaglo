from rest_framework.serializers import ModelSerializer

from .models import Listing, Property


class PropertySerializer(ModelSerializer):
    class Meta:
        model = Property
        fields = "__all__"


class ListingSerializer(ModelSerializer):
    class Meta:
        model = Listing
        fields = "__all__"

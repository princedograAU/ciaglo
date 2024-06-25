from django.urls import path

# from rest_framework.routers import DefaultRouter
from .views import ListingListView, PropertyListView

app_name = "listing"

# router = DefaultRouter()
# router.register("property", PropertyViewSet, basename="property")

# urlpatterns = router.urls

urlpatterns = [
    path("property/", PropertyListView.as_view(), name="property"),
    path("listing/", ListingListView.as_view(), name="listing"),
]

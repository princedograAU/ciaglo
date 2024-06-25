from django.contrib.auth import get_user_model
from django.db import models

from common.models import Address, TimestampedModel

User = get_user_model()


class Property(TimestampedModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="properties")
    num_bedrooms = models.IntegerField(default=0)
    num_bathrooms = models.IntegerField(default=0)
    square_feet = models.IntegerField(default=0)
    lot_size = models.FloatField(
        null=True, blank=True
    )  # Lot size in acres or square feet
    year_built = models.IntegerField(null=True, blank=True)
    has_garage = models.BooleanField(default=False)
    has_pool = models.BooleanField(default=False)
    has_basement = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Properties"


class PropertyImage(models.Model):
    property = models.ForeignKey(
        Property, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(upload_to="property_images/")

    def __str__(self):
        return f"Image for {self.property.title}"


class Listing(TimestampedModel):
    AVAILABLE = "AVAILABLE"
    PENDING = "PENDING"
    SOLD = "SOLD"

    PROPERTY_STATUS = ((AVAILABLE, AVAILABLE), (PENDING, PENDING), (SOLD, SOLD))

    property = models.OneToOneField(Property, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    agent = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name="listings"
    )
    status = models.CharField(max_length=50, choices=PROPERTY_STATUS, default=AVAILABLE)
    listing_date = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateField(
        null=True, blank=True
    )  # Optional: When the listing expires
    listed_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="listed_properties"
    )

    def __str__(self):
        return f"Listing for {self.property.title} at ${self.price}"

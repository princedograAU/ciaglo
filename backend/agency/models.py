from django.db import models

from common.models import Address, TimestampedModel, UserProfile


# TODO: This has to be an onboarding process where agencies need to register themselves
# and their details like name and other information should come from ABN details
class Agency(TimestampedModel):
    business_name = models.CharField(max_length=255)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.business_name

    class Meta:
        verbose_name_plural = "Agencies"


class Agent(TimestampedModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    agency = models.ForeignKey(Agency, related_name="agents", on_delete=models.CASCADE)

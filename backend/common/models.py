from django.contrib.auth import get_user_model
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

User = get_user_model()


class TimestampedModel(models.Model):
    # A timestamp representing when this object was created
    dt_created = models.DateTimeField(auto_now_add=True, null=False)

    # A timestamp representing when this object was last updated
    dt_last_changed = models.DateTimeField(auto_now=True, null=False)

    class Meta:
        abstract = True
        ordering = ["-dt_created", "-dt_last_changed"]


class EmailLogs(TimestampedModel):
    """
    Keeps a track of sent emails
    """

    destination = models.EmailField("email address", blank=False, db_index=True)
    message = models.TextField(null=True, help_text="The message we sent.")

    def __str__(self):
        return f"EmailLog: {self.id} - sent to {self.destination}"


# TODO: To improve precision we must use packages like django-address
class Address(TimestampedModel):
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=100)

    def __str__(self):
        return (
            f"{self.street}, {self.city}, {self.state}, {self.zip_code}, {self.country}"
        )


class UserProfile(TimestampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        upload_to="profile_pics/", blank=True, null=True
    )
    date_of_birth = models.DateField(blank=True, null=True)
    location = models.OneToOneField(
        Address, on_delete=models.DO_NOTHING, null=True, blank=True
    )
    phone_number = PhoneNumberField(blank=True, region="AU")  # Default is set to AU
    bio = models.TextField(blank=True)

    def __str__(self) -> str:
        # user can be created without firstname and lastname
        if fullname := f"{self.user.first_name} {self.user.last_name}".strip(""):
            return fullname
        return self.user.username


# class Roles(TimestampedModel):
#     SUPERUSER = "SUPERUSER"
#     AGENT = "AGENT"
#     SELLER = "SELLER"
#     BUYER = "BUYER"

#     role_choices = (
#         (SUPERUSER, SUPERUSER),
#         (AGENT, AGENT),
#         (BUYER, BUYER),
#         (SELLER, SELLER),
#     )

#     roles = models.CharField(choices=role_choices, max_length=128, db_index=True, unique=True)

from django.db import models


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


class Address(TimestampedModel):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=100)

    def __str__(self):
        return (
            f"{self.street}, {self.city}, {self.state}, {self.zip_code}, {self.country}"
        )


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

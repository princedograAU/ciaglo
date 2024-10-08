# Generated by Django 5.1.1 on 2024-09-08 16:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("common", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Property",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("dt_created", models.DateTimeField(auto_now_add=True)),
                ("dt_last_changed", models.DateTimeField(auto_now=True)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("HOUSE", "House"),
                            ("APARTMENT", "Apartment"),
                            ("TOWNHOUSE", "Townhouse"),
                            ("LAND", "Land"),
                            ("RETIREMENT", "Retirement"),
                        ]
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("number_of_bedrooms", models.IntegerField(default=0)),
                ("number_of_bathrooms", models.IntegerField(default=0)),
                ("square_feet", models.IntegerField(default=0)),
                ("area_size", models.FloatField(blank=True, null=True)),
                ("year_built", models.IntegerField(blank=True, null=True)),
                ("number_of_garage", models.IntegerField(default=0)),
                ("number_of_pool", models.IntegerField(default=0)),
                ("number_of_basement", models.IntegerField(default=0)),
                (
                    "address",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="common.address"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Properties",
            },
        ),
        migrations.CreateModel(
            name="Listing",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("dt_created", models.DateTimeField(auto_now_add=True)),
                ("dt_last_changed", models.DateTimeField(auto_now=True)),
                ("price", models.DecimalField(decimal_places=2, max_digits=12)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("AVAILABLE", "AVAILABLE"),
                            ("PENDING", "PENDING"),
                            ("SOLD", "SOLD"),
                        ],
                        default="INACTIVE",
                        max_length=50,
                    ),
                ),
                ("listing_date", models.DateTimeField(auto_now_add=True)),
                ("expiry_date", models.DateField(blank=True, null=True)),
                (
                    "listed_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="listed_properties",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "property",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="listing.property",
                    ),
                ),
            ],
            options={
                "ordering": ["-dt_created", "-dt_last_changed"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="PropertyImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="property_images/")),
                (
                    "property",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="listing.property",
                    ),
                ),
            ],
        ),
    ]

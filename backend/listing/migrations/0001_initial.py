# Generated by Django 5.0.6 on 2024-07-03 05:01

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
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("num_bedrooms", models.IntegerField(default=0)),
                ("num_bathrooms", models.IntegerField(default=0)),
                ("square_feet", models.IntegerField(default=0)),
                ("lot_size", models.FloatField(blank=True, null=True)),
                ("year_built", models.IntegerField(blank=True, null=True)),
                ("has_garage", models.BooleanField(default=False)),
                ("has_pool", models.BooleanField(default=False)),
                ("has_basement", models.BooleanField(default=False)),
                (
                    "address",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="common.address"
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="properties",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-dt_created", "-dt_last_changed"],
                "abstract": False,
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
                        default="AVAILABLE",
                        max_length=50,
                    ),
                ),
                ("listing_date", models.DateTimeField(auto_now_add=True)),
                ("expiry_date", models.DateField(blank=True, null=True)),
                (
                    "agent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="listings",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "listed_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
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
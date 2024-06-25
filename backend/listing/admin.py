from django.contrib import admin

from listing import models


@admin.register(models.Property)
class PropertyAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Listing)
class ListingAdmin(admin.ModelAdmin):
    pass


@admin.register(models.PropertyImage)
class PropertyImageAdmin(admin.ModelAdmin):
    pass

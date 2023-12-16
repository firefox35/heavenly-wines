from django.contrib import admin
from .models import Wine

# Register your models here.


@admin.register(Wine)
class WineAdmin(admin.ModelAdmin):
    list_displayed = ("title", "slug", "type_of_wine", "description", "image")
    list_filter = (
        "year",
        "colour",
        "country",
    )

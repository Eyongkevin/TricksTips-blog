from django.contrib import admin
from rangefilter.filters import DateRangeFilter
from .models import Category

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "created_at",
    )
    list_filter = (("created_at", DateRangeFilter),)
    search_fields = ("name",)
    # TODO: 'prepopulated_fields' Do not work for updates
    prepopulated_fields = {"slug": ("name",)}
    date_hierarchy = "created_at"
    ordering = ("name", "created_at")

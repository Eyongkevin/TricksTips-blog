from django.contrib import admin
from .models import Post

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "get_username", "body", "published_date", "status")
    list_filter = ("status", "published_date")
    search_fields = ("title", "body")
    # TODO: 'prepopulated_fields' Do not work for updates
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "published_date"
    ordering = ("status", "published_date")

    @admin.display(description="Author")
    def get_username(self, obj):
        return obj.author.username

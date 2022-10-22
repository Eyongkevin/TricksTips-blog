from django.contrib import admin
from .models import Post
from .utils import get_minimized_text

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "get_username",
        "get_minimized_body",
        "published_date",
        "status",
    )
    list_filter = ("status", "published_date")
    search_fields = ("title", "body")
    # TODO: 'prepopulated_fields' Do not work for updates
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "published_date"
    ordering = ("status", "published_date")

    @admin.display(description="Author")
    def get_username(self, obj):
        return obj.author.username

    @admin.display(description="Body")
    def get_minimized_body(self, obj):
        return get_minimized_text(obj.body, 60)

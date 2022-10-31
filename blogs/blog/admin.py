from django.contrib import admin
from rangefilter.filters import DateRangeFilter
from .models import Post
from .utils import get_minimized_text

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "get_username",
        "get_minimized_body",
        "category",
        "published_date",
        "status",
        "get_likes",
        "get_dislikes",
        "get_tags",
    )
    list_filter = ("status", ("published_date", DateRangeFilter))
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

    @admin.display(description="Tags")
    def get_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])

    @admin.display(description="Likes")
    def get_likes(self, obj):
        return obj.like_count

    @admin.display(description="Dislikes")
    def get_dislikes(self, obj):
        return obj.dislike_count

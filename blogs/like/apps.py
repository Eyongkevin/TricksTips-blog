from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class LikeConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "blogs.like"
    verbose_name: str = _("Post Likes & Dislikes")

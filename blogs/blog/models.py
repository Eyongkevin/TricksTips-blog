from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Post(models.Model):
    """model for Post"""

    class StatusChoices(models.TextChoices):
        """Status choices for posts if published or not"""

        PUBLISHED = "published", "Published"
        DRAFT = "draft", "Draft"

    title = models.CharField(_("Post Title"), max_length=250, db_index=True)
    slug = models.SlugField(
        _("Post Slug"), max_length=250, unique_for_date="published_date"
    )
    author = models.ForeignKey(
        User,
        verbose_name=_("Post Author"),
        on_delete=models.CASCADE,
        related_name="blog_posts",
    )
    body = models.TextField(_("Post Body"))
    published_date = models.DateTimeField(
        _("Post Published Date"),
        default=timezone.now,
        null=True,
        blank=True,
        editable=False,
    )
    status = models.CharField(
        _("Post Status"),
        max_length=9,
        choices=StatusChoices.choices,
        default=StatusChoices.PUBLISHED,
        db_index=True,
    )
    created_at = models.DateTimeField(_("Post Created Date"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Post Updated Date"), auto_now=True)

    class Meta:
        """set meta"""

        ordering = ("-published_date",)

    def __str__(self):
        return f"{self.title}"

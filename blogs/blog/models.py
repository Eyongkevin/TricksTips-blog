from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.utils.functional import cached_property
from django.db.models import F
from taggit.managers import TaggableManager
from django_ckeditor_5.fields import CKEditor5Field
from blogs.core.models import TimeStampedModel
from blogs.like.models import Like

# Create your models here.


class PostManager(models.Manager):
    """custom post manager"""


class PostQuerySet(models.QuerySet):
    """custom Post query set"""

    def published(self, **kwargs):
        """return all published posts"""

        return self.filter(status="published", **kwargs)

    def this_year_posts(self, **kwargs):
        """return all post that was published this year."""

        return self.filter(created_at__year=timezone.now().year, **kwargs)


class Post(TimeStampedModel):
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
    body = CKEditor5Field("Body", config_name="extends")
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

    objects = models.Manager()
    post = PostManager.from_queryset(PostQuerySet)()
    tags = TaggableManager()

    class Meta:
        """set meta"""

        ordering = ("-published_date",)

    def __str__(self):
        return f"{self.title}"

    @cached_property
    def get_absolute_url(self):
        return reverse(
            "blogs:post_detail",
            args=[
                self.published_date.year,
                self.published_date.month,
                self.published_date.day,
                self.slug,
            ],
        )

    @classmethod
    def get_all_tags(cls):
        return cls.tags.all()

    @property
    def like_count(self):
        """return post's like count or zero if not exist"""

        if self.likes.exists():
            return self.likes.first().like_count
        return 0

    @property
    def dislike_count(self):
        """return post's dislike count or zero if not exist"""

        if self.likes.exists():
            return self.likes.first().dislike_count
        return 0

    def _create_or_update_likes(self, like=True):
        """add like or dislike, or create Like for a post

        Args:
            like (bool, optional): determine if like or dislike. Defaults to True.
        """

        if like:
            lookup = "like_count"
        else:
            lookup = "dislike_count"

        if self.likes.exists():
            lookup_filter = {lookup: F(lookup) + 1}
            self.likes.all().update(**lookup_filter)
        else:
            Like.objects.create(
                post=self,
                like_count=int(like),
                dislike_count=int(not like),
            ).save()

    def add_like(self):
        """add like to a post"""

        self._create_or_update_likes()

    def add_dislike(self):
        """add dislike to a post"""

        self._create_or_update_likes(like=False)

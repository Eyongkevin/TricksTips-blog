from django.db import models
from django.utils.translation import gettext_lazy as _
from blogs.core.models import TimeStampedModel


# Create your models here.
class LinkeManager(models.Manager):
    def most_liked_posts(self, count=10, **kwargs):
        return self.filter(post__status="published", **kwargs).order_by("-like_count")[
            :count
        ]


class Like(TimeStampedModel):
    post = models.ForeignKey(
        "blog.Post",
        verbose_name=_("Post likes and dislikes"),
        on_delete=models.CASCADE,
        related_name="likes",
    )
    like_count = models.PositiveIntegerField()
    dislike_count = models.PositiveIntegerField()
    objects = models.Manager()
    like = LinkeManager()

    def __str__(self):
        return f"{self.like_count} Likes & {self.dislike_count} dislikes on {self.post}"

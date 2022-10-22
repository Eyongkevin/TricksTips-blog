from django.db import models
from django.utils.translation import gettext_lazy as _
from blogs.core.models import TimeStampedModel


# Create your models here.
class Like(TimeStampedModel):
    post = models.ForeignKey(
        "blog.Post",
        verbose_name=_("Post likes and dislikes"),
        on_delete=models.CASCADE,
        related_name="likes",
    )
    like_count = models.PositiveIntegerField()
    dislike_count = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.like_count} Likes & {self.dislike_count} dislikes on {self.post}"

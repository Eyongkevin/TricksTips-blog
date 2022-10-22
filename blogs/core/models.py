from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampedModel(models.Model):
    """abstract model for created and updated at date"""

    created_at = models.DateTimeField(_("Post Created Date"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Post Updated Date"), auto_now=True)

    class Meta:
        abstract = True

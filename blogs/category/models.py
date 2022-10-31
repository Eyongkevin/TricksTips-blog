from django.db import models
from django.utils.translation import gettext_lazy as _
from blogs.core.models import TimeStampedModel


# Create your models here.


class Category(TimeStampedModel):
    """model for Post"""

    name = models.CharField(_("Category Name"), max_length=250, db_index=True)
    slug = models.SlugField(
        _("Category Slug"), max_length=250, unique_for_date="created_at"
    )
    description = models.TextField(_("Description"), blank=True, null=True)

    class Meta:
        """set meta"""

        ordering = ("-name",)

    def __str__(self):
        return f"{self.name}"

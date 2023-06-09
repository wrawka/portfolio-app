from django.db import models
from django.utils.translation import gettext_lazy as _


class Project(models.Model):
    """Represents a coding project in portfolio."""
    title = models.CharField(verbose_name=_('Title'), max_length=100)
    description = models.TextField(verbose_name=_('Description'))
    technology = models.CharField(verbose_name=_('Technology'), max_length=20)
    image = models.ImageField(verbose_name=_('Image'))
    link = models.URLField(verbose_name=_('Project URL'), blank=True)
    source = models.URLField(verbose_name=_('Source code URL'), blank=True)

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')

    def __str__(self) -> str:
        return self.title

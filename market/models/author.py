from django.db import models
from django.utils.translation import gettext_lazy as _


class Author(models.Model):
    first_name = models.CharField(max_length=50, verbose_name=_('First name'))
    last_name = models.CharField(max_length=50, verbose_name=_('Last Name'))
    birth_date = models.DateField(verbose_name=_('Date of Birth'))

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = _('Author')
        verbose_name_plural = _('Authors')

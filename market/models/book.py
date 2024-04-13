from django.db import models
from django.utils.translation import gettext_lazy as _


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name=_("Title"))
    page_count = models.IntegerField(verbose_name=_("Page Count"))
    category = models.CharField(max_length=100, verbose_name=_("Category"))
    author_name = models.CharField(max_length=100, verbose_name=_("Author Name"))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Price"))
    image = models.ImageField(upload_to='books', verbose_name=_("Image"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Book")
        verbose_name_plural = _("Books")

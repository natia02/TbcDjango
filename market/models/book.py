from django.db import models
from django.utils.translation import gettext_lazy as _
from market.models.author import Author
from market.enums.cover import Cover
from market.models.category import Category


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name=_("Title"))
    cover = models.IntegerField(choices=Cover.choices, default=Cover.SOLID, verbose_name=_("Cover"))
    page_count = models.IntegerField(verbose_name=_("Page Count"))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Price"))
    image = models.ImageField(upload_to='book', verbose_name=_("Image"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_("Author"))
    category = models.ManyToManyField(Category, verbose_name=_("Category"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Book")
        verbose_name_plural = _("Books")

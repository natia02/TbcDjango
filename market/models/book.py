from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    page_count = models.IntegerField()
    category = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


from django.db.models import IntegerChoices


class Cover(IntegerChoices):
    SOLID = 1, 'Solid'
    SOFT = 2, 'Soft'
    SPECIAL = 3, 'Special'

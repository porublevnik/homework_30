from django.core.validators import MinLengthValidator
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=10, validators=[MinLengthValidator(5)], unique=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

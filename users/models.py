from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models

from users.validators import EmailDomainValidator, AgeValidator


class Location(models.Model):
    name = models.CharField(max_length=250)
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True)

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"

    def __str__(self):
        return self.name


class User(AbstractUser):
    ROLES = [('member', 'member'), ('moderator', 'moderator'), ('admin', 'admin')]
    role = models.CharField(max_length=250, choices=ROLES, default="member")
    age = models.PositiveIntegerField(null=True, blank=True)
    locations = models.ManyToManyField(Location)
    birth_date = models.DateField(default='2000-01-01')
    email = models.EmailField()

    def save(self, *args, **kwargs):
        self.set_password(raw_password=self.password)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username

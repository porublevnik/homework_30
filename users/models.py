from django.contrib.auth.models import AbstractUser
from django.db import models

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




    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username

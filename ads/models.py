from django.db import models
from users.models import User
from categories.models import Category
from users.models import User



class Ad(models.Model):
    PUBLISHED_STATUS = [
        ("TRUE", "True"),
        ("FALSE", "False")
    ]
    # id = models.IntegerField()
    name = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    description = models.TextField()
    is_published = models.BooleanField()
    image = models.ImageField(upload_to='images/', default=None)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return self.name
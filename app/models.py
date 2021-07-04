from django.db import models
from django.contrib.auth import get_user_model
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.utils.translation import gettext_lazy as _

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='product')
    image_thumbnail = ImageSpecField(source='product', processors=[ResizeToFill(100, 50)], format='JPEG', options={'quality': 60})

    def __str__(self):
        return self.name

class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    user = models.ForeignKey('users.User', on_delete=models.PROTECT)
    amount = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(_("商品単価"))
    total_price = models.PositiveIntegerField(_("小計"))
    created_at = models.DateTimeField(auto_now=True)


# Create your models here.

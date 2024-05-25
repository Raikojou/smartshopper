from django.db import models
from django.utils.text import slugify

class StoreCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Store(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(
        help_text = "Don't fill, will be slugified",
        max_length=100,
        unique=True,
        blank=True)
    category = models.ManyToManyField(
        StoreCategory,
        related_name='category')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Coupon(models.Model):
    code = models.CharField(max_length=100)
    description = models.CharField(
        max_length=255,
        blank=True,
        null=True)
    store = models.ForeignKey(
        Store,
        help_text = "Store doesn't exist? Create new Store first",
        on_delete=models.CASCADE,
        related_name='coupons',
        blank=True,
        null=True)

    def __str__(self):
        return f"{self.store.name} - {self.code}"
from django.db import models


class Size(models.Model):
    sizes = models.CharField(max_length=25)

    def __str__(self):
        return "{}".format(self.sizes)

class Item(models.Model):
    """ Base class for all item"""
    GENDER_CHOICES = (
        ('Men', "Male"),
        ('Women', 'Female')
    )

    item_title = models.CharField(max_length=300, blank=False)
    item_brand = models.CharField(max_length=255, blank=False)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, blank=False)
    item_price = models.FloatField(blank=False)
    item_type = models.CharField(max_length=250, blank=False)
    item_color = models.CharField(max_length=100, blank=False)
    is_in_stock = models.BooleanField(default=False, blank=False)
    description = models.TextField(blank=False)
    sizes = models.ManyToManyField(Size, related_name="shoe_size", blank=True)
    category = models.CharField(max_length=200, default="Category", blank=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}-{}".format(self.item_brand, self.item_title)


class ItemImage(models.Model):
    itemImage = models.ForeignKey('Item', related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(blank=False)

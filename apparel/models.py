from django.db import models

class Size(models.Model):
    sizes = models.CharField(max_length=25)

    def __str__(self):
        return "{}".format(self.sizes)

class Item(models.Model):
    """ Base class for all item
    it contains all common field
    it is abstract"""
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
    item_image = models.URLField(max_length=1500, blank=False)
    is_in_stock = models.BooleanField(default=False, blank=False)
    description = models.TextField(blank=False)
    sizes = models.ManyToManyField(Size, related_name="shoe_size")
    category = models.CharField(max_length=200, default="Category", blank=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}-{}".format(self.item_brand, self.item_title)

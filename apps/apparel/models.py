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
    sizes = models.ManyToManyField(Size, related_name="item_size", blank=True)
    category = models.CharField(max_length=200, default="Category", blank=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}-{}".format(self.item_brand, self.item_title)

    def serialize(self):
        as_dict = {
            "id": self.pk,
            "item_title": self.item_title,
            "item_brand": self.item_brand,
            "gender": self.gender,
            "item_price": self.item_price,
            "is_in_stock": self.is_in_stock,
            "description": self.description,
            "sizes": [s.sizes for s in self.sizes.all()],
            "category": self.category,
            "item_images": [image.image.url for image in self.images.all()],
        }

        return as_dict



class ItemImage(models.Model):
    itemImage = models.ForeignKey('Item', related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(blank=False)

    def __str__(self):
        return "{}".format(self.itemImage.item_title)


class Customer(models.Model):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    phone = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=254, blank=False)
    address = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Order(models.Model):
    item = models.ForeignKey('Item', related_name='ordered_item', on_delete=models.CASCADE)
    buyer = models.ForeignKey('Customer', related_name="purchaser", on_delete=models.CASCADE)
    when = models.DateTimeField(auto_now_add=True)
    is_new_buyer = models.BooleanField(default=True, blank=True)
    quantity = models.IntegerField(blank=False)
    cash_on_delivery = models.BooleanField(default=False, blank=False)
    paypal = models.BooleanField(default=False, blank=False)

    def __str__(self):
        return '{} - {}'.format(self.item.item_title, self.item.item_brand)

    def serialize(self):
        as_dict = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone": self.phone,
            "email": self.email,
            "address": self.address,
            "quantity": self.quantity,
            "cash_on_delivery": self.cash_on_delivery,
            "paypal": self.paypal
        }

        return as_dict

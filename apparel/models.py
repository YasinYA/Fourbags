from django.db import models


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
    item_color = models.CharField(max_length=100, blank=False)
    is_in_stock = models.BooleanField(default=False, blank=False)
    description = models.TextField(blank=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}-{}".format(self.item_brand, self.item_title)

    class Meta:
           abstract = True


class Size(models.Model):
    sizes = models.CharField(max_length=25, blank=False)

    def __str__(self):
        return "{}".format(self.sizes)

class Cloth(Item):

    # Cloth categories
    CLOTH_CATEGORY_CHOICES = (
        ('outerwear', 'OUTERWEAR'),
        ('socks', 'SOCKS'),
        ('shirts', 'SHIRTS'),
        ('t-shirts', 'T-SHIRTS'),
        ('polo', 'POLO'),
        ('shirts', 'SHIRTS'),
        ('underwear', 'UNDERWEAR'),
        ('pants', 'PANTS'),
        ('jeans', 'JEANS'),
        ('shorts', 'SHORTS'),
        ('ethnic', 'ETHNIC'),
        ('wear', 'WEAR'),
        ('beachwear', 'BEACHWEAR'),
    )

    sizes = models.ManyToManyField(Size, related_name="cloth_sizes")
    category = models.CharField(max_length=200, choices=CLOTH_CATEGORY_CHOICES, default="Category", blank=False)

class Shoe(Item):
    SHOES_CATEGORY_CHOICES = (
        ('SLIP-ONS', 'SLIP-ONS'),
        ('HIGH TOPS', 'HIGH TOPS'),
        ('LOW TOPS', 'LOW TOPS'),
        ('SANDALS & FLIP FLOPS', 'SANDALS & FLIP FLOPS'),
        ('SNEAKERS & PLIMSOLLS', 'SNEAKERS & PLIMSOLLS'),
        ('FORMAL', 'FORMAL'),
        ('SPORTS', 'SPORTS'),
        ('BOOTS', 'BOOTS'),
        ('BROGUES & DERBIES', 'BROGUES & DERBIES'),
    )

    sizes = models.ManyToManyField(Size, related_name="shoe_size")
    category = models.CharField(max_length=200, choices=SHOES_CATEGORY_CHOICES, default="Category", blank=False)



class ItemImage(models.Model):
    cloth_images = models.ForeignKey(Cloth, related_name="cloth_images", on_delete=models.CASCADE, blank=False)
    shoes_images = models.ForeignKey(Shoe, related_name="shoes_images", on_delete=models.CASCADE, blank=False)
    images = models.ImageField(upload_to='static/images/clothes', max_length=1000)

    def __str__(self):
        return "{}".format(self.item_images.item_title)

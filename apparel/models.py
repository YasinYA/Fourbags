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
    item_price = models.IntegerField(blank=False)
    item_color = models.CharField(max_length=100, blank=False)
    is_in_stock = models.BooleanField(default=False, blank=False)
    description = models.TextField(blank=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}-{}".format(self.item_brand, self.item_title)

    class Meta:
           abstract = True


class Size(models.Model):

    # Cloth Size choices all together (shirts and pants)
    SIZE_CHOICES = (
        ('S', "Small"),
        ('M', 'Medium'),
        ('L', "Large"),
        ('XL', 'Extra-Large'),
        ('28', "28"),
        ('29', '29'),
        ('30', "30"),
        ('31', '31'),
        ('32', "32"),
        ('33', '33'),
        ('34', "34"),
        ('35', '35'),
        # shoe size
        ('36', "36"),
        ('37', '37'),
        ('38', "38"),
        ('39', '39'),
        ('40', "40"),
        ('41', '41'),
        ('42', "42"),
        ('43', '43'),
        ('44', "44"),
        ('45', '45'),
    )

    sizes = models.CharField(max_length=25, choices=SIZE_CHOICES, blank=False)

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
    item_images = models.ForeignKey(Cloth, related_name="cloth_images", on_delete=models.CASCADE, blank=False)
    images = models.ImageField(upload_to='static/images/clothes', max_length=1000)

    def __str__(self):
        return "{}".format(self.item_images.item_title)

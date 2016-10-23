from django.contrib import admin
from .models import Item, Size, ItemImage, Order

admin.site.register(Item)
admin.site.register(Size)
admin.site.register(ItemImage)
admin.site.register(Order)


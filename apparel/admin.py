from django.contrib import admin
from .models import Cloth, ItemImage, Size, Shoe

admin.site.register(Cloth)
admin.site.register(Size)
admin.site.register(ItemImage)

admin.site.register(Shoe)


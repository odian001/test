from django.contrib import admin
from .models import Ingredient
from .models import GroceryStore
from .models import PriceData
from .models import PriceHistory
from .models import StoreCollection
from .models import ShoppingListCollection

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(GroceryStore)
admin.site.register(PriceData)
admin.site.register(PriceHistory)
admin.site.register(StoreCollection)
admin.site.register(ShoppingListCollection)
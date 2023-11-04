from django.contrib import admin
from .models import Ingredient
from .models import GroceryStore
from .models import PriceData
from .models import PriceHistory

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(GroceryStore)
admin.site.register(PriceData)
admin.site.register(PriceHistory)
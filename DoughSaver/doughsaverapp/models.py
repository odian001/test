from django.contrib.auth.models import User
from django.db import models

class Ingredient(models.Model):
    class Meta:
        managed = False
        db_table = 'Ingredient'
    IngredientID = models.IntegerField(primary_key=True, db_column='IngredientID')
    IngredientName = models.CharField(max_length=150, db_column='IngredientName')
    Brand = models.CharField(max_length=25, blank=True, null=True, db_column='Brand')
    Quantity = models.DecimalField(max_digits=6, decimal_places=2, db_column='Quantity')
    Unit = models.CharField(max_length=25, db_column='Unit')
    IsPrivate = models.BooleanField(db_column='IsPrivate')
    PrivateUID = models.IntegerField(blank=True, null=True, db_column='PrivateUID')

class GroceryStore(models.Model):
    class Meta:
        managed = False
        db_table = 'GroceryStore'
    StoreId = models.IntegerField(primary_key=True, db_column='StoreId')
    StoreName = models.CharField(max_length=25, db_column='StoreName')
    Address = models.CharField(max_length=75, db_column='Address')
   
class PriceData(models.Model):
    class Meta:
        unique_together = ('StoreID', 'IngredientID')
        db_table = 'PriceData'
        managed = False
    DjangoID = models.AutoField(primary_key=True, unique=True, db_column='DjangoID')
    StoreID = models.ForeignKey(GroceryStore, on_delete=models.CASCADE, db_column='StoreID', related_name='store')
    IngredientID = models.ForeignKey(Ingredient, on_delete=models.CASCADE, db_column='IngredientID', related_name='ingredient')
    Link = models.CharField(max_length=150, db_column='Link')
    RegularPrice = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, db_column='RegularPrice')
    CurrentPrice = models.DecimalField(max_digits=6, decimal_places=2, db_column='CurrentPrice')
    UpdateTimestamp = models.DateTimeField(db_column='UpdateTimestamp')
    IsPaused = models.BooleanField(blank=True, null=True, db_column='IsPaused')
    
class PriceHistory(models.Model):
    class Meta:
        unique_together = ('StoreID', 'IngredientID', 'UpdateTimestamp')
        db_table = 'PriceHistory'
        managed = False
    DjangoID = models.AutoField(primary_key=True, unique=True, db_column='DjangoID')
    StoreID = models.ForeignKey(GroceryStore, on_delete=models.CASCADE, db_column='StoreID')
    IngredientID = models.ForeignKey(Ingredient, on_delete=models.CASCADE, db_column='IngredientID')
    UpdateTimestamp = models.DateTimeField()
    HistoricalPrice = models.DecimalField(max_digits=6, decimal_places=2)



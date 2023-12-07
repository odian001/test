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
    StoreId = models.AutoField(primary_key=True, db_column='StoreId')
    StoreName = models.CharField(max_length=25, db_column='StoreName')
    Address = models.CharField(max_length=75, db_column='Address')
    def __str__(self):
        return self.StoreName + " - " + self.Address
       
class ShoppingListNames(models.Model):
    class Meta:
        managed = False
        db_table = 'ShoppingListNames'
    ListID = models.AutoField(primary_key=True, db_column='ListID')
    ListName = models.CharField(max_length=75, db_column='ListName')
    UserID = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='UserID')

    def __str__(self):
        return f"{self.ListName} - {self.Ingredient.IngredientName} ({self.Quantity} {self.Ingredient.Unit})"
        
class ShoppingList(models.Model):
    class Meta:
        managed = False
        db_table = 'ShoppingList'
        unique_together = (('ListID', 'Ingredient'),)
    ListID = models.AutoField(primary_key=True, db_column='ListID')
    Ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, db_column='IngredientID')
    StoreID = models.ForeignKey(GroceryStore, on_delete=models.CASCADE, db_column='StoreID')
    Quantity = models.IntegerField(db_column='Quantity')

    def __str__(self):
        return f"{self.ListName} - {self.Ingredient.IngredientName} ({self.Quantity} {self.Ingredient.Unit})"
        
        
class ShoppingListCollection(models.Model):
    DjangoID = models.AutoField(primary_key=True, unique=True, db_column='DjangoID')
    UserID = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='UserID')
    ListID = models.ForeignKey(ShoppingList, on_delete=models.CASCADE, db_column='ListID')

    class Meta:
        managed = False
        db_table = 'ShoppingListCollection'
        unique_together = (('UserID', 'ListID'),)

    def __str__(self):
        return f'{self.UserID} - Shopping List Collection'
        
class StoreCollection(models.Model):
    DjangoID = models.AutoField(primary_key=True, unique=True, db_column='DjangoID')
    UserID = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='UserID')
    StoreID = models.ForeignKey(GroceryStore, on_delete=models.CASCADE, db_column='StoreID')

    class Meta:
        managed = False
        db_table = 'StoreCollection'
        unique_together = (('UserID', 'StoreID'),)

    def __str__(self):
        return f'{self.UserID} - Store Collection'
        
class IngredientCollection(models.Model):
    DjangoID = models.AutoField(primary_key=True, unique=True, db_column='DjangoID')
    UserID = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='UserID')
    IngredientID = models.ForeignKey(Ingredient, on_delete=models.CASCADE, db_column='IngredientID')
    TargetPrice = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, db_column='target_price')

    class Meta:
        managed = False
        db_table = 'IngredientCollection'
        unique_together = (('UserID', 'IngredientID'),)

    def __str__(self):
        return f'{self.UserID} - Ingredient Collection'
    

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

class Recipe(models.Model):
    class Meta:
        db_table = 'Recipe'
        managed = False
    RecipeID = models.AutoField(primary_key=True, unique=True, db_column='RecipeID')
    RecipeName = models.CharField(max_length=150, db_column='RecipeName')
    IsPrivate = models.BooleanField(db_column='IsPrivate')
    PrivateUID = models.IntegerField(db_column='PrivateUID', null=True)
    Ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, db_column='IngredientID')
    Quantity = models.DecimalField(max_digits=10, decimal_places=0, db_column='Quantity')
    Unit = models.CharField(max_length=25, db_column='Unit')

class RecipeCollection(models.Model):
    DjangoID = models.AutoField(primary_key=True, unique=True, db_column='DjangoID')
    UserID = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='UserID')
    RecipeID = models.ForeignKey(Recipe, on_delete=models.CASCADE, db_column='RecipeID')
    TargetPrice = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, db_column='target_price')

    class Meta:
        managed = False
        db_table = 'RecipeCollection'
        unique_together = (('UserID', 'RecipeID'),)

    def __str__(self):
        return f'{self.UserID} - Recipe Collection'
        
#class Shopping

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'

    def __str__(self):
        return self.username
    


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


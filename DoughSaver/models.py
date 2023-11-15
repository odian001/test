# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Customer(models.Model):
    userid = models.AutoField(db_column='UserId', primary_key=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=60)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=25)  # Field name made lowercase.
    email = models.CharField(db_column='Email', unique=True, max_length=50)  # Field name made lowercase.
    primarylocation = models.IntegerField(db_column='PrimaryLocation')  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=75, blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate')  # Field name made lowercase.
    lastlogin = models.DateTimeField(db_column='LastLogin')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Customer'


class Grocerystore(models.Model):
    storeid = models.AutoField(db_column='StoreId', primary_key=True)  # Field name made lowercase.
    storename = models.CharField(db_column='StoreName', max_length=25)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=75)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GroceryStore'


class Ingredient(models.Model):
    ingredientid = models.AutoField(db_column='IngredientID', primary_key=True)  # Field name made lowercase.
    ingredientname = models.CharField(db_column='IngredientName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    brand = models.CharField(db_column='Brand', max_length=25, blank=True, null=True)  # Field name made lowercase.
    quantity = models.FloatField(db_column='Quantity')  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=25)  # Field name made lowercase.
    isprivate = models.IntegerField(db_column='IsPrivate')  # Field name made lowercase.
    privateuid = models.IntegerField(db_column='PrivateUID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Ingredient'


class Ingredientcollection(models.Model):
    userid = models.OneToOneField('AuthUser', models.DO_NOTHING, db_column='UserID', primary_key=True)  # Field name made lowercase. The composite primary key (UserID, IngredientID) found, that is not supported. The first column is selected.
    ingredientid = models.OneToOneField(Ingredient, models.DO_NOTHING, db_column='IngredientID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IngredientCollection'
        unique_together = (('userid', 'ingredientid'),)


class Pricedata(models.Model):
    storeid = models.OneToOneField(Grocerystore, models.DO_NOTHING, db_column='StoreID', primary_key=True)  # Field name made lowercase. The composite primary key (StoreID, IngredientID) found, that is not supported. The first column is selected.
    ingredientid = models.ForeignKey(Ingredient, models.DO_NOTHING, db_column='IngredientID')  # Field name made lowercase.
    link = models.CharField(db_column='Link', max_length=150)  # Field name made lowercase.
    regularprice = models.FloatField(db_column='RegularPrice', blank=True, null=True)  # Field name made lowercase.
    currentprice = models.FloatField(db_column='CurrentPrice')  # Field name made lowercase.
    updatetimestamp = models.DateTimeField(db_column='UpdateTimestamp')  # Field name made lowercase.
    ispaused = models.IntegerField(db_column='IsPaused', blank=True, null=True)  # Field name made lowercase.
    djangoid = models.AutoField(db_column='DjangoID', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PriceData'
        unique_together = (('storeid', 'ingredientid'),)


class Pricehistory(models.Model):
    storeid = models.OneToOneField(Grocerystore, models.DO_NOTHING, db_column='StoreID', primary_key=True)  # Field name made lowercase. The composite primary key (StoreID, IngredientID, UpdateTimestamp) found, that is not supported. The first column is selected.
    ingredientid = models.ForeignKey(Ingredient, models.DO_NOTHING, db_column='IngredientID')  # Field name made lowercase.
    updatetimestamp = models.DateTimeField(db_column='UpdateTimestamp')  # Field name made lowercase.
    historicalprice = models.FloatField(db_column='HistoricalPrice')  # Field name made lowercase.
    djangoid = models.AutoField(db_column='DjangoID', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PriceHistory'
        unique_together = (('storeid', 'ingredientid', 'updatetimestamp'),)


class Recipe(models.Model):
    recipeid = models.IntegerField(db_column='RecipeID', primary_key=True)  # Field name made lowercase. The composite primary key (RecipeID, IngredientID) found, that is not supported. The first column is selected.
    recipename = models.CharField(db_column='RecipeName', max_length=50)  # Field name made lowercase.
    isprivate = models.IntegerField(db_column='IsPrivate')  # Field name made lowercase.
    privateuid = models.IntegerField(db_column='PrivateUID', blank=True, null=True)  # Field name made lowercase.
    ingredientid = models.ForeignKey(Ingredient, models.DO_NOTHING, db_column='IngredientID')  # Field name made lowercase.
    quantity = models.DecimalField(db_column='Quantity', max_digits=10, decimal_places=0)  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=25)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Recipe'
        unique_together = (('recipeid', 'ingredientid'),)


class Recipecollection(models.Model):
    userid = models.OneToOneField('AuthUser', models.DO_NOTHING, db_column='UserID', primary_key=True)  # Field name made lowercase. The composite primary key (UserID, RecipeID) found, that is not supported. The first column is selected.
    recipeid = models.ForeignKey(Recipe, models.DO_NOTHING, db_column='RecipeID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RecipeCollection'
        unique_together = (('userid', 'recipeid'),)


class Shoppinglist(models.Model):
    listid = models.IntegerField(db_column='ListID', primary_key=True)  # Field name made lowercase. The composite primary key (ListID, IngredientID, StoreID) found, that is not supported. The first column is selected.
    listname = models.CharField(db_column='ListName', max_length=25)  # Field name made lowercase.
    ingredientid = models.ForeignKey(Ingredient, models.DO_NOTHING, db_column='IngredientID')  # Field name made lowercase.
    storeid = models.ForeignKey(Grocerystore, models.DO_NOTHING, db_column='StoreID')  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.
    budget = models.IntegerField(db_column='Budget', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ShoppingList'
        unique_together = (('listid', 'ingredientid', 'storeid'),)


class Shoppinglistcollection(models.Model):
    userid = models.OneToOneField('AuthUser', models.DO_NOTHING, db_column='UserID', primary_key=True)  # Field name made lowercase. The composite primary key (UserID, ListID) found, that is not supported. The first column is selected.
    listid = models.ForeignKey(Shoppinglist, models.DO_NOTHING, db_column='ListID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ShoppingListCollection'
        unique_together = (('userid', 'listid'),)


class Storecollection(models.Model):
    userid = models.OneToOneField('AuthUser', models.DO_NOTHING, db_column='UserID', primary_key=True)  # Field name made lowercase. The composite primary key (UserID, StoreID) found, that is not supported. The first column is selected.
    storeid = models.OneToOneField(Grocerystore, models.DO_NOTHING, db_column='StoreID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StoreCollection'
        unique_together = (('userid', 'storeid'),)


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


class DoughsaverappUserstoreselection(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'doughsaverapp_userstoreselection'


class DoughsaverappUserstoreselectionStores(models.Model):
    id = models.BigAutoField(primary_key=True)
    userstoreselection = models.ForeignKey(DoughsaverappUserstoreselection, models.DO_NOTHING)
    grocerystore = models.ForeignKey(Grocerystore, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'doughsaverapp_userstoreselection_stores'
        unique_together = (('userstoreselection', 'grocerystore'),)

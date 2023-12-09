from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import *


urlpatterns = [
    path('index/', views.index, name = "index"),
    path('logout_user/', auth_views.LogoutView.as_view(next_page=('index')), name = "logout"),
    path('accountcreation/', views.accountcreation, name = 'accountcreation'),
    path('current_prices/', PriceDataListView.as_view(), name='current_prices'),
    path('ingredient_list/', views.ingredient_list, name='ingredient_list'),
    path('price_history/', price_history_list, name='price_history_list'),
    path('ingredient_search/', views.ingredient_search, name='ingredient_search'),
    path('store_selection/', views.store_selection, name='store_selection'),
    path('view_stores/', views.view_selected_stores, name='view_selected_stores'),
    path('price_comparison/', views.price_comparison_options, name='price_comparison_options'),
    path('ingredient/<int:IngredientID>/', ingredient_detail, name='ingredient_detail'),
    path('recipe_search/', views.recipe_search, name='recipe_search'),
    path('user_ingredients/', user_ingredients, name='user_ingredients'),
    path('user_recipes/', user_recipes, name='user_recipes'),
    #path('shopping_list/<int:list_id>/', shopping_list_detail, name='shopping_list_detail'),
    path('recipe/<int:RecipeID>/', views.recipe_detail, name='recipe_detail'),
    path('untrack_item/', untrack_item, name='untrack_item'),
    path('track_item/', track_item, name='track_item'),
    path('untrack_recipe/', untrack_recipe, name='untrack_recipe'),
    path('track_recipe/', track_recipe, name='track_recipe'),
    path('shopping_lists/', views.shopping_lists, name='shopping_lists'),
    path('shopping_lists/<int:list_id>/', views.shopping_lists, name='shopping_lists_with_id'),
    path('shopping_lists/<int:list_id>/<str:algorithm>/', views.shopping_lists, name='shopping_lists_with_id_algorithm'),
    path('target_price_ingredient/', target_price_ingredient, name='target_price_ingredient'),
    path('target_price_recipe/', target_price_recipe, name='target_price_recipe'),
    path('remove_item_from_list/', remove_item_from_list, name='remove_item_from_list'),
    path('settings/', settings_page, name='settings_page'),


]



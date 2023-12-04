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
    path('shopping_list/<int:list_id>/', shopping_list_detail, name='shopping_list_detail'),
    path('recipe/<int:RecipeID>/', views.recipe_detail, name='recipe_detail')
]



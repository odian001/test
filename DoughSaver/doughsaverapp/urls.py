from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('index', views.index, name = "index"),
    path('footer', views.footer, name = "footer"),
    path('heading', views.heading, name = "heading"),
    path('accountcreation', views.accountcreation, name = 'accountcreation'),
    path('current_prices/', PriceDataListView.as_view(), name='current_prices'),
    path('ingredient_list/', views.ingredient_list, name='ingredient_list'),
    path('price_history/', price_history_list, name='price_history_list'),
]

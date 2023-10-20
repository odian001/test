from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name = "index"),
    path('footer', views.footer, name = "footer"),
    path('heading', views.heading, name = "heading"),
]
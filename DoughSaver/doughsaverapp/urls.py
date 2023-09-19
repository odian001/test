from django.urls import path
from . import views

urlpatterns = [
    path('doughsaverapp/', views.doughsaverapp, name='doughsaverapp'),
]
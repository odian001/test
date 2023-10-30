from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView
from django.shortcuts import render
from doughsaverapp.models import *


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def footer(request):
    template = loader.get_template('footer.html')
    return HttpResponse(template.render())

def heading(request):
    template = loader.get_template('heading.html')
    return HttpResponse(template.render())

def accountcreation(request):
    template = loader.get_template('accountcreation.html')
    return HttpResponse(template.render())


class PriceDataListView(ListView):
    model = PriceData
    template_name = 'price_data_list.html'
    context_object_name = 'price_data_list'

def ingredient_list(request):
    ingredients = Ingredient.objects.all()  # Query all Ingredient objects
    context = {'ingredients': ingredients}
    return render(request, 'ingredient_list.html', context)
    
def current_prices(request):
    # Retrieve PriceData objects along with related GroceryStore and Ingredient
    price_data_list = PriceData.objects.select_related('store', 'ingredient').all()
    context = {'price_data_list': price_data_list}
    return render(request, 'current_prices.html', context)

def price_history_list(request):
    price_history_list = PriceHistory.objects.all()
    context = {'price_history_list': price_history_list}
    return render(request, 'price_history_list.html', context)